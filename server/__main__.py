import sys
sys.path.append('.')

from server.webapp import flaskapp, db, TEMPLATES
from server.models import *
from server.routes import *

default_books = [
    ("The Hobbit", "JRR Tolkien", True),
    ("The Fellowship of the Ring", "JRR Tolkien", True),
    ("The Eye of the World", "Robert Jordan", False),
    ("A Game of Thrones", "George R. R. Martin", True),
    ("The Way of Kings", "Brandon Sanderson", False)
]


if __name__ == "__main__":
    for bookname, bookauthor, hasread in default_books:
        if not Book.query.filter_by(name=bookname).first():
            book = Book(name=bookname, author=bookauthor, read=hasread)
            db.session.add(book)
            db.session.commit()

    db.create_all()
    flaskapp.run('0.0.0.0', debug=True)
