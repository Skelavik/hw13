from flask import Flask
import utils


from main.main_veiws import main_blueprint
from post.veiw_post import post_blueprint

app = Flask(__name__)


app.register_blueprint(post_blueprint)
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run()

