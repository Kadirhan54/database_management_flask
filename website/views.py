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


@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    return render_template('admin.html', user=current_user)


@views.route('/estates', methods=['GET', 'POST'])
@login_required
def estates():

    if request.method == 'POST':
        name = request.form.get('customer')
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
            customer_id = Customer.query.filter_by(name=name).first().id

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

    return render_template('estates.html', user=current_user, estates=Estate.query.all(), customers=Customer.query.all())


@views.route('/estates/<int:id>', methods=['GET', 'POST'])
@login_required
def estate(id):

    return render_template('estate.html', user=current_user, estate=Estate.query.filter_by(id=id).first())


@views.route('/estates/add', methods=['POST'])
@login_required
def add_estate():
    pass


@views.route('/estates/edit', methods=['POST'])
@login_required
def edit_estate():
    if request.method == 'POST':
        try:
            estate_id = request.form.get('estate_id')
            name = request.form.get('customer')
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

            estate = Estate.query.filter_by(id=estate_id).first()

            estate.name = name
            estate.project = project
            estate.blok = blok
            estate.kapi = kapi
            estate.kat = kat
            estate.oda = oda
            estate.m2 = m2
            estate.m2_birim = m2_birim
            estate.alinan_pesinat = alinan_pesinat
            estate.alim_tarih = alim_tarih
            estate.satis_tarih = satis_tarih
            estate.satis_fiyat = satis_fiyat
            estate.taksit_sayisi = taksit_sayisi
            estate.taksit_tutari = taksit_tutari
            estate.yatirmci_verilecek = yatirmci_verilecek
            estate.saglam_gruba_kalan = saglam_gruba_kalan

            db.session.commit()
            flash('User Succesfully Edited!', category='success')

            return 'OK'

        except:
            flash('Error while Editing User!', category='error')

            return 'Fail'


@views.route('/estates/delete/<int:id>', methods=['POST'])
@login_required
def delete_estate(id):
    if request.method == "POST":
        try:
            estate = db.get_or_404(Estate, id)
            db.session.delete(estate)
            db.session.commit()
            flash('Estate Succesfully Deleted!', category='success')

            return 'OK'

        except:
            flash('Error while Deleting Estate!', category='error')

            return 'Fail'


@views.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    # print(Customer.query.filter_by(name='Yaso').first().estates)

    return render_template('users.html', user=current_user, customers=Customer.query.all())


@views.route('/users/<int:id>', methods=['GET', 'POST'])
@login_required
def user(id):
    # print(Customer.query.filter_by(name=name).first().estates)

    return render_template('user.html', user=current_user, customer=Customer.query.filter_by(id=id).first())


@views.route('/users/add', methods=['POST'])
@login_required
def user_add():
    if request.method == 'POST':
        name = request.form.get('name')
        customerid = request.form.get('customerid')
        phone = request.form.get('phone')
        tc = request.form.get('tc')

        try:
            new_customer = Customer(
                name=name, customer_id=customerid, phone=phone, tc=tc)
            db.session.add(new_customer)  # adding the note to the database
            db.session.commit()
            flash('User added!', category='success')
            return 'OK'

        except:
            flash('Error while Adding user!', category='error')
            return 'Fail'


@views.route('/users/edit/', methods=['POST'])
@login_required
def user_edit():
    if request.method == 'POST':
        try:
            user_id = request.form.get('user_id')
            name = request.form.get('name')
            customerid = request.form.get('customerid')
            phone = request.form.get('phone')
            tc = request.form.get('tc')

            customer = Customer.query.filter_by(id=user_id).first()

            customer.name = name
            customer.customer_id = customerid
            customer.phone = phone
            customer.tc = tc
            db.session.commit()
            flash('User Succesfully Edited!', category='success')

            return 'OK'

        except:
            flash('Error while Editing User!', category='error')

            return 'Fail'


@views.route('/users/delete/<int:id>', methods=['POST'])
@login_required
def user_delete(id):
    if request.method == "POST":
        try:
            customer = db.get_or_404(Customer, id)
            db.session.delete(customer)
            db.session.commit()
            flash('User Succesfully Deleted!', category='success')

            return 'OK'

        except:
            flash('Error while Deleting User!', category='error')

            return 'Fail'
