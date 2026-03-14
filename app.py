from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Привет! Это мое приложение для упражнения 1.15, запущенное из Docker!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
