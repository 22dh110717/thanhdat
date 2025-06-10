from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask API is running on Render!'

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from Render Cloud API!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
