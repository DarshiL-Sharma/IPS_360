from flask import Flask, render_template
from firebase_config import db



app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'Secret-key'

@app.route('/')
def landing_page():
    docs  = db.collection("users").stream()

    for doc in docs:
        print(doc.id, doc.to_dict())

    return render_template("landing_page.html")

if __name__ == "__main__":
    app.run(debug=True)