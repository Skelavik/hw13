from flask import Blueprint, render_template, request
import utils

main_blueprint = Blueprint("main_blueprint", __name__)

@main_blueprint.route("/")
def main_page():
    data_for_posts = utils.get_post_all()
    print("Hello")
    return render_template('index.html', data=data_for_posts)


