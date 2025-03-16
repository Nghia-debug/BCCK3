import sqlite3
import getpass


conn = sqlite3.connect("exam_system.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER,
    title TEXT NOT NULL,
    questions TEXT NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES users(id)
)
""")
conn.commit()

class LoginSystem:
    def __init__(self):
        self.conn = sqlite3.connect("exam_system.db")
        self.cursor = self.conn.cursor()

    def Signup(self, username, password):
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login(self, username, password):
        self.cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()
        return user[0] if user else None

    def close(self):
        self.conn.close()


class Exam:
    def __init__(self, teacher_id):
        self.conn = sqlite3.connect("exam_system.db")
        self.cursor = self.conn.cursor()
        self.teacher_id = teacher_id

    def create_exam(self, title, questions):
        self.cursor.execute("INSERT INTO exams (teacher_id, title, questions) VALUES (?, ?, ?)",
                            (self.teacher_id, title, questions))
        self.conn.commit()
        print("Đề thi đã được tạo thành công!")

    def list_exams(self):
        self.cursor.execute("SELECT id, title, questions FROM exams WHERE teacher_id = ?", (self.teacher_id,))
        exams = self.cursor.fetchall()
        if exams:
            print("Danh sách đề thi của bạn:")
            for exam in exams:
                print(f"ID: {exam[0]} - Tiêu đề: {exam[1]}")
                question_list = exam[2].split("|")  
            for i, question in enumerate(question_list, 1):
                print(f"   {i}. {question}")
        else:
            print("Bạn chưa tạo đề thi nào.")

    def close(self):
        self.conn.close()


def main():
    login_system = LoginSystem()
    print("Xin chào!")
    while True:
        print("Chọn một thao tác:")
        print("1. Đăng nhập")
        print("2. Đăng ký")
        print("3. Thoát")
        choice = input("Nhập lựa chọn của bạn (1/2/3): ")

        if choice == '1':
            username = input("Nhập tên người dùng: ")
            password = getpass.getpass("Nhập mật khẩu: ")
            teacher_id = login_system.login(username, password)
            
            if teacher_id:
                print("Đăng nhập thành công!")
                exam_system = Exam(teacher_id)
                while True:
                    print("Chọn một thao tác:")
                    print("1. Tạo đề thi")
                    print("2. Xem danh sách đề thi")
                    print("3. Đăng xuất")
                    sub_choice = input("Nhập lựa chọn của bạn (1/2/3): ")
                    
                    if sub_choice == '1':
                        title = input("Nhập tiêu đề đề thi: ")
                        questions = input("Nhập danh sách câu hỏi (phân tách bằng dấu |): ")
                        exam_system.create_exam(title, questions)
                    elif sub_choice == '2':
                        exam_system.list_exams()
                    elif sub_choice == '3':
                        print("Đăng xuất thành công!")
                        break
                    else:
                        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
            else:
                print("Tên người dùng hoặc mật khẩu không chính xác.")
        elif choice == '2':
            username = input("Nhập tên người dùng: ")
            password = getpass.getpass("Nhập mật khẩu: ")
            if login_system.Signup(username, password):
                print("Đăng ký thành công!")
            else:
                print("Tên người dùng đã tồn tại. Vui lòng chọn tên khác.")
        elif choice == '3':
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
