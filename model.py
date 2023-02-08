from main import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'author': self.name,
            'books': self.list_books(self.id)
        }

    def list_books(self, id):
        books = Book.query.filter_by(author_id=id)
        book_return = {}
        list_book = []
        for book in books:
            book_return["id"] = book.id
            book_return["title"] = book.title
            book_return["author_id"] = book.author_id
            list_book.append(Book.serialize(book))

        return list_book


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author_id': self.author_id
        }


db.create_all()
