from app.database.models import *
from app import db


def insert_album(title, author, urlImg, timelineStart, timelineEnd, description):
    album = Album(title=title, author=author, urlImg=urlImg, timelineStart=timelineStart, timelineEnd=timelineEnd,
                  description=description)
    db.session.add(album)
    db.session.commit()
    return album


def insert_member(name, surname, urlImg, mainAudition):
    member = Member(name=name, surname=surname, urlImg=urlImg, mainAudition=mainAudition)
    db.session.add(member)
    db.session.commit()
    return member


def insert_recording(title, url, urlImg, description):
    recording = Recording(title=title, url=url, urlImg=urlImg, description=description)
    db.session.add(recording)
    db.session.commit()
    return recording


def insert_audition(title, urlImg, author, description, day, hourStart, hourEnd):
    audition = Audition(title=title, urlImg=urlImg, author=author, description=description, day=day,
                        hourStart=hourStart, hourEnd=hourEnd)
    db.session.add(audition)
    db.session.commit()
    return audition
