from flask import Blueprint, current_app, request, jsonify
from .model import Book
from .serializer import BookSchema


bp_books = Blueprint('books', __name__, url_prefix='/api/books')


@bp_books.route('/show/<id>', methods=['GET'])
def show(id):
    bs = BookSchema()
    book = Book.query.filter(Book.id == id)
    return bs.jsonify(book.first()), 200


@bp_books.route('/showAll', methods=['GET'])
def showAll():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200


@bp_books.route('/insert', methods=['POST'])
def insert():
    bs = BookSchema()
    input = request.json
    book = bs.load(input)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    return bs.jsonify(book), 201


@bp_books.route('/update/<id>', methods=['PUT'])
def update(id):
    bs = BookSchema()
    input = request.json
    book = Book.query.filter(Book.id == id)
    book.update(input)
    current_app.db.session.commit()
    return bs.jsonify(book.first()), 200


@bp_books.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    book = Book.query.filter(Book.id == id)
    book.delete()
    current_app.db.session.commit()
    return jsonify({"message": "Book {} Deleted!".format(id)}), 200

