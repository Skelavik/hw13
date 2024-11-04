from flask import Blueprint, render_template, request
from utils import get_post_all, len_bookmarks

main_blueprint = Blueprint("main_blueprint", __name__)

@main_blueprint.route("/")
def main_page():
    data_for_posts = get_post_all()
    len_b = len_bookmarks()
    return render_template('index.html', data=data_for_posts, len=len_b)


