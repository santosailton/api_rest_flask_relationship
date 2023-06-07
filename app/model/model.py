from app.__init__ import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'author': self.name,
            'books': self.list_books()
        }

    def list_books(self):
        list_book = []
        [list_book.append(book.serialize()) for book in self.books]

        return list_book


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author_id': self.author_id
        }


db.create_all()
