from flask import Flask, request, redirect, url_for, abort, make_response
import hashlib

app = Flask(__name__)
app.secret_key = '{Flag_H8Jm2FvQ5Nr9X4xZk0L6Pt3j}'  # Secret key for session handling

# Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "bulanpurnama1"
ADMIN_PASSWORD_HASH = hashlib.sha256(ADMIN_PASSWORD.encode()).hexdigest()

# Home page (no buttons or links)
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <title>Home</title>
    </head>
    <body class="container">
        <h1 class="mt-5">Welcome to my "secure" web app</h1>
        <p>Here is your flag for Challenge 01: {Flag_Xc8W9fJzKLq3h6TvNp2xRd9B} </p>
    </body>
    </html>
    """

# Dummy directories with configuration files
@app.route("/conf/")
@app.route("/install/setup.conf")
def config_files():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <title>Dummy Config</title>
    </head>
    <body class="container">
        <p>This is a dummy configuration file. No effect. Challenge 03: {Flag_Rc9XlYq8Gv2Mt5Jh7Np0Wz6Q}</p>
    </body>
    </html>
    """

# Admin page requiring X-Forwarded-For header to be 127.0.0.1
@app.route("/admin")
def admin():
    for header, value in request.headers.items():
        print(f"{header}: {value}")
    x_forwarded_for = request.headers.get("True-Client-IP")
    if x_forwarded_for == "127.0.0.1":
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <title>Admin Page</title>
        </head>
        <body class="container">
            <h1>Admin Page</h1>
            <p>Access granted. You successfully manipulate me. Your flag for Challenge 02: {Flag_Yr7bGfQ9Mn6TxH4vV3sZj8Pk}</p>
        </body>
        </html>
        """
    else:
        abort(403, description="403 Not Authorized")

# Login page for hardcoded admin credentials
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Check if the provided credentials match the hardcoded admin credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            response = make_response(redirect(url_for("remote_command_injection")))
            response.set_cookie("auth", ADMIN_PASSWORD_HASH)  # Set the hashed password as the cookie value
            return response
        else:
            return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
                <title>Login Failed</title>
            </head>
            <body class="container">
                <h1>Ooops. Invalid Credentials</h1>
                <p>Try again.</p>
            </body>
            </html>
            """
    
    # Render a simple login form
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <title>Login</title>
    </head>
    <body class="container">
        <h1 class="mt-5">Login</h1>
        <p>Challenge 04: {Flag_1Tm7VpQ3F9Lz8Kr5xHwJd6Nx}</p>
        <form method="post" class="form-group">
            <label for="username">Username:</label>
            <input type="text" name="username" id="username" class="form-control"><br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password" class="form-control"><br>
            <input type="submit" value="Login" class="btn btn-primary">
        </form>
    </body>
    </html>
    '''

# Remote command injection page
@app.route("/admin/{Flag_5Pw3NhQxT8Jl9Vb0Rk4sZmF2}", methods=["GET", "POST"])
def remote_command_injection():
    # Check if user has the correct auth cookie set
    if request.cookies.get("auth") == ADMIN_PASSWORD_HASH:
        result = ""
        if request.method == "POST":
            cmd = request.form.get("cmd")
            if cmd:
                import os
                command_string = "echo " + cmd
                result = os.popen(command_string).read()
        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <title>Remote Admin</title>
        </head>
        <body class="container">
            <h1 class="mt-5">Remote Admin: Simple is key</h1>
            <p>PS: You found Correct credential, your Challenge 05 flag is in the URL</p>
            <form method="post" class="form-group">
                <label for="cmd">Enter command:</label>
                <input type="text" name="cmd" id="cmd" class="form-control"><br>
                <input type="submit" value="Execute" class="btn btn-danger">
            </form>
            <p>Result:</p>
            <pre>{result}</pre>
        </body>
        </html>
        '''
    else:
        abort(403, description="403 Not Authorized")

if __name__ == "__main__":
    app.run(debug=True)
