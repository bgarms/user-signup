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

# ------ Validation Section ------

# ------ username validation ------

# Username cannot have spaces.
# Username cannot have empty fields. 
# This requirement has both client and server side validation. 
# **See edit.html for client side.**
# Username cannot be greater than 20 characters long or less that 3 characters.

    for character in username:
        if character ==" ":
            username_error = 'Username cannot have spaces'
            return render_template('edit.html', username_error=username_error)

    if username == '':
        username_error = 'Username cannot be blank'
        
    if len(username) > 20 or len(username) < 3:
        username_error = 'Not a valid username'
        return render_template('edit.html', username_error=username_error)

# ------ password validation ------

# Password cannot have spaces.
# Password cannot have empty fields.
# This requirement has both client and server side validation.
# **Se edit.html for client side.**
# Password cannot be greater than 20 characters long or less that 3 characters.

    password = request.form['password']
    password_error = ''

    verify_password = request.form['verify-password']
    verify_password_error = ''
    password_escape = cgi.escape(password, quote=True)
    
    for character in password:
        if character == " ":
            password_error = "Password cannot have spaces"
            return render_template('edit.html', password_error=password_error, username=username)

    if password == '':
        password_error = "Password cannot be blank"
        return render_template('edit.html', password_error=password_error)
        
    if len(password) > 20 or len(password) < 3:
        password_error = 'Not a valid password'.format(password)
        return render_template('edit.html', password_error=password_error)

# ------ verify validation ------

# Password and Re-typed Password must match.

    if verify_password != password:
        verify_password_error = 'Passwords do not match'
        return render_template('edit.html', verify_password_error=verify_password_error)

# Success without email

    welcome_message = '<h1>Welcome, ' + username + '</h1>'
    return welcome_message

# ------ email validation ------ 

# Email is optional.
# Email cannot have spaces.
# Email can have only one '@' sign.
# Email can have only one '.' 
# Email cannot be greater than 20 characters long or less that 3 characters.

    email = request.form['email']
    email_error = ''
    email_escape = cgi.escape(email, quote=True)

    for character in email:
        if character == " ":
            email_error = "Email cannot have spaces"
            return render_template('edit.html', email_error=email_error)

        if email.count('@') > 1:
            email_error = "Email can only contain one at sign"
            return render_template('edit.html', email_error=email_error)

        if email.count('.') > 1:
            email_error = "Email can only contain one '.'"
            return render_template('edit.html', email_error=email_error)

    if len(email) > 20 or len(email) < 3:
        password_error = 'Not a valid email'
        return render_template('edit.html', email_error=email_error)

# Success with email

        welcome_message = '<h1>Welcome, ' + username + '</h1>'
        return welcome_message
    

app.run()
