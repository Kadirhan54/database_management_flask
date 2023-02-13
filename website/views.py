from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Estate, Customer
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')  # Gets the note from the HTML

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            # providing the schema for the note
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)  # adding the note to the database
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # this function expects a JSON from the INDEX.js file
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/car', methods=['GET', 'POST'])
@login_required
def car():

    return render_template('car.html', user=current_user)

#### Fetch Spesific Data #####
# user = db.get_or_404(Customer, 2)
# print(user.name)


@views.route('/estate', methods=['GET', 'POST'])
@login_required
def estate():
    print(Customer.query.all())

    if request.method == 'POST':
        customer = request.form.get('customer')
        project = request.form.get('project')
        blok = request.form.get('blok')
        kapi = request.form.get('kapi')
        kat = request.form.get('kat')
        oda = request.form.get('oda')
        m2 = request.form.get('m2')
        m2_birim = request.form.get('m2-birim')
        alinan_pesinat = request.form.get('alinan-pesinat')
        alim_tarih = request.form.get('alim-tarih')
        satis_tarih = request.form.get('satis-tarih')
        satis_fiyat = request.form.get('satis-fiyat')
        taksit_sayisi = request.form.get('taksit-sayisi')
        taksit_tutari = request.form.get('taksit-tutari')
        yatirmci_verilecek = request.form.get('yatirimci-verilecek')
        saglam_gruba_kalan = request.form.get('saglam-gruba-kalan')

        try:
            customer_id = Customer.query.filter_by(name=customer).first().id

            new_estate = Estate(project=project, blok=blok, customer_id=customer_id,
                                kapi=kapi, kat=kat, oda=oda,
                                m2=m2, m2_birim=m2_birim, alim_tarih=alim_tarih, satis_tarih=satis_tarih,
                                alinan_pesinat=alinan_pesinat, satis_fiyat=satis_fiyat, taksit_sayisi=taksit_sayisi,
                                taksit_tutari=taksit_tutari, yatirimci_verilecek=yatirmci_verilecek,
                                saglam_gruba_kalan=saglam_gruba_kalan)

            db.session.add(new_estate)
            db.session.commit()
            flash('Estate added!', category='success')
        except:
            flash('Please Select User!', category='error')

    return render_template('estate.html', user=current_user, estates=Estate.query.all(), customers=Customer.query.all())


@views.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    if request.method == 'POST':
        name = request.form.get('name')
        customerID = request.form.get('customerID')
        phone = request.form.get('phone')
        tc = request.form.get('tc')

        try:
            new_customer = Customer(
                name=name, customer_id=customerID, phone=phone, tc=tc)
            db.session.add(new_customer)  # adding the note to the database
            db.session.commit()
            flash('User added!', category='success')

        except:
            flash('Error while Adding user!', category='error')

    # print(Customer.query.filter_by(name='Yaso').first().estates)

    return render_template('users.html', user=current_user, customers=Customer.query.all())


@views.route('/users/<name>', methods=['GET', 'POST'])
@login_required
def kado(name):

    print(Customer.query.filter_by(name=name).first().estates)

    return render_template('user.html', user=current_user, customer=Customer.query.filter_by(name=name).first())


@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    return render_template('admin.html', user=current_user)
