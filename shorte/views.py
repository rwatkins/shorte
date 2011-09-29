from flask import render_template, request, Response, jsonify, redirect
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
    response = jsonify(short_url=full_short, clicks=entry.clicks)
    return response

@app.route('/all')
def view_all():
    all_entries = Shorte.query.all()
    return render_template('view_all.html', entries=all_entries)

@app.route('/<short_url>')
def redirect_short(short_url):
    entry = Shorte.query.filter_by(short_url=short_url).first()
    if entry == None:
        abort(404)
    else:
        entry.clicks += 1
        db.session.commit()
        return redirect(entry.long_url)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', url=request.url)
