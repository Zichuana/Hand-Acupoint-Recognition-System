import os
from flask import Flask, jsonify, request, render_template, session, g, redirect, url_for
from datetime import datetime, timedelta
from PIL import Image
import io
import random
import json
from uils import hand_predict
import hashlib
from models import User, FadeBack
from extension import db
from flask_cors import CORS
from flask_login import UserMixin, LoginManager, login_required, logout_user, login_user, current_user

app = Flask(__name__, static_url_path='/')

# 自动重载模板文件
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 设置静态文件缓存过期时间
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

CORS(app)  # 解决跨域问题
basedir = os.path.abspath(os.path.dirname(__file__))  # 使用绝对路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = 'secret_key'  # 设置表单交互密钥
# 1、实例化登录管理对象
login_manager = LoginManager()

# 参数配置
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'

login_manager.init_app(app)  # 初始化应用


@login_manager.user_loader
def user_loader(user_id: str):
    if User.query.filter_by(id=int(user_id)) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        mail = request.form.get('mail')
        user = User.query.filter(User.username == username).all()
        if len(user) > 0:
            return render_template('register.html', msg='用户名已存在！')
        user1 = User.query.filter(User.mail == mail).all()
        if len(user1) > 0:
            return render_template('register.html', msg='邮箱已存在！')
        if password == repassword:
            # 注册用户
            user = User()
            user.username = username
            # 加密
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.mail = mail
            # 添加并提交
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 关键  select * from user where username='xxxx';
        new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # 查询
        user_list = User.query.filter_by(username=username)

        for u in user_list:
            # 此时的u表示的就是用户对象
            if u.password == new_password:
                login_user(u)
                return redirect(url_for('index'))
        else:
            return render_template('login.html', msg='用户名或者密码有误！')

    return render_template('login.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('root'))


@app.route('/feedback', methods=["POST", "GET"])
@login_required
def feedback():
    if request.method == 'POST':
        try:
            id = current_user.get_id()
            user = User.query.filter(User.id == id).all()
            for u in user:
                username = u.username
                mail = u.mail
                text = request.form.get('text')
                fk = FadeBack()
                fk.username = username
                fk.mail = mail
                fk.text = text
                db.session.add(fk)
                db.session.commit()
                return render_template('feedback.html', msg='提交成功！')
        except Exception as e:
            return render_template('feedback.html', msg='提交失败！-' + str(e))
    return render_template('feedback.html')


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    User.init_db()


@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("root.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
@login_required
def predict():
    info = {}
    try:
        image = request.files["file"]
        img_bytes = image.read()
        image = Image.open(io.BytesIO(img_bytes))
        width = image.size[0]  # 获取宽度
        height = image.size[1]  # 获取高度
        image = image.resize((int(width * 0.5), int(height * 0.5)), Image.ANTIALIAS)
        nowTime = datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum = random.randint(0, 99)
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        image_path = 'data/' + uniqueNum
        image.save('./static/' + image_path + '.jpg')
        result_path = hand_predict(image_path)
        info['result'] = result_path
        print(result_path)
    except Exception as e:
        info['err'] = str(e)
    return info  # json格式传至前端


@app.route("/fore1", methods=["GET", "POST"])
@login_required
def fore1():
    return render_template("fore1.html")


@app.route("/fore2", methods=["GET", "POST"])
@login_required
def fore2():
    return render_template("fore2.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2222)
