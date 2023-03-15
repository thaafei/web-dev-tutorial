from flask import Flask  #flask=module, Flask = class

app = Flask(__name__)  #creating object of Flask


@app.route("/")  #adding a route
def hello_world():  #when url / is active, show "hello"
  return "Hello"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
