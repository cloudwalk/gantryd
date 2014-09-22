#!/usr/bin/env python

from flask import Flask, request
from werkzeug.utils import secure_filename
import subprocess
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/etc/gantryd/config_files'

@app.route('/config', methods=['POST'])
def upload_config():
    config_file = request.files.get('config')
    if config_file is not None:
        filename = secure_filename(config_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        config_file.save(filepath)

        return 'Uploaded file %s.' % filename
    return 'Please pass the configuration file in your form.'

@app.route('/list', methods=['GET'])
def list():
    config_file = request.args.get('config')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], config_file)
    project_name = request.args.get('project')

    r = subprocess.check_output(['./gantry.py', filepath, 'list', project_name])
    return r

@app.route('/start', methods=['GET'])
def start():
    config_file = request.args.get('config')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], config_file)
    project_name = request.args.get('project')

    r = subprocess.check_output(['./gantry.py', filepath, 'start', project_name])
    return r

@app.route('/stop', methods=['GET'])
def stop():
    config_file = request.args.get('config')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], config_file)
    project_name = request.args.get('project')

    r = subprocess.check_output(['./gantry.py', filepath, 'stop', project_name])
    return r

@app.route('/kill', methods=['GET'])
def kill():
    config_file = request.args.get('config')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], config_file)
    project_name = request.args.get('project')

    r = subprocess.check_output(['./gantry.py', filepath, 'kill', project_name])
    return r

@app.route('/update', methods=['GET'])
def update():
    config_file = request.args.get('config')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], config_file)
    project_name = request.args.get('project')

    r = subprocess.check_output(['./gantry.py', filepath, 'update', project_name])
    return r

if __name__ == '__main__':
    try:
        os.makedirs(app.config['UPLOAD_FOLDER'])
    except OSError:
        pass

    app.run(host='0.0.0.0', port=5000, debug=True)