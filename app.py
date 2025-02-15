from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get_client_ip():
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return f"Client IP: {client_ip}", 200

if __name__ == '__main__':
    # Run on 0.0.0.0 so it is accessible from outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)
