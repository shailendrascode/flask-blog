from flask import Flask, jsonify , render_template, request , session , redirect
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail
import datetime
from werkzeug.utils import secure_filename
import os
import math

app = Flask(__name__)
app.secret_key = 'super-secret-key'

# from app import apps
# from apps.members.models import db

#loading config json file
config = json.load(open('./config.json'))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
#username:root , password:''(blank)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/blog_database'

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME = config['mail_creds']['username'],
    MAIL_PASSWORD = config['mail_creds']['password']
)

#object for mail server
mail = Mail(app)

if(config['params']['local_server']):
    app.config['SQLALCHEMY_DATABASE_URI'] = config['params']['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = config['params']['local_uri']


db = SQLAlchemy(app)
# db.init_app(app)

social_handels = config['social_media']
post_metadata = config['posts_metadata']

class Contact(db.Model):
    # sno,name,email,phone_num,message
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(120), nullable=False)


class Posts(db.Model):
    # sno,name,email,phone_num,message
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(150), unique=True, nullable=False)
    date = db.Column(db.String(20), nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(120), nullable=False)
    subtitle = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)





@app.route('/')
def home():
    """Returns all the posts in the database but with the help of the pagination."""
    # Pagination Logic
    #First Page : prev =# next=page+1
    #Middle Page : prev = page-1 next = page+1
    #Last Page : prev = page-1 next=#

    posts = Posts.query.all()
    #[0:post_metadata['n_posts']]
    last = math.ceil(len(posts)/int(post_metadata['n_posts']))

    page = request.args.get('page')
    if not str(page).isnumeric():
        page=1
    page = int(page)
    posts = posts[(int(page-1))*post_metadata['n_posts']:(int(page-1))*post_metadata['n_posts']+post_metadata['n_posts']]

    if page==1:
        prev="#"
        next="/?page="+str(page+1)
    elif page==last:
        next="#"
        prev="/?page="+str(page-1)
    else:
        prev = "/?page="+str(page-1)
        next = "/page="+str(page+1)

    print(posts)
    for pos in posts:
        print(pos.author)
    return render_template('index.html', param=social_handels, posts=posts, prev=prev,next=next)


@app.route('/login', methods=['GET','POST'])
def login():
    """Login for the admin panel where the user can edit and delete posts."""

    if 'user' in session and session['user'] == config['admin_creds']['username'] :
        posts = Posts.query.all()
        return render_template('dashboard.html', param=social_handels, posts=posts)

    if request.method == 'POST':
        username = request.form.get('uname')
        passowrd = request.form.get('password')
        if username == config['admin_creds']['username'] and passowrd == config['admin_creds']['password']:
            #set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', param=social_handels, posts=posts)
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    """Log out from the admin panel."""
    session.pop('user', None)
    return redirect('/login')


@app.route('/about')
def about():
    """About the website."""
    return render_template('about.html', param=social_handels)

@app.route('/post')
@app.route('/post/<string:post_slug>' , methods=['GET'])
def post_route(post_slug=''):
    """return the post based on the slug"""
    if post_slug == '':
        post = Posts.query.filter_by(title='skills').first()
        return render_template('post.html', post=post, param=social_handels)
    post = Posts.query.filter_by(slug=post_slug).first()
    print(post.image_file)
    return render_template('post.html', param=social_handels,post=post)

@app.route('/contact', methods=['GET','POST'])
def contact():
    """Contact form for the users. """
    if(request.method=='POST'):
        # add entry to the database
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg= request.form.get('message')
        # making entry to the database
        # sno,name,email,phone_num,message
        print(name,email,phone,msg)
        entry = Contact(name=name,email=email,phone_num=phone,message=msg)
        db.session.add(entry)
        db.session.commit()

        # sending mail to the sender
        mail.send_message(
        'Hello from blog website',
        sender=config['mail_creds']['username'],
        recipients=[email],
        body="Congratulations you've succeeded!"+f" Your details are as follows : Name:{name} Phone:{phone} Email:{email}" )

    return render_template('contact.html', param=social_handels)


@app.route('/edit/<string:s_no>', methods=['POST','GET'])
def edit_post(s_no):
    """Edit a post and saving it to the database."""
    if 'user' in session and session['user'] == config['admin_creds']['username'] :
        if request.method == 'POST':
                box_title = request.form.get('title')
                subtitle = request.form.get('subtitle')
                slug = request.form.get('slug')
                content = request.form.get('content')
                img_file = request.form.get('img_file')
                date = datetime.datetime.now()
                author = request.form.get('author')

                if s_no == '0':
                    post = Posts(title=box_title,date=date,slug=slug,content=content,subtitle=subtitle,image_file=img_file, author=author)
                    db.session.add(post)
                    print(post)
                    db.session.commit()
                else:
                    post = Posts.query.filter_by(sno=s_no).first()
                    post.title = box_title
                    post.slug = slug
                    post.subtitle = subtitle
                    post.content = content
                    post.author = author
                    post.date = date
                    post.iamge_file = img_file
                    db.session.commit()
                    return redirect('/login')
                    
        post = Posts.query.filter_by(sno=s_no).first()
        return render_template('edit.html', param=social_handels, post=post)
    
    return render_template('login.html')

@app.route('/delete/<string:s_no>',methods=['GET'])
def delete(s_no):
    """Delete a post."""
    if 'user' in session and session['user'] == config['admin_creds']['username'] :
        Posts.query.filter(Posts.sno==s_no).delete()
        db.session.commit()
    return redirect('/login')
    







@app.route("/uploader",methods=['POST', 'GET'])
def uploader():
    """File Uploader"""
    if 'user' in session and session['user'] == config['admin_creds']['username'] :
        if request.method == 'POST':
            file = request.files['file1']
            file.save(os.path.join(config['paths']['uploaded_files'],secure_filename(file.filename)))
            return "Uploaded Successfully"










if __name__ == '__main__':
    app.run(debug=True, port=7777)
