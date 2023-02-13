from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Estate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    project = db.Column(db.String(100))
    blok = db.Column(db.String(20))
    kapi = db.Column(db.Integer)
    kat = db.Column(db.Integer)
    oda = db.Column(db.String(20))
    m2 = db.Column(db.Integer)
    m2_birim = db.Column(db.Integer)
    alim_tarih = db.Column(db.Integer)
    satis_tarih = db.Column(db.Integer)
    alinan_pesinat = db.Column(db.Integer)
    satis_fiyat = db.Column(db.Integer)
    taksit_sayisi = db.Column(db.Integer)
    taksit_tutari = db.Column(db.Integer)
    yatirimci_verilecek = db.Column(db.Integer)
    saglam_gruba_kalan = db.Column(db.Integer)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.relationship('Note')

    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estates = db.relationship('Estate')
    # cars = db.relationship('Cars')

    name = db.Column(db.String(150))
    customer_id =  db.Column(db.Integer)
    phone =  db.Column(db.Integer)
    tc =  db.Column(db.Integer)
