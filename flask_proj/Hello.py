from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/blog/<int:blog_id>')
def display_blog_id(blog_id):
    return f'Blog id {blog_id}'
#app.add_url_rule(rule='/hello', view_func=hello_world)

@app.route('/rev/<float:rev>')
def revision(rev):
    return f'revision {rev}'

@app.route('/<rev>')
def redirect_to_revision(rev):
    return redirect(url_for('revision', rev=rev))

@app.route('/login', methods=["GET", "POST"])
def login():
    user = ''
    if request.method == "POST":
        user = request.form["nm"]
    else:
        user = request.args.get("nm")
    return f"Welcome {user}"

if __name__ == '__main__':
    app.run(debug=True)
