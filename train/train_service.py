from flask import Flask, jsonify
app = Flask(__name__)


TRAINS = [
{"id": 1, "name": "Express A1", "from": "CityX", "to": "CityY", "duration": "3h"},
{"id": 2, "name": "Local B2", "from": "TownA", "to": "TownB", "duration": "1h 20m"},
]


@app.route('/trains', methods=['GET'])
def list_trains():
return jsonify(TRAINS)


@app.route('/trains/<int:train_id>', methods=['GET'])
def get_train(train_id):
for t in TRAINS:
if t['id'] == train_id:
return jsonify(t)
return ("", 404)


if __name__ == '__main__':
app.run(host='0.0.0.0', port=5002)
