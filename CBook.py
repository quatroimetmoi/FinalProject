class Book:
    def __init__(self, book_id, book_name, author, book_type, published_year, price, quantity):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.book_type = book_type
        self.published_year = published_year
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return(f"Mã sách: {self.book_id}, Tên sách: {self.book_name}, Tác giả: {self.author}")
