from flask import render_template, request, Response, jsonify
from models import db, Shorte
import urlencoder as urlenc
from shorte import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/g')
def generate():
    assert 'long_url' in request.args
    long_url = request.args['long_url']
    entry = Shorte.query.filter_by(long_url=long_url).first()
    if entry == None:
        entry = Shorte(long_url)
        db.session.add(entry)
        db.session.flush()
        db.session.refresh(entry)
        short_url = urlenc.encode_url(entry.id)
        entry.short_url = short_url
        db.session.commit()
    full_short = 'http://rw4.us/' + entry.short_url
    response = jsonify(id=entry.id,
                       short_url=full_short,
                       clicks=entry.hits)
    return response
