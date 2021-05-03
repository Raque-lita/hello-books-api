from app import db
from flask import Blueprint
from flask import request
from flask import jsonify
from .models.book import Book


books_bp = Blueprint("books", __name__, url_prefix="/books")

def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False

#gets single book, new route
@books_bp.route("/<book_id>", methods=["GET"])
def get_single_book(book_id):
    if not is_int(book_id):
        return {
            "message": f"ID {book_id} must be a number",
            "success": False
        }, 400

    book = Book.query.get(book_id)
    if book:
        return {
            "id" : book.id,
            "title" : book.title,
            "description": book.description
        }, 200
    return {
        "message": f"Book with id {book_id} was not found",
        "success": False,
    }, 404

@books_bp.route("", methods=["GET"], strict_slashes=False)
def books_index():
    books = Book.query.all()
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
            })
    return jsonify(books_response, 200)



@books_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return f"Book {new_book.title} successfully created", 201

# hello_world_bp = Blueprint('hello_world', __name__)

# @hello_world_bp.route('/hello-world', methods=["GET"])
# def get_hello_world():
#     my_response = "hello, world!"
#     return my_response

# @hello_world_bp.route('/hello-world/JSON', methods=["GET"])
# def hello_world_json():
#     return {
#         'name' : "Raqi!",
#         'message' : "Chello!",
#         'hobbies' : ['coding', 'riding', 'kindess'],
#     }, 200