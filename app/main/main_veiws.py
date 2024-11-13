from flask import Blueprint, render_template, request
from utils import get_post_all, len_bookmarks

main_blueprint = Blueprint("main_blueprint", __name__)

@main_blueprint.route("/")
def main_page():
    data_for_posts = get_post_all()
    len_b = len_bookmarks()
    return render_template('index.html', data=data_for_posts, len=len_b)


@main_blueprint.route("/search")
def search_page():
    search_by = request.args['s']
    len_b = len_bookmarks()
    posts = [x for x in get_post_all() if search_by in x['content'].lower()]
    len_p = len(posts)
    return render_template('search.html ', data=posts, len_b=len_b, len_p=len_p)