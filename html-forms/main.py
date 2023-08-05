from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)

