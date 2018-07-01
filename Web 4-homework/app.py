from flask import *
import mlab
from datetime import datetime
from models.service import Service
from models.user import User
from models.order import Order

app = Flask(__name__)
app.secret_key = "string"
#0. Connect to the Database
mlab.connect()


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
########################################

@app.route('/detail/<service_id>')
def detail(service_id):
    if  session.get('user_login'):
        service = Service.objects.with_id(service_id)
        return render_template('service_id.html',service=service)
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
        if  User.objects(username=username, password=password):
            session['user_login'] = True
            session['loggedin-user'] = "user"
            session['account'] = username
            session['password'] = password
            return redirect(url_for('search'))
        else:
            return "dinh hack cua bo may a"

@app.route('/logout')
def logout():
    if  session.get('user_login'):
        del session['user_login'] 
        del session['loggedin-user']
        del session['account']
        del session['password']
        return redirect(url_for('login'))
    else:
        return "error"
   

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
        return redirect(url_for('search'))

@app.route('/order_list')
def order_list():
    if  session.get('user_login'):
        all_order = Order.objects()
        return render_template('order.html', all_order=all_order)
    else:
        return redirect(url_for("login"))

@app.route('/order/<service_id>')
def order(service_id):
    if  session.get('user_login'):
        service = Service.objects.with_id(service_id)
        order = Order(service_name=service.name,
                         user_id = session['account'],
                         time=datetime.now(), 
                         is_accepted=False)           
        order.save()

        return redirect(url_for('search'))
    else:
        return redirect(url_for("login"))

@app.route('/accept/<order_id>')
def accept(order_id):
    if session.get('user_login'):
        order = Order.objects.with_id(order_id)
        order.update(set__is_accepted=True)
        all_order = Order.objects()
        return render_template('order.html', all_order=all_order)
    else:
        return redirect(url_for("login"))



if __name__ == '__main__':
  app.run(debug=True)
 