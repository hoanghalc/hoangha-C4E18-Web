from flask import *
import mlab
from models.service import Service

app = Flask(__name__)
#0. Connect to the Database
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    all_service = Service.objects()     
    return render_template('search.html', all_service=all_service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',
                            all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))   
    else:
        return('Service not found')    

@app.route('/new_service',methods=["GET","POST"])
def new_service():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form 

        new_service = Service(
            name = form['name'],
            yob = form['yob'],
            gender = form['gender'],
            height = form['height'],
            description = form['description']
        )
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/detail/<service_id>')
def detail(service_id):
    service_to_find = Service.objects.with_id(service_id)
    return render_template('service_id.html',service_to_find=service_to_find)

@app.route('/update/<service_id>', methods = ['GET','POST']) 
def update(service_id):
    if request.method == 'GET':
        service_to_update = Service.objects.with_id(service_id)
        return render_template ('update.html', service_to_update=service_to_update)
    elif request.method == 'POST':
        form = request.form
        service_to_update = Service.objects.with_id(service_id)
        service_to_update.update(set__name=form['name'],
                                    set__yob=form['yob'],
                                    set__gender=form['gender'],
                                    set__height=form['height'],
                                    set__phone=form['phone'],
                                    set__description=form['description'],
                                    set__measurement=form['measurement'],
                                )
        service_to_update.reload()
        return redirect(url_for('admin'))    

@app.route('/find/<gender>')
def find(gender):
    service_gender = Service.objects(gender=gender)
    return render_template('find.html',service_gender=service_gender)

if __name__ == '__main__':
  app.run(debug=True)
 