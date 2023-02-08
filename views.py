from flask import request, jsonify
from main import app
from model import *

routes = '''
    <p> http://localhost:5000/authors       </p>
    <p> http://localhost:5000/authors/1    </p>
    <p> http://localhost:5000/books        </p>
    <p> http://localhost:5000/books/1      </p>
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
        return 'não encontrado', 404

    elif request.method == 'POST':
        name = request.json.get('name')
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
        return author.serialize(), 201


@app.route('/authors/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def author(id):
    author = Author.query.filter_by(id=id).first()
    if author:
        if request.method == 'GET':
            return author.serialize()

        elif request.method == 'PUT':
            name = request.json.get('name')
            author.name = name
            db.session.commit()
            return author.serialize()

        elif request.method == 'DELETE':
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


@app.route('/books/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def book(id):
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
