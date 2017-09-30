from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/")
def index():

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''


    return render_template('edit.html', username_error=username_error, password_error=password_error,
        verify_password_error=verify_password_error, email_error=email_error)

@app.route("/signup", methods=['POST'])
def form_validate():

    username = request.form['username']
    username_error = ''
    username_escape = cgi.escape(username, quote=True)
    username_input = request.form['username']
    password = request.form['password']
    password_error = ''
    verify_password = request.form['verify-password']
    verify_password_error = ''
    password_escape = cgi.escape(password, quote=True)
    email_input = request.form['email']
    email = request.form['email']
    email_error = ''
    email_escape = cgi.escape(email, quote=True)

    welcome_message = '<h1>Welcome, ' + username + '</h1>'


    for character in username:
        if character ==" ":
            username_error = 'Username cannot have spaces'
            username_input = ''

    if username == '':
        username_error = 'Username cannot be blank'
        username_input = ''
        
    if len(username) > 20 or len(username) < 3:
        username_error = 'Not a valid username'
        username_input = ''
    
    for character in password:
        if character == " ":
            password_error = "Password cannot have spaces"

    if password == '':
        password_error = "Password cannot be blank"
        
    if len(password) > 20 or len(password) < 3:
        password_error = 'Not a valid password'

    if verify_password != password:
        verify_password_error = 'Passwords do not match'

    for character in email:
        if character == " ":
            email_error = "Email cannot have spaces"
            email_input = ''

    if email.count('@') > 1:
        email_error = "Email can only contain one at sign"
        email_input = ''

    if email.count('.') > 1:
        email_error = "Email can only contain one '.'"
        email_input = ''

    if len(email) > 20 or len(email) < 3:
        email_error = 'Not a valid email'
        email_input = ''

    if len(email) == 0:
        email_error = ''

    if username_error != '' and password_error != '' and verify_password_error != '' and email_error!= '':
        return render_template('edit.html', username_error=username_error, password_error=password_error,
            verify_password_error=verify_password_error, email_error=email_error)

    if username_error != '' and password_error != '' and email_error!= '':
        return render_template('edit.html', username_error=username_error, password_error=password_error,
            email_error=email_error)

    if username_error != '' and verify_password_error != '' and email_error!= '':
        return render_template('edit.html', username_error=username_error,
            verify_password_error=verify_password_error, email_error=email_error)

    if username_error != '' and password_error != '' and verify_password_error != '':
        return render_template('edit.html', username_error=username_error, password_error=password_error, 
            verify_password_error=verify_password_error, email_input=email_input)
    
    if username_error != '' and email_error!= '':
        return render_template('edit.html', username_error=username_error, email_error=email_error)

    if username_error != '' and password_error != '':
        return render_template('edit.html', username_error=username_error, password_error=password_error, 
            email_input=email_input)

    if username_error != '':
        return render_template('edit.html', username_error=username_error, email_input=email_input)

#--------------------------------------------------------------------------------------------------------
    
    if password_error != '' and verify_password_error != '' and email_error!= '':
        return render_template('edit.html', username_input=username_input, password_error=password_error,
            verify_password_error=verify_password_error, email_error=email_error)   

    if password_error != '' and verify_password_error != '':
        return render_template('edit.html', username_input=username_input, password_error=password_error,
            verify_password_error=verify_password_error, email_input=email_input)  

    if password_error != '' and email_error!= '':
        return render_template('edit.html', username_input=username_input, password_error=password_error, 
            email_error=email_error) 

    if password_error != '':
        return render_template('edit.html', username_input=username_input, password_error=password_error, 
            email_input=email_input) 
    
#---------------------------------------------------------------------------------------------------------

    if email_error != '':
        return render_template('edit.html', username_input=username_input, email_error=email_error)


    else:
        return welcome_message




# Success with email
    

app.run()