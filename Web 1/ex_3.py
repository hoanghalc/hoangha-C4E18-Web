from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def info_user(username):
    users = {
        "quy" : {
            "name" : "Đinh Công Quý",
            "age" : 20,
            "hobbies" : "Hentai"
        },
        "tuananh" : {
            "name" : "Nguyễn Tuấn Anh",
            "age" : 22,
            "hobbies" : "Gãi đít"
        },
        "duy" : {
            "name" : "Vũ Khánh Duy",
            "age" : 21,
            "hobbies" : "Ăn cứt mũi"
        }
    }
    return render_template("ex_3.html", users = users, username = username)

if __name__ == '__main__':
  app.run(port= 8000, debug=True)


 