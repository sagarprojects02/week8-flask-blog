from flask import render_template, redirect, url_for
from app.posts import posts_bp
from app.posts.forms import PostForm
from app import db
from app.models import Post

@posts_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    user_id=1)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('posts/create_post.html', form=form)
