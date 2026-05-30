from fastapi import FastAPI, Body

app = FastAPI()


Books = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'economics'},
    {'title': 'Title Four', 'author': 'Author Three', 'category': 'economics'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'history'},
    {'title': 'Title Six', 'author': 'Author Six', 'category': 'hindi'},
    {'title': 'Title Seven', 'author': 'Author Seven', 'category': 'english'},
    {'title': 'Title Eight', 'author': 'Author Eight', 'category': 'math'},
    {'title': 'Title Nine', 'author': 'Author Eight', 'category': 'math'},
    {'title': 'Title Ten', 'author': 'Author Eight', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return Books


@app.get("/books/title/{book_title}")
async def read_book_by_title(book_title: str):
    read_all_books = []
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            read_all_books.append(book)
    return read_all_books
    

@app.get("/books/category/")
async def read_book_by_category(category: str):
    read_all_books_by_category = []
    for book in Books:
        if book.get('category').casefold() == category.casefold():
            read_all_books_by_category.append(book)
    return read_all_books_by_category


@app.get("/books/{author}/")
async def read_book_by_author_and_category(author: str, category: str):
    read_all_books_by_author_and_category = []
    for book in Books:
        if book.get('author').casefold() == author.casefold() and book.get('category').casefold() == category.casefold():
            read_all_books_by_author_and_category.append(book)
    return read_all_books_by_author_and_category


@app.post("/books/create_book")
async def create_book(book=Body()):
    return Books.append(book)


@app.put("/books/update/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == updated_book.get('title').casefold():
            Books[i] = updated_book
        

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == book_title.casefold():
            Books.pop(i)
            break

