import socket
import select
from flask import Flask
from flask import render_template
from flask import Flask, redirect, url_for
from flask import request
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from flask_login import UserMixin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'abcccde'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
data = "db.db"
login_manager = LoginManager()
login_manager.init_app(app)


class chat1(db.Model):
    name = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
    message = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'name:{}, message:{}, time:{}'.format(
            self.name,
            self.message,
            self.time
        )


class user(db.Model):
    username = db.Column(db.Text, primary_key=True,
                         nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)


# class User(UserMixin):
#     pass


@login_manager.user_loader
def user_loader(cls, username, password):
    user = cls.query.filter_by(username=username).first()
    username = request.form['username']

    if request.form['password'] == users[username]['password']:
        if user.check_password(password):
            return user
        else:
            return None
    return None


# def request_loader(request):
#     ab = request.form.get('user_id')
#     if ab not in users:
#         return
#     user = User()
#     user.id = ab
#     user.is_authenticated = request.form['password'] == users[ab]['password']
#     return user

# email = request.form['email']
#     if request.form['password'] == users[email]['password']:
#         #  實作User類別
#         user = User()
#         #  設置id就是email
#         user.id = email
#         #  這邊，透過login_user來記錄user_id，如下了解程式碼的login_user說明。
#         login_user(user)
#         #  登入成功，轉址
#         return redirect(url_for('protected'))


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/hello')
def hello():
    return 'Hi'


@app.route('/up')
def homeoo():
    return render_template('signup.html')


@app.route('/room', methods=['GET', 'POST'])
def homeroo():
    return render_template('chatroom.html')


@app.route('/log', methods=['POST'])
def homeottto():
    u = request.form['Username']
    p = request.form['Password']
    return redirect('/room')


@app.route('/sign', methods=['POST'])
def homeotttoo():
    n = request.form['Name']
    w = request.form['pwd']

    ch1 = user(username=n, password=w)
    try:
        db.session.add(ch1)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    return redirect('/')


@app.route('/demo')
def demo_url_for():
    return redirect(url_for('signup.html'))


if __name__ == '__main__':
    app.run(debug=True)

HEADER_LENGTH = 10
Host = "127.0.0.1"
# Server IP
Port = 8080


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((Host, Port))
server_socket.listen()
sockets_list = [server_socket]
clients = {}
# print(f'Listening for connections on {Host}:{Port}...')


def receive_message(client_socket):

    try:

        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:

        return False


# while True:

#     read_sockets, _, exception_sockets = select.select(
#         sockets_list, [], sockets_list)

#     for notified_socket in read_sockets:

#         if notified_socket == server_socket:
#             client_socket, client_address = server_socket.accept()
#             user = receive_message(client_socket)

#             if user is False:
#                 continue

#             sockets_list.append(client_socket)
#             clients[client_socket] = user
#             # print('Accepted new connection from {}:{}, username: {}'.format(
#             #     *client_address, user['data'].decode('utf-8')))

#         else:

#             message = receive_message(notified_socket)

#             if message is False:
#                 print('Closed connection from: {}'.format(
#                     clients[notified_socket]['data'].decode('utf-8')))
#                 sockets_list.remove(notified_socket)
#                 del clients[notified_socket]
#                 continue

#             user = clients[notified_socket]
#             # print(
#             #     f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

#             for client_socket in clients:

#                 if client_socket != notified_socket:
#                     client_socket.send(
#                         user['header'] + user['data'] + message['header'] + message['data'])

#     for notified_socket in exception_sockets:

#         sockets_list.remove(notified_socket)
#         del clients[notified_socket]


# 資料庫資料比對
# 訊息刷新網頁
