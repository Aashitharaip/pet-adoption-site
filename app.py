from flask import Flask, render_template, request, redirect, session, url_for, flash
from database import Auth, PetStore, login_required


app = Flask(__name__,template_folder='templates')

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
    user = Auth().get_user_details(session.get("user-token"))
    pets = PetStore().get_pets()
    return render_template("store.html", pets = pets, user = user)

@app.route('/cart/<int:pet_id>')
def cart(pet_id):
    customer = PetStore().buy_pet(pet_id)
    return render_template("cart.html", pet = PetStore().get_pet(pet_id), customer = customer)

# Route to update user details
@app.route('/update_user', methods=['GET', 'POST'])
@login_required
def update_user():
    auth = Auth()
    if request.method == "POST":
        auth.update_user_details(request)
    user_details = auth.get_user_details(session.get("user-token"))
    return render_template('update_user.html', user_details=user_details)

# Route to delete user account
@app.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    auth = Auth()
    if request.method == "POST":
        auth.delete_user_account()
        return redirect(url_for('index'))
    user_details = auth.get_user_details(session.get("user-token"))
    return render_template('delete-account.html', user_details=user_details)