from flask import Blueprint, render_template
from utils import get_post_all

post_blueprint = Blueprint("post_blueprint", __name__)

@post_blueprint.route("/post")
def post_page():
    return render_template('post.html',)






