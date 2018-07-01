from flask import *
import mlab
from models.video import Video
from models.user import User
from youtube_dl import YoutubeDL
app = Flask(__name__)
app.secret_key = "string"
mlab.connect()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html',videos=videos)

@app.route('/admin',methods=['GET','POST'])
def admin():
    if 'loggedin' in session:
        if request.method == 'GET':
            videos = Video.objects()
            return render_template('admin.html',videos=videos)
        elif request.method == 'POST':
            form = request.form
            link = form['link']
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download = False)

            title = data['title']
            thumbnail = data['thumbnail']
            youtube_id = data['id']
            views = data['view_count']

            new_video = Video(title=title,
                                thumbnail=thumbnail,
                                youtube_id=youtube_id,
                                views=views,
                                link=link
                            )
            new_video.save()            
            return redirect(url_for('admin'))
    else:
        return "Yeu cau dang nhap!!!"
@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    if session['loggedin'] == True:
        return render_template('detail.html',youtube_id=youtube_id)
    else:
        return redirect(url_for('login'))


@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        #query from database
        if username == "admin" and password == "admin":
            session ['loggedin'] == True
            return redirect(url_for('admin'))
        else:
            return "dinh hack cua bo may a"

@app.route('/logout')
def logout():
    del session['loggedin']
    return redirect(url_for('index'))

@app.route('/sign_in', methods=["GET","POST"])
def sign_in():
    if request.method =="GET":
        return render_template('sign_in.html')
    elif request.method =="POST":
        form = request.form
        new_user = User(username = form['username'],
                        password = form['password'],
                        email = form['email'],
                        fullname =  form['fullname']
        )
        new_user.save()
        return redirect(url_for('index'))


if __name__ == '__main__':
  app.run( debug=True)
 