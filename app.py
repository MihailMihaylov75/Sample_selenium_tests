__author__ = 'Mihail Mihaylov'
import flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
print(flask.__version__)

posts = []


@app.route('/')
def homepage():
    """Render home page."""
    return render_template('home.html')


@app.route('/blog')
def blog_page():
    """Render blog page"""
    return render_template('blog.html', posts=posts)


@app.route('/post', methods=['GET', 'POST'])
def add_post():
    """Render post page"""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        global posts

        posts.append({
            'title': title,
            'content': content
        })

        return redirect(url_for('blog_page'))
    return render_template('new_post.html')


@app.route('/post/<string:title>')
def see_post(title):
    """Render posts"""
    global posts

    for post in posts:
        if post['title'] == title:
            return render_template('post.html', post=post)

    return render_template('post.html', post=None)


if __name__ == '__main__':
    app.run()
