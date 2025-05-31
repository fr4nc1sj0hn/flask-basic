import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)
import json
from collections import defaultdict

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/page2')
def page2():
   print('Request for index page received')
   return render_template('page2.html')

if __name__ == '__main__':
    app.run()
