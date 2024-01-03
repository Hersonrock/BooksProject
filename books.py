from fastapi import FastAPI

app = FastAPI()

books ={
    "book1":{
        "title":"Title One",
        "author":"Author One",
             },
    "book2":{
        "title":"Title Two",
        "author":"Author Two",
             },
    "book3":{
        "title":"Title Three",
        "author":"Author Three",
             },
    "book4":{
        "title":"Title Four",
        "author":"Author Four",
             },
    "book5":{
        "title":"Title Five",
        "author":"Author Five",
             },
}

@app.get("/")
async def read_all_books():
    return books

@app.get("/book/{book_id}")
async def read_book(book_id:  int):
    response = books["book"+str(book_id)]
    return response