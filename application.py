from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/sendtime")
def sendtime():
    return render_template('sendtime.html')

@app.route("/view")
def view():
    return render_template('viewresponse.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)