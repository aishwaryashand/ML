


#!usr/bin/python3
# main.py

from flask import Flask, render_template, Response
from camera import VideoCamera
#from motion import motionframe

app = Flask(__name__)

#web page
page="""
<html>
<head>
<title>Video Streaming Demonstration</title>
</head>
<body>
<h1>Video Streaming Demonstration</h1>
<iframe src="http://0.0.0.0:5000/video_feed" height=480 width=640></iframe>

</body>
</html>
"""
@app.route('/')

def index():
	return page
        #return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
	return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace;boundary=frame')

'''
@app.route('/video_frame')
def video_frame():
	return Response(gen(motionframe()),mimetype='multipart/x-mixed-replace;boundary=frame')
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

