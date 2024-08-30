from flask import Flask, render_template

app = Flask(__name__)

# Sample data for blog posts
posts = [
    {
        'id': 1,
        'title': 'First Blog Post',
        'content': 'This is the content of the first blog post.',
        'author': 'Akshay Ravi',
        'date': '2024-08-30'
    },
    {
        'id': 2,
        'title': 'Second Blog Post',
        'content': 'This is the content of the second blog post.',
        'author': 'Akshay Ravi',
        'date': '2024-08-29'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True, port=1336)
