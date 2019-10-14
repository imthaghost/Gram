from flask import Flask, url_for, redirect, render_template, session
from urllib.request import urlopen
from app import app

# merge root and index routes
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    if request.method == 'GET':
        render_template('home.html')

    if request.method == 'POST':
        redirect(url_for('index'))
