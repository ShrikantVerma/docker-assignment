import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    return jsonify({'cpu': cpu, 'memory': memory})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

