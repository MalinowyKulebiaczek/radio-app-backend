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
    response = app.response_class(
        response=json.dumps(radio_schedule_dto, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


# Auditions
@app.route('/auditions')
def auditions():
    response = app.response_class(
        response=json.dumps(auditions_dto, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/auditions/<audition_id>')
def specific_audition(audition_id):
    audition_to_return = None
    for audition in auditions_dto.members:
        if audition.id == int(audition_id):
            audition_to_return = audition

    response = app.response_class(
        response=json.dumps(audition_to_return, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


# Recordings
@app.route('/recordings')
def recordings():
    response = app.response_class(
        response=json.dumps(recordings_dto, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


# Recordings
@app.route('/recordings/<recording_id>')
def specific_recording(recording_id):
    recording_to_return = None
    for recording in recordings_dto.members:
        if recording.id == int(recording_id):
            recording_to_return = recording

    response = app.response_class(
        response=json.dumps(recording_to_return, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


# Albums
@app.route('/albums')
def albums():
    albums = Album.query.order_by(Album.id).all()
    # print(albums)
    albums_resp = AlbumsDTO(Album.serialize_list(albums))
    response = app.response_class(
        response=json.dumps(albums_resp, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/albums/<album_id>')
def specific_album(album_id):
    album_to_return = None
    for album in albums_dto.members:
        if album.id == int(album_id):
            album_to_return = album

    response = app.response_class(
        response=json.dumps(album_to_return, default=vars),
        status=200,
        mimetype='application/json'
    )

    return response


# Members
@app.route('/members')
def members():
    response = app.response_class(
        response=json.dumps(members_dto, default=vars),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/members/<member_id>')
def specific_member(member_id):
    member_to_return = None
    for member in members_dto.members:
        if member.id == int(member_id):
            member_to_return = member

    response = app.response_class(
        response=json.dumps(member_to_return, default=vars),
        status=200,
        mimetype='application/json'
    )

    return response
