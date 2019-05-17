from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'root'}
    listing = [
        {
            'header': {'group': 'Folders'},
            'item': 'New Folder'
        },
        {
            'header': {'group': 'Text Files'},
            'item': 'My_file.txt'
        },
        {
            'header': {'group': 'Pictures'},
            'item': 'Photo.jpg'
        }
    ]
    return render_template('index.html', title='File Manager', user=user, posts=listing)
