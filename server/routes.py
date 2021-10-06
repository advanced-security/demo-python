
from flask import request, render_template, make_response

from server.webapp import flaskapp, db
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        result = db.engine.execute(
            "SELECT * FROM Book WHERE name LIKE '%" + name + "%'"
        )
        books = [row for row in result]
        if len(books) == 0:
            return make_response(f"Search Result not found: {name}", 404)
    elif author:
        result = db.engine.execute(
            "SELECT * FROM Book WHERE author LIKE '%" + author + "%'"
        )
        books = [row for row in result]
        if len(books) == 0:
            return make_response(f"Search Result not found: {author}", 404)
    else:
        books = Book.query.all()
    
    return render_template('books.html', books=books)
