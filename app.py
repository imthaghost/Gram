from flask import Flask, jsonify, redirect, url_for, render_template, request, session
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import WebApplicationClient

# set flask name
app = Flask(__name__)
client_id =  # instagram client id
client_secret =  # instagram client secret
authorization_uri = "https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=code"
token_url = 'https://api.instagram.com/oauth/access_token'
# merge root and index routes
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        return redirect(url_for('index'))


@app.route('/instagram', methods=['GET'])
def instagram():
    instagram_callback_url = request.base_url + \
        '/callback'  # call back url

    # ig = WebApplicationClient()
    instagram = OAuth2Session(
        client_id=client_id, redirect_uri=instagram_callback_url)
    authorization_url, state = instagram.authorization_url(
        authorization_uri.format(client_id, request.base_url + '/callback'))
    # State is used to prevent CSRF
    session['oauth_state'] = state
    return redirect(authorization_uri.format(client_id, request.base_url + '/callback'))


@app.route('/instagram/callback')
def instagram_callback():

    # set up to recieve code grant
    code = request.args.get("code")
    # grant_url = token_url % code = code
    instagram = OAuth2Session(
        client_id=client_id, redirect_uri=request.base_url, state=session['oauth_state'], scope=["public_content"])
    token = instagram.fetch_token(
        token_url, client_id=client_id, client_secret=client_secret, code=code, include_client_id=True)
    print(token)
    return redirect(url_for('index'))


@app.route('/login', methods=['GET'])
def login():
    pass


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8080)
