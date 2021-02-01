# coding=utf-8
import os
import pathlib
import uuid

# Flask utils
from flask import Flask, request, render_template, send_file
from gevent.pywsgi import WSGIServer

import core


# Define a flask app
PORT = 5000
HOST = '172.16.68.107'
app = Flask(__name__, static_folder='pic')


def gen_uuid_hex():
    return uuid.uuid4().hex


def face_merge(src_fn, face_fn):
    ofn = f'results/{gen_uuid_hex()}.jpg'
    core.face_merge(src_img=src_fn,
                    dst_img=face_fn,
                    out_img=ofn,
                    face_area=None,
                    alpha=0.75,
                    blur_detail_x=15,
                    blur_detail_y=10,
                    mat_multiple=0.95)
    return ofn


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/files/', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return {'errors': 'upload file?'}, 400
    basepath = os.path.dirname(__file__)
    relative_path = f'uploads/{gen_uuid_hex()}{pathlib.Path(file.filename).suffix}'
    fn = os.path.join(basepath, relative_path)
    file.save(fn)
    return {'filename': relative_path, 'url': f'http://{HOST}:{PORT}/{relative_path}'}


@app.route('/uploads/<path:path>')
def uploads_file(path):
    basepath = os.path.dirname(__file__)
    fn = os.path.join(basepath, 'uploads', path)
    return send_file(fn)


@app.route('/results/<path:path>')
def results_file(path):
    basepath = os.path.dirname(__file__)
    fn = os.path.join(basepath, 'results', path)
    return send_file(fn)


@app.route('/face-swap/', methods=['POST'])
def face_swap():
    # Get the file from post request
    data = request.json
    src_image = data.get('src_image')
    face_image = data.get('face_image')
    if not src_image or not face_image:
        return {'errors': 'src_image and face_image?'}, 400

    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    src_fn = os.path.join(basepath, src_image)
    face_fn = os.path.join(basepath, face_image)

    # Make prediction
    ofn = face_merge(src_fn, face_fn)

    # Process your result for human
    result = {
        'code': 200,
        'msg': 'success',
        'image_url': f'http://{HOST}:{PORT}/{ofn}',
    }
    return result


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    # Serve the app with gevent
    # http_server = WSGIServer(('', PORT), app)
    # http_server.serve_forever()
