from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
   
    posts = [
        { "title" : "Tho con coc",
            "author"  : "Ha Hoang",
            "content" : "Hello",
            "gender": 1
        },
        {'title': "tho con ech",
        'author': 'van la Ha',
        'content': "kia chu la chu ech con",
        "gender": 0
        },
    ]
    return render_template("index.html",post=posts)

@app.route('/hello')
def say_hello():
    return "Hello C4E 18"

@app.route('/xin_chao/<name>/<age>')
def say_hi(name, age):
    return "Hi {0}, you're {1} years old".format(name,age)

@app.route("/sum/<int:a>/<int:b>")
def sum(a, b):
    return str(a + b) 

if __name__ == '__main__':
  app.run(debug=True)
 