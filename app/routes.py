from flask import Flask, json
from app.dto.members import *
from app.dto.albums import *
from app.dto.recordings import *
from app.dto.auditions import *
from app.dto.radioschedule import *

from app import app, db
from app.database.models import *


@app.route('/')
def hello_world():
    return 'Hello World!'


# Auditions
@app.route('/radioschedule')
def radio_schedule():
    auditions = Audition.query.order_by(Audition.id).all()
    radio_schedule_dto_new = RadioScheduleDTO(auditions)

    response = app.response_class(
        response=json.dumps(radio_schedule_dto_new, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


# Auditions
@app.route('/auditions')
def auditions():
    auditions = Audition.query.order_by(Audition.id).all()
    auditions_dto = AuditionsDTO(Audition.serialize_list(auditions))
    response = app.response_class(
        response=json.dumps(auditions_dto, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/auditions/<audition_id>')
def specific_audition(audition_id):
    audition_to_return = Audition.query.filter(Audition.id == audition_id).one()
    response = app.response_class(
        response=json.dumps(audition_to_return.serialize()),
        status=200,
        mimetype='application/json'
    )
    return response


# Recordings
@app.route('/recordings')
def recordings():
    recordings = Recording.query.order_by(Recording.id).all()
    recordings_dto = RecordingsDTO(Recording.serialize_list(recordings))
    response = app.response_class(
        response=json.dumps(recordings_dto, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


# Recordings
@app.route('/recordings/<recording_id>')
def specific_recording(recording_id):
    recording_to_return = Recording.query.filter(Recording.id == recording_id).one()
    response = app.response_class(
        response=json.dumps(recording_to_return.serialize()),
        status=200,
        mimetype='application/json'
    )
    return response


# Albums
@app.route('/albums')
def albums():
    albums = Album.query.order_by(Album.id).all()
    albums_resp = AlbumsDTO(Album.serialize_list(albums))
    response = app.response_class(
        response=json.dumps(albums_resp, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/albums/<album_id>')
def specific_album(album_id):
    album = Album.query.filter(Album.id == album_id).one()
    response = app.response_class(
        response=json.dumps(album.serialize()),
        status=200,
        mimetype='application/json'
    )

    return response


# Members
@app.route('/members')
def members():
    members = Member.query.order_by(Member.id).all()
    members_dto = MembersDTO(Member.serialize_list(members))
    response = app.response_class(
        response=json.dumps(members_dto, default=vars),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/members/<member_id>')
def specific_member(member_id):
    member_to_return = Member.query.filter(Member.id == member_id).one()

    response = app.response_class(
        response=json.dumps(member_to_return.serialize()),
        status=200,
        mimetype='application/json'
    )

    return response
