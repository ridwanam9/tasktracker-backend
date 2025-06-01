# def main():
#     print("Hello from tasktracker-backend!")


# if __name__ == "__main__":
#     main()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"