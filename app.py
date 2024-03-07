from flask import Flask, render_template, request, redirect, session, url_for, flash
from database import Auth, PetStore


app = Flask(__name__)

app.secret_key = "webjfgerjkgfjervjkgrjvgjgjvgrjgbhjgrjhg"

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        Auth().register(request)
        flash("Customer registered successfully")
        return redirect("/login")
    return render_template("auth/register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = Auth().authenticate(request)
        if email:
            session["user-token"] = email
            if request.args.get("next"):
                return redirect(request.args.get("next"))
            else:
                return redirect("/pet-store")
    return render_template('auth/login.html')


@app.route("/pet-store")
def pet_store():
    pets = PetStore().get_pets()
    return render_template("store.html", pets = pets)


@app.route('/cart/<int:pet_id>')
def cart(pet_id):
    customer = PetStore().buy_pet(pet_id)
    return render_template("cart.html", pet = PetStore().get_pet(pet_id), customer = customer)
