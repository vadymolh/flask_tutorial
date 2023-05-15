from flask import Flask, url_for, render_template
#WSGI

app = Flask(__name__) 


@app.route("/", methods=["GET", ])
def index():
    print (url_for("index"))
    return render_template("navbar.html", user="None")

@app.route("/", methods=["POST",])
def index_post():
    return "POST request on mainpage"

@app.route("/profile/<username>")
def profile(username):
    print (url_for("profile", username=username))
    return f"Hello {username}"

if __name__=="__main__":
    app.run(debug=True)