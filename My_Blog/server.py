import requests
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/guess/<name>')
def guess(name):
    gender_url=f"https://api.genderize.io?name={name}"
    gender_response=requests.get(gender_url)
    gender_data=gender_response.json()
    gender=gender_data["gender"]
    age_url=f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html",person_name=name,gender=gender,age=age)
@app.route('/blog')
def get_blog():
    blog_url="https://api.npoint.io/84d5ef3b32626cad7d74"
    response=requests.get(blog_url)
    all_posts=response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
