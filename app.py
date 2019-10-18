from flask import Flask, jsonify, redirect, url_for, render_template, request, session
import os
from pymongo import MongoClient
from instagram_private_api import Client, ClientCompatPatch, ClientLoginError, ClientCheckpointRequiredError, ClientChallengeRequiredError
import json
from bson import json_util
import pandas as pd
from models import User, Network, assests
from tqdm import tqdm
import graphistry
import time
# set flask name
app = Flask(__name__)
# portnum = 8080  # custom port number
# set environment variable
# app.config['SESSION_COOKIE_SECURE'] = True THIS FUCKED ME OVER
# set default mongodb URI
os.environ['MONGO_URI'] = 'mongodb://localhost:27017/Gram'
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
app.config['MONGO_URI'] = host
app.config['SECRET_KEY'] = os.urandom(24)
app.secret_key = os.environ.get('SECRET_KEY')
# instantiate the database
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database('test')    # get default database name
users = db.users  # user collection
visitor = db.visitor
key = os.environ.get('graphistry_key')
# merge root and index routes
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'user' in session:
            username = session['user']['username']
            return redirect(url_for('dashboard'))
        else:
            return render_template('home.html')

    if request.method == 'POST':
        return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('dashboard', user=session['user']))
    if request.method == 'POST':
        login_user = db.users.find_one({'username': request.form['username']})

        if login_user:
            data = {
                'username': login_user['username'],
                'is_active': login_user['is_active'],
                'follower_count': login_user['follower_count'],
                'following_count': login_user['following_count'],
                'profile_picture': login_user['profile_picture'],
                'full_name': login_user['full_name'],
                'rank_token': login_user['rank_token'],
                'graph': login_user['graph']
            }

            session['user'] = json.loads(json_util.dumps(data))
            return redirect(url_for('dashboard', user=session['user']))
        else:
            try:
                # try logging in user
                Client(
                    request.form['username'], request.form['password'])
            except ClientLoginError:
                return redirect(url_for('login'))
            except ClientChallengeRequiredError:
                # redirect the user back to the login page if username and passwword fails
                time.sleep(60)

            except ClientCheckpointRequiredError:
                time.sleep(60)

            # set client agent
            api = Client(request.form['username'],
                         request.form['password'])
            # create a new user from the username store it into the variable called me :)
            me = User()
            # set the username
            me.set_username(request.form['username'])
            # set user to active
            me.set_to_active()
            # create user is
            user_id = api.authenticated_user_id
            # set my id
            me.set_id(user_id)
            # set set full name
            me.set_name(api.user_info(me.get_id())['user']['full_name'])
            # set rank token
            me.set_rank_token(api.generate_uuid())
            #####################!You need at least 32 cores to run this fuck shit!############################################
            # test = []
            # results = api.user_followers(me.id, me.rank_token)
            # test.extend(results.get('users', []))
            # next_max_id = results.get('next_max_id')
            # while next_max_id:
            #     results = api.user_followers(
            #         me.id, me.rank_token, max_id=next_max_id)
            #     test.extend(results.get('users', []))
            #     if len(test) >= 8000:
            #         break
            #     next_max_id2 = results.get('next_max_id')
            # test2 = []
            # results2 = api.user_following(me.id, me.rank_token)
            # test2.extend(results2.get('users', []))
            # next_max_id2 = results2.get('next_max_id')
            # while next_max_id2:
            #     results2 = api.user_following(
            #         me.id, me.rank_token, max_id=next_max_id)
            #     test2.extend(results2.get('users', []))
            #     if len(test2) >= 8000:
            #         break
            #     next_max_id2 = results2.get('next_max_id')

            # relations = []
            # for user in test:
            #      # grab followed user id
            #     followed_id = user['pk']
            #     followed_name = user['full_name']
            #     relations.append((
            #         me.get_id(), followed_id, me.get_full_name(), followed_name))
            #     # if test2.get('users') is not None:
            #     for users in test2:
            #         relations.append(
            #             (followed_id, users['pk'], followed_name, users['full_name']))
            # df = pd.DataFrame(relations, columns=[
            #     'src_id', 'dst_id', 'src_name', 'dst_name'])
            # key = os.environ.get('graphistry_key')
            # graphistry.register(key=key)
            # graph = graphistry.bind(source='src_name',
            #                         destination='dst_name').edges(df).plot()
            #####################!You need at least 32 cores to run this fuck shit!############################################
            # followers
            followers = api.user_followers(
                me.get_id(), me.get_rank_token())
            # following
            following = api.user_following(
                me.get_id(), me.get_rank_token())
            # set the likes
            # me.set_likes(api.feed_liked())
            # print(me.likes)
            # set followers count
            count = 0
            for user in followers['users']:
                count += 1
            me.set_follower_count(count)
            val = 0
            for user in following['users']:
                val += 1
            # set following count
            me.set_following_count(val)
            # set picture
            me.set_picture(api.user_info(me.id)['user']['profile_pic_url'])
            # wtf is this
            # print(api.explore())
            # follow relationtionships
            api.story_viewers()
            follow_relationships = []
            # create network
            for user in tqdm(following['users']):
                # grab followed user id
                followed_user_id = user['pk']
                # grab followed user full name
                followed_user_name = user['full_name']
                # append my id, followed user id, my full name, followed user full name
                follow_relationships.append(
                    (me.get_id(), followed_user_id, me.get_full_name(), followed_user_name))
                # if you are following no one break
                if following.get('users') is not None:
                    for users in followers['users']:
                        follow_relationships.append(
                            (followed_user_id, users['pk'], followed_user_name, users['full_name']))
            # set network
            me.set_network(follow_relationships)
            df = pd.DataFrame(follow_relationships, columns=[
                'src_id', 'dst_id', 'src_name', 'dst_name'])
            graphistry.register(key=key)
            me.set_graph(graphistry.bind(source='src_name',
                                         destination='dst_name').edges(df).plot())
            graph = str(me.get_graph())
            # set our graph
            # me.set_graph(graph)
            # get data from user object
            data = me.json()
            # push data to our collection in data base
            db.users.insert_one(json.loads(json_util.dumps(data)))
            # store session data as cookie
            session['user'] = json.loads(json_util.dumps(data))
            # redirect to dashboard
            return redirect(url_for('dashboard', user=session['user']))

    if request.method == 'GET':
        return render_template('login.html')
        #     # if the user does pull the user data and return user to dashboard
        #     if users.find_one({'username': request.form['username']}):


