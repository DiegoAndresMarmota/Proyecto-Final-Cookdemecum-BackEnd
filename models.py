from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False, unique=False)
    blog = db.relationship("Blog")

    def __repr__(self) -> str:
        return "<User %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,
            "email": self.email,
            "password": self.password,
        }


"""class Blog(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    comentary = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    posts = db.relantioship("Post")

    def _repr_(self):
        return "<Product %r>" % self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "comentary": self.comentary,
            "user_id": self.user_id
        }
"""


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    post = db.Column(db.String(300), nullable=False)
    date = db.Column(db.Date(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #blog_id = db.Column(db.Interger, db.ForeignKey("blogs.id"), nullable=False)

    def _repr_(self):
        return "<Product %r>" % self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "comentary": self.post,
            "date": self.date,
            "user_id": self.user_id
            # "blog_id": self.blog_id
        }
