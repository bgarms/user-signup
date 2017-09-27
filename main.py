from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/")
def index():
    return render_template('edit.html')

@app.route("/signup", methods=['POST'])
def form_validate():
    username = request.form['username']
    username_error = ''
    username_escape = cgi.escape(username, quote=True)

# ------ Validation Section ------

# Redirects used to test functions. 
# Look for specific error message in URL when testing.

# Unable to get errors to return on re-rendered form page with feedback. 

# ------ username validation ------

# Username cannot have spaces.
# Username cannot have empty fields. 
# This requirement has both client and server side validation. 
# **See edit.html for client side.**
# Username cannot be greater than 20 characters long or less that 3 characters.

    for character in username:
        if character ==" ":
            username_error = 'Username cannot have spaces'
            return redirect("/?error=" + username_error)

    if username == '':
        username_error = 'Username cannot be blank'
        
    if len(username) > 20 or len(username) < 3:
        username_error = 'Not a valid username'
        return redirect("/?error=" + username_error)

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
            return redirect("/?error=" + password_error)

    if password == '':
        password_error = "Password cannot be blank"
        return redirect("/?error=" + password_error)
        
    if len(password) > 20 or len(password) < 3:
        password_error = 'Not a valid password'.format(password)
        return redirect("/?error=" + password_error)

# ------ verify validation ------

# Password and Re-typed Password must match.

    if verify_password != password:
        verify_password_error = 'Passwords do not match'
        return redirect("/?error=" + verify_password_error)

# ------ email validation ------ 

# Email is optional.
# Email cannot have spaces.
# Email can have only one '@' sign.
# Email can have only '.' 
# Email cannot be greater than 20 characters long or less that 3 characters.

    email = request.form['email']
    email_error = ''
    email_escape = cgi.escape(email, quote=True)

    for character in email:
        if character == " ":
            email_error = "Email cannot have spaces"
            return redirect("/?error=" + email_error)

        if email.count('@') > 1:
            email_error = "Email can only contain one at sign"
            return redirect("/?error=" + email_error)

        if email.count('.') > 1:
            email_error = "Email can only contain one '.'"
            return redirect("/?error=" + email_error)

    if len(email) > 20 or len(email) < 3:
        password_error = 'Not a valid email'
        return redirect("/?error=" + email_error)
        
# ------ success ------

    else:
        welcome_message = '<h1>Welcome, ' + username + '</h1>'
        return welcome_message
    

app.run()
