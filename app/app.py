from flask import Flask, request, redirect, jsonify
import string
import random
import logging

app = Flask(__name__)

# Enable logging (important for CloudWatch later)
logging.basicConfig(level=logging.INFO)

url_map = {}

def generate_short():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET'])
def home():
    return '''
    <h2>URL Shortener</h2>
    <form action="/shorten" method="post">
        <input name="url" placeholder="Enter URL" required>
        <button type="submit">Shorten</button>
    </form>
    '''

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_code = generate_short()
    url_map[short_code] = original_url

    logging.info(f"Shortened URL: {original_url} -> {short_code}")
    logging.error("Test error log for CloudWatch")

    return f"Short URL: http://localhost:5000/{short_code}"

@app.route('/<short_code>')
def redirect_url(short_code):
    url = url_map.get(short_code)
    if url:
        return redirect(url)
    return "URL not found", 404

# Health check (important for Kubernetes)
@app.route('/health')
def health():
    return jsonify(status="OK"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