@app.route('/dashboard', methods=['GET'])
def dashboard():
    if request.method == 'GET':
        if 'user' in session:
            user = session['user']
            return render_template('dashboard.html', user=user)
        else:
            return redirect(url_for('index'))


@app.route('/data', methods=['GET'])
def somedata():
    if request.method == 'GET':
        followers = []
    results = api.user_followers(user_id)
    followers.extend(results.get('users', []))

    next_max_id = results.get('next_max_id')
    while next_max_id:
        results = api.user_followers(user_id, max_id=next_max_id)
        followers.extend(results.get('users', []))
        if len(followers) >= 600:       # get only first 600 or so
            break
        next_max_id = results.get('next_max_id')

    followers.sort(key=lambda x: x['pk'])
    # print list of user IDs
    print(json.dumps([u['pk'] for u in followers], indent=2))
    rank_token = Client.generate_uuid()
    has_more = True
    tag_results = []
    while has_more and rank_token and len(tag_results) < 60:
        results = api.tag_search(
            'cats', rank_token, exclude_list=[t['id'] for t in tag_results])
        tag_results.extend(results.get('results', []))
        has_more = results.get('has_more')
        rank_token = results.get('rank_token')

        # test = []
        # results = api.user_followers(me.id, me.rank_token)
        # test.extend(results.get('users', []))
        # next_max_id = results.get('next_max_id')
        # while next_max_id:
        #     results = api.user_followers(
        #         me.id, me.rank_token, max_id=next_max_id)
        #     test.extend(results.get('users', []))
        #     if len(test) >= 8000:       # get only first 600 or so
        #         break
        #     next_max_id = results.get('next_max_id')

        #     for user in following['users']:
        #         # grab followed user id
        #     followed_user_id = user['pk']
        #     # grab followed user full name
        #     followed_user_name = user['full_name']
        #     # append my id, followed user id, my full name, followed user full name
        #     follow_relationships.append(
        #         (me.get_id(), followed_user_id, me.get_full_name(), followed_user_name))
        #     # if you are following no one break
        #     if following.get('users') is not None:
        #         for users in followers['users']:
        #             follow_relationships.append(
        #                 (followed_user_id, users['pk'], followed_user_name, users['full_name']))

    print(json.dumps([t['name'] for t in tag_results], indent=2))


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/delete')
def delete():
    if 'user' in session:
        username = session['user']['username']
        db.users.delete_one({'username': username})
        session.clear()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host='127.0.0.1',
            port=os.environ.get('PORT', 8080))
