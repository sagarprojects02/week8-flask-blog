from flask import render_template
from app.main import main_bp
from app.models import Post

@main_bp.route('/')
def home():
    posts = Post.query.all()
    return render_template('main/home.html', posts=posts)
