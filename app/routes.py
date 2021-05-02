from app import db
from flask import Blueprint
from flask import request
from .models.book import Book


books_bp = Blueprint("books", __name__, url_prefix="/books")


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