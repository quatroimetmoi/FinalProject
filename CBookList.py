import json
import os
from Models.CBook import Book

class BookList:
    def __init__(self):
        self.book_list = []
        self.file = "data/Book.json"
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.file):
            print(f"File {self.file} không tồn tại.")
            return
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.book_list = []
                for item in data:
                    book = Book(
                        book_id = item["book_id"],
                        book_name = item["book_name"],
                        author = item["author"],
                        book_type = item["type"],  # Trong JSON là 'type'
                        published_year = item["published_year"],
                        price = item["price"],  # Thêm price từ JSON
                        quantity = item["quantity"]
                    )
                    self.book_list.append(book)
            print(f"Đã tải thành công {len(self.book_list)} cuốn sách.")
        except Exception as e:
            print(f"Lỗi khi đọc file JSON: {e}")

    def save_books(self):
        data_to_save = []
        for b in self.book_list:
            data_to_save.append({
                "book_id": b.book_id,
                "book_name": b.book_name,
                "author": b.author,
                "type": b.book_type,
                "published_year": b.published_year,
                "price": b.price,
                "quantity": b.quantity
            })

        try:
            with open(self.file, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi khi lưu file: {e}")

    def get_all_book(self):
        self.load_books()
        return self.book_list

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
        return None

    def show_book(self):
        if not self.book_list:
            print("Danh sách sách trống.")
        else:
            for book in self.book_list:
                book.hien_thi()