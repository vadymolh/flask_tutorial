from flask import Flask, url_for, render_template
from data_sanity.data_interface import get_all_posts
#WSGI

app = Flask(__name__) 


@app.route("/", methods=["GET", ])
def index():
    context = get_all_posts()
    print (url_for("index"))
    return render_template("navbar.html", 
                           title = context[0]['title'],
                           text = context[0]['text'],
                           user = "anonimous" )

@app.route("/", methods=["POST",])
def index_post():
    return "POST request on mainpage"

@app.route("/profile/<username>")
def profile(username):
    print (url_for("profile", username=username))
    return f"Hello {username}"

if __name__=="__main__":
    app.run(debug=True)