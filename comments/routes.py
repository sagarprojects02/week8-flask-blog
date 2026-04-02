from flask import request, redirect, url_for
from app.comments import comments_bp
from app import db
from app.models import Comment

@comments_bp.route('/add/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    content = request.form.get('content')
    comment = Comment(content=content, post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.home'))
