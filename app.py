from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    client_ip = request.remote_addr
    return f"Your IP address is: {client_ip}"

if __name__ == '__main__':
    # Run on 0.0.0.0 so it is accessible from outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)
