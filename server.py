import os
from flask import Flask, send_file, make_response
from flask_cors import CORS

APP = Flask(__name__)
CORS(APP)
MEDIA_PATH = '/Users/hongji/code/dora/video/tianjin/'

@APP.route('/<path:vid_name>')
def serve_video(vid_name):
    print(vid_name)
    vid_path = os.path.join(MEDIA_PATH, vid_name)

    # Set the appropriate headers to force inline video playback
    resp = make_response(send_file(vid_path, mimetype='video/mp4'))
    resp.headers['Content-Disposition'] = 'inline'  # Ensure the video is played inline
    resp.headers['Accept-Ranges'] = 'bytes'  # Enable byte-range requests for seeking
    return resp   


if __name__ == '__main__':
    APP.run()