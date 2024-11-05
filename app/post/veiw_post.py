from flask import Blueprint, render_template
from utils import get_post_by_pk, get_comments_by_post_id

post_blueprint = Blueprint("post_blueprint", __name__)

@post_blueprint.route("/post/<int:x>")
def post_page(x):
    data = get_post_by_pk(x)
    data_comments = get_comments_by_post_id(x)
    count_comments_under_post = len(data_comments)
    return render_template('post.html', data=data,
                           comments=data_comments,
                           count_comments=count_comments_under_post)






