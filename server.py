from flask import Flask, request, render_template
from baby_names import find_names

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get("name", None)
    gender = request.args.get("gender", None)
    results = []
    if name is not None and name != '' and gender is not None:
      results = find_names(name, gender)
    return render_template("index.html", name = name, gender = gender, results = results)

if __name__ == '__main__':
  app.run(debug = True)