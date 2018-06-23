from flask import Flask, render_template
from module.customer import Customer
import mlab



app = Flask(__name__)
#0. Connect to the Database
mlab.connect()

@app.route('/customer')
def home_page():
    all_customer = Customer.objects(gender = 1,
                                    contacted = False,
    )

    if len(all_customer) < 10:
        ten_customer = all_customer
    else:
        ten_customer = all_customer[0:10]

    return render_template('home_page.html', ten_customer = ten_customer)
        




if __name__ == '__main__':
  app.run(debug=True)
 
