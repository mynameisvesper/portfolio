import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'gkswngh14@gmail.com'
app.config['MAIL_PASSWORD'] = 'tgawdqsinbnjyrdp'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['DEBUG'] = True
app.config['TESTING'] = False
app.template_folder = 'templates'


# 앱 비번 tgawdqsinbnjyrdp

app.template_folder = os.path.abspath('templates')
print(os.getcwd())


mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message('New message from your website', sender='gkswngh14@gmail.com', recipients=['gkswngh14@gmail.com'])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'


    try:
        mail.send(msg)
        return 'success'
    except Exception as e:
         print(e)
         return str(e)

if __name__ == '__main__':
    app.run(debug=True)


