from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help='Name of the video  is required', required=True)
video_put_args.add_argument("likes", type=int, help='Likes of the video is required', required=True)
video_put_args.add_argument("views", type=int, help='Views of the video is required', required=True)

videos = {}


def video_id_dose_not_exist(video_id):
    if video_id not in videos:
        abort(404, message='Could not find video...')


def abort_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video id already exists...")


class Video(Resource):
    def get(self, video_id):
        video_id_dose_not_exist(video_id)
        return videos[video_id]


    def put(self, video_id):
        abort_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    
    def delete(self, video_id):
        video_id_dose_not_exist(video_id)
        del videos[video_id]
        return 'Video deleted', 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

