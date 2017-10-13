from flask import Flask, request, render_template
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('user_signupform.html') 


@app.route('/sign_up', methods=['POST'])


    
def sign_up():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    username_boolean = True
    password_boolean = True
    email_boolean = True
    verify_boolean = True 



    if ' ' in username or len(username) < 3 or len(username) > 20:
            username_error = 'Invalid Username 3-20 Characters' 
            username = ''
            username_boolean = False
    
    if ' ' in password or len(password) <3 or len(password) > 20:
            password_error = 'Password 3-20 Length'
            password = ''
            password_boolean = False

    if verify != password :
        verify_error = 'Passwords must match'
        verify = ''
        verify_boolean = False  

    if len(email) <3 or len(email) > 20 or '@' in email or '.' in email or ' ' in email and email != "":
                email_error = 'Not valid email 3-20 Characters'  
                email = ''
                email_boolean = False   

    if username_boolean or password_boolean or email_boolean or verify_boolean == True:
        
        return render_template('user_signupform.html', username = username, password = password,
                            verify = verify, email = email, username_error = username_error, 
                            password_error = password_error, verify_error = verify_error, email_error = email_error)
    else:

        
        return render_template('welcome_gretting.html', username = username, password = password, 
                            verify = verify, email = email, username_error = username_error, 
                            password_error = password_error, verify_error = verify_error, email_error = email_error)
   
   
    #if not password_error and not username_error and not verify_error and not email_error:
    
app.run()