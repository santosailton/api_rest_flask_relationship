from flask import request
from app.__init__ import app, db
from app.model.model import *

routes = '''
    <p> http://localhost:5000/authors           </p>
    <p> http://localhost:5000/authors/1         </p>
    <p> http://localhost:5000/books             </p>
    <p> http://localhost:5000/authors/1/books/  </p>
'''


@app.route('/', methods=['GET'])
def index():
    return routes


@app.route('/authors/', methods=['GET', 'POST'])
def authors():
    if request.method == 'GET':
        authors = Author.query.all()
        if authors:
            return {'authors': [author.serialize() for author in authors]}
        else:
            return 'não encontrado', 404

    elif request.method == 'POST':
        data = request.json
        name = data.get('name')
        books = data.get('books')

        # Criação do autor
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()

        # Verifica se há livros para inserir
        if books:
            for book_data in books:
                title = book_data.get('title')
                book = Book(title=title, author_id=author.id)
                db.session.add(book)

            db.session.commit()

        return author.serialize(), 201


@app.route('/authors/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def author(id):
    author = Author.query.filter_by(id=id).first()
    if author:
        if request.method == 'GET':
            return author.serialize()

        elif request.method == 'PUT':
            name = request.json.get('author')
            author.name = name
            db.session.commit()
            return author.serialize()

        elif request.method == 'DELETE':
            books = Book.query.filter_by(author_id=id).all()
            for book in books:
                db.session.delete(book)

            db.session.delete(author)
            db.session.commit()
            return '', 204
    return 'não encontrado', 404


@app.route('/books/', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        books = Book.query.all()
        if books:
            return {'books': [book.serialize() for book in books]}, 201
        return 'não encontrado', 404

    elif request.method == 'POST':
        title = request.json.get('title')
        author_id = request.json.get('author_id')
        book = Book(title=title, author_id=author_id)
        db.session.add(book)
        db.session.commit()
        return book.serialize(), 201


@app.route('/authors/<int:id>/books/', methods=['GET', 'PUT', 'DELETE'])
def author_books(id):
    book = Book.query.get(id)

    if book:
        if request.method == 'GET':
            return book.serialize()
        elif request.method == 'PUT':
            title = request.json.get('title')
            book.title = title
            db.session.commit()
            return book.serialize()
        elif request.method == 'DELETE':
            db.session.delete(book)
            db.session.commit()
            return '', 204
    return 'não encontrado', 404


@app.route('/authors/<int:id_author>/books/<int:id_book>', methods=['GET', 'PUT', 'DELETE'])
def author_book(id_author, id_book):
    pass
