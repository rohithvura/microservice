from flask import Flask, jsonify, request, abort
app = Flask(__name__)


# In-memory data
MOVIES = [
{"id": 1, "title": "The Great Heist", "genre": "Action", "duration": 125},
{"id": 2, "title": "Silent Moon", "genre": "Drama", "duration": 104},
]
next_id = 3


@app.route('/movies', methods=['GET'])
def list_movies():
return jsonify(MOVIES)


@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
for m in MOVIES:
if m['id'] == movie_id:
return jsonify(m)
abort(404)


@app.route('/movies', methods=['POST'])
def add_movie():
global next_id
data = request.get_json() or {}
if not data.get('title'):
return jsonify({"error": "title required"}), 400
movie = {
'id': next_id,
'title': data['title'],
'genre': data.get('genre','Unknown'),
'duration': data.get('duration', 120)
}
MOVIES.append(movie)
next_id += 1
return jsonify(movie), 201


if __name__ == '__main__':
app.run(host='0.0.0.0', port=5001)
