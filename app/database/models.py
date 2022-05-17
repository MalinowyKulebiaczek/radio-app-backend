from app import db

from sqlalchemy.inspection import inspect


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class Album(db.Model, Serializer):
    __tablename__ = "Albums"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    urlImg = db.Column(db.String(150))
    timelineStart = db.Column(db.String(20))
    timelineEnd = db.Column(db.String(20))
    description = db.Column(db.String(7000))

    def __repr__(self):
        return f"Albums('{self.id}','{self.title}','{self.author}')"


class Member(db.Model, Serializer):
    __tablename__ = "Members"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    urlImg = db.Column(db.String(150))
    mainAudition = db.Column(db.String(50))

    def __repr__(self):
        return f"Members('{self.id}','{self.name}','{self.surname}')"


class Recording(db.Model, Serializer):
    __tablename__ = "Recordings"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    url = db.Column(db.String(150))
    description = db.Column(db.String(7000))

    def __repr__(self):
        return f"Recordings('{self.id}','{self.title}')"


class Audition(db.Model, Serializer):
    __tablename__ = "Auditions"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    urlImg = db.Column(db.String(150))
    author = db.Column(db.String(50))
    description = db.Column(db.String(7000))
    day = db.Column(db.String(50))
    hourStart = db.Column(db.String(50))

    def __repr__(self):
        return f"Auditions('{self.id}','{self.title}','{self.author}')"
