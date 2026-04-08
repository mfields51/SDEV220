from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Title: {self.book_name}, Author: {self.author}, Publisher: {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'


# Get all books
@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {
            'Title': book.book_name, 
            'Author': book.author, 
            'Publisher': book.publisher
        }
        output.append(book_data) 
    return {"books": output}

# Get specific book
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({
            'Title': book.book_name, 
            'Author': book.author, 
            'Publisher': book.publisher
        })

# Add book
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# Delete book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}, 404
    
    db.session.delete(book)
    db.session.commit()
    return {"message": "Deleted"}

if __name__ == "__main__":
    app.run(debug=True)