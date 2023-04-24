from flask import render_template, redirect, url_for, flash, request, session, jsonify, send_from_directory
from . import main
from .. import db
from ..models import User
from .forms import RegisterForm, LoginForm, PhotosForm
from flask_login import login_user, logout_user, login_required, current_user
import os
from werkzeug.utils import secure_filename

from pathlib import Path

from PIL import Image
from torchvision.utils import save_image
from .neural_transfer import showImage
import config

@main.route('/uploads/<name>')
def download_file(name):
    print(config.UPLOAD_FOLDER)
    return send_from_directory(config.UPLOAD_FOLDER, name)

@main.route("/")
def index():
    return redirect(url_for("main.home"))


@main.route("/home")
def home():
    return render_template("index.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("main.login"))
        login_user(user, remember=True)
        session["username"] = user.username
        return redirect(url_for("main.profile"))

    return render_template("login.html", form=form)


@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegisterForm()
    if (form.validate_on_submit()):
        username = form.username.data
        password = form.password.data
        # password = generate_password_hash(password)
        createUser(username, password)
        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)


@main.route("/logout", methods=["GET", "POST"])
def logout():
    current_user.authenticated = False
    logout_user()
    return render_template("index.html")


@main.route("/photo", methods=["GET", "POST"])
def photo():
    form = PhotosForm()

    if form.validate_on_submit() and request.method == 'POST':
        # Get the uploaded files from the request
        contentImg = form.contentImg.data
        styleImg = form.styleImg.data
        
        #initial save
        contentImg.save(os.path.join(config.UPLOAD_FOLDER, 'content.jpg'))
        styleImg.save(os.path.join(config.UPLOAD_FOLDER, 'style.jpg'))

        #resize files
        contentImg = Image.open(os.path.join(config.UPLOAD_FOLDER, 'content.jpg'))
        styleImg = Image.open(os.path.join(config.UPLOAD_FOLDER, 'style.jpg'))
        contentImg = contentImg.resize((600, 800))
        styleImg = styleImg.resize((600, 800))
        contentImg.save(os.path.join(config.UPLOAD_FOLDER, 'content.jpg'))
        styleImg.save(os.path.join(config.UPLOAD_FOLDER, 'style.jpg'))


        return redirect(url_for('main.result'))
    return render_template('photo.html', form=form)

@main.route("/result", methods=["GET", "POST"])
def result():

    #run neural transfer
    output_image = showImage(os.path.join(config.UPLOAD_FOLDER,'content.jpg'), os.path.join(config.UPLOAD_FOLDER,'style.jpg'))
    #resize image
    output_image = output_image.resize((600, 800))
    # save image
    output_image.save(os.path.join(config.UPLOAD_FOLDER, 'output.jpg'))

    return render_template('result.html', output_image=url_for('static', filename='output.jpg'), content_image=url_for('static', filename='content.jpg'), style_image=url_for('static', filename='style.jpg'))


@main.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    return redirect(url_for("main.profile_user", username=current_user.username, output_image=url_for('static', filename='output.jpg'), content_image=url_for('static', filename='content.jpg'), style_image=url_for('static', filename='style.jpg')))


@main.route("/<username>", methods=["GET", "POST"])
@login_required
def profile_user(username):
    user = db.one_or_404(
        db.select(User).filter_by(username=username),
        description=f"No user named '{username}'."
    )
    return render_template("profile.html", user=user, output_image=url_for('static', filename='output.jpg'), content_image=url_for('static', filename='content.jpg'), style_image=url_for('static', filename='style.jpg'))



@main.before_app_first_request
def create_tables():
    db.create_all()
    # new_user = User(username="admin", password="admin")
    # db.session.add(new_user)
    db.session.commit()


def createUser(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
