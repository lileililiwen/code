from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

# 创建Flask应用
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建数据库实例
db = SQLAlchemy(app)

# 创建数据库迁移实例
migrate = Migrate(app, db)

# 创建登录管理实例
login_manager = LoginManager()
login_manager.init_app(app)

# 定义用户模型
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# 定义登录回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 配置首页路由
@app.route('/')
def index():
    return 'Hello World!'

# 配置登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

# 配置登出路由
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

# 配置管理员路由，需要登录才能访问
@app.route('/admin')
@login_required
def admin():
    return 'Admin Page'

# 启动Flask应用
if __name__ == '__main__':
    app.run(debug=True)