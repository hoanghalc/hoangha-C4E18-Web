from flask import Flask, render_template
import mlab
from models.service import Service

app = Flask(__name__)
#0. Connect to the Database
mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender=gender,
                                 yob__lte=1998,
                                address__iexact="ha noi")
    return render_template('search.html', all_service=all_service)

if __name__ == '__main__':
  app.run(debug=True)
 