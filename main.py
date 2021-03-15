from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/bio')
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')