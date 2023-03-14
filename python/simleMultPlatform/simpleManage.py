from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['news']

@app.route('/api/news', methods=['GET'])
def get_news():
    news = db.news.find({})
    return jsonify(list(news))

@app.route('/api/news', methods=['POST'])
def create_news():
    data = request.json
    db.news.insert_one(data)
    return jsonify({'message': 'News created successfully.'})

@app.route('/api/news/<id>', methods=['PUT'])
def update_news(id):
    data = request.json
    db.news.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'News updated successfully.'})

@app.route('/api/news/<id>', methods=['DELETE'])
def delete_news(id):
    db.news.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'News deleted successfully.'})

if __name__ == '__main__':
    app.run(debug=True)