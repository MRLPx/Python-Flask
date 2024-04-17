from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/credit')
def credit():
    return render_template("credit.html")

@app.route('/vars/<nums>')
def vars(num):
    output = "You chose number {int(num)} which is 1 more than {int(num) - 1}"
    output += "<br> <a href='/'>Home</a>"
    return output


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

#● Add code to this project so that the input and button for the variable routing are on a separate web page that needs to be routed to from the main page. 
#● Add input validation to avoid crashes when letters are put into the number input
#when click submit send to different route page 