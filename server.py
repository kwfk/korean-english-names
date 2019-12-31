from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get("name", "World")
    gender = request.args.get("gender", "Male")
    return render_template("index.html", name = name, gender = gender)
    # return f'Hello, {escape(name)}!'

if __name__ == '__main__':
  app.run(debug = True)