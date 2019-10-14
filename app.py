from flask import Flask, jsonify, redirect, url_for, render_template
import os

# find os version
version = os.sys.version

if version < python_verision_3:
    pass
else:
    pass


# set flask name
app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
