from flask import Flask, render_template, request, redirect, url_for, session, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import markdown
import os

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(45), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    long_text = db.Column(db.Text)
    slug = db.Column(db.String(100), unique=True)

with app.app_context():
    db.create_all()

ADMIN_PASSWORD_HASH = generate_password_hash("Navlis_11")

@app.before_request
def track_user():
    if request.path.startswith('/static') or request.path == '/favicon.ico':
        return
    ip = request.remote_addr
    user = User.query.filter_by(ip=ip).first()
    if not user:
        user = User(ip=ip, clicks=0)
        db.session.add(user)
    user.clicks += 1
    db.session.commit()

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/About')
def about():
    return render_template('About/index.html')

@app.route('/Contact')
def contact():
    return render_template('Contact/index.html')

@app.route('/Projects')
def projects_page():
    projects = Project.query.all()
    return render_template('Projects/index.html', projects=projects)

@app.route('/projects/<slug>')
def project_detail(slug):
    project = Project.query.filter_by(slug=slug).first_or_404()
    content = markdown.markdown(project.long_text)
    return render_template('project_detail.html', project=project, content=content)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form.get('password')
        if check_password_hash(ADMIN_PASSWORD_HASH, password):
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
    return '''
        <form method="post">
            Password: <input type="password" name="password">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin'))
    users = User.query.all()
    projects = Project.query.all()
    total_users = User.query.count()
    total_clicks = db.session.query(db.func.sum(User.clicks)).scalar() or 0
    return render_template('admin.html', users=users, projects=projects, total_users=total_users, total_clicks=total_clicks)

@app.route('/admin/add_project', methods=['POST'])
def add_project():
    if not session.get('admin_logged_in'):
        abort(403)
    title = request.form.get('title')
    short_description = request.form.get('short_description')
    image_url = request.form.get('image_url')
    long_text = request.form.get('long_text')
    slug = title.lower().replace(' ', '-')
    
    new_project = Project(title=title, short_description=short_description, image_url=image_url, long_text=long_text, slug=slug)
    db.session.add(new_project)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
