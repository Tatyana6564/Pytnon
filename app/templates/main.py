from flask import Flask, request, render_template

app = Flask (__name__)


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return f"Это профель пользователя с ID{user_id}"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form ['username']
        password = request.form ['password']
        return 'Вы вошли в систему'
    else:
        return render_template('login.html')

@app.route('/blog')
def blog():
    return 'Этот блог о увлечениях и о работе '

if __name__ == '__main__':
    app.run(debug=True)
