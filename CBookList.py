from Models.CBook import Book
from JsonFactory import *

class BookList:
    def __init__(self):
        self.book_list = []
        self.file = "data/Book.json"
        self.load_books()

    def load_books(self):
        data = JsonFileFactory.read_data(self.file)
        self.book_list = []

        for item in data:
            book = Book(
                item["book_id"],
                item["book_name"],
                item["author"],
                item["type"],
                item["published_year"],
                item["price"],
                item["quantity"]
            )
            self.book_list.append(book)

    def get_all_books(self):
        return self.book_list

    def save_books(self):
        data = [book.to_dict() for book in self.book_list]
        JsonFileFactory.write_data(self.file, data)

    def add_book(self, book):
        for b in self.book_list:
             if str(b.book_id) == str(book.book_id): # Tránh 1 =! 001
                return "Sách đã tồn tại!"
        self.book_list.append(book)
        self.save_books()  # Lưu lại sau khi thêm
        return "Thêm sách thành công!"

    def delete_book(self, book_id):
        original_len = len(self.book_list)
        self.book_list = [b for b in self.book_list if str(b.book_id) != str(book_id)]
        if len(self.book_list) < original_len:
            self.save_books()  # Lưu lại sau khi xóa
            return "Xóa thành công."
        return "Không tìm thấy ID để xóa."

    def find_book_by_id (self, book_id):
        for book in self.book_list:
            if str(book.book_id) == str(book_id):
                return book
        return None

    def find_book_by_name (self, book_name):
        search_name = book_name.lower()
        for book in self.book_list:
            if book.book_name.lower() == search_name:
                return book
        return None

    def search_book(self, keyword):
        keyword = keyword.lower()
        result = []
        for book in self.book_list:
            if (keyword in book.book_name.lower() or
                keyword in book.author.lower() or
                keyword in book.book_type.lower()):
                 result.append(book) # Đưa vào danh sách result
        return result

    def show_book(self):
        if not self.book_list:
            print("Danh sách sách trống.")
        else:
            for book in self.book_list:
                book.hien_thi()
