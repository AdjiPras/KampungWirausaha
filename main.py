from flask import Flask, session, request, jsonify, flash, render_template, json, redirect, url_for, make_response
from datetime import date, datetime 
from models import MModel
from time import sleep
# from flask_mysqldb import MySQL
import datetime 
import config2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test-test'

model = MModel()
html_source = ''

# Home
@app.route('/')
def home():
	if 'data_user' in session:
		data_user = session['data_user']
		return render_template('index_diskusi.html', data_user=data_user)
	return render_template('form_login.html')

# login   
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if model.authenticate(username, password):
			data_user = model.getUserForSession(username)
			session['data_user'] = data_user
			return redirect(url_for('home'))
		msg = 'Username/Password salah.'
		return render_template('form_login.html', msg=msg)
	return render_template('form_login.html')
	
# SIGN UP
@app.route('/insert_signup', methods=['GET', 'POST'])
def insert_signup():
    if request.method == 'POST':
        id_freelancer = request.form['id_freelancer']
        username = request.form['username']
        password = request.form['password']
        nama = request.form['nama']
        tipe_akses = 2
        data_signup = (id_freelancer, username, password, nama, tipe_akses)
        model.insertSignUp(data_signup)
        return redirect(url_for('freelancer'))
    else:
        return render_template('form_signup.html')

# Logout  
@app.route('/logout')
def logout():
  session.pop('data_user', '')
  return redirect(url_for('home'))

# SOP
@app.route('/sop')
def sop():
	if 'data_user' in session:
		data_user = session['data_user']
		return render_template('sop.html', data_user=data_user)
	return render_template('form_login.html')
  
# TEAM
@app.route('/team')
def team():
	if 'data_user' in session:
		data_user = session['data_user']
		return render_template('team.html', data_user=data_user)
	return render_template('form_login.html')

# ================================ KATEGORI ==============================
# SEMUA
@app.route('/beranda')
def beranda():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_semua = [] 
        container_semua = model.selectSemua()
        return render_template('semua.html', container_semua=container_semua, data_user=data_user)
    return render_template('form_login.html')

# MAKANAN
@app.route('/makanan')
def makanan():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_makanan = [] 
        container_makanan = model.selectMakanan()
        return render_template('makanan.html', container_makanan=container_makanan, data_user=data_user)
    return render_template('form_login.html')

# MINUMAN
@app.route('/minuman')
def minuman():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_minuman = [] 
        container_minuman = model.selectMinuman()
        return render_template('minuman.html', container_minuman=container_minuman, data_user=data_user)
    return render_template('form_login.html')

# PAKAIAN
@app.route('/pakaian')
def pakaian():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_pakaian = [] 
        container_pakaian = model.selectPakaian()
        return render_template('pakaian.html', container_pakaian=container_pakaian, data_user=data_user)
    return render_template('form_login.html')

# DESAIN
@app.route('/desain')
def desain():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_desain = [] 
        container_desain = model.selectDesain()
        return render_template('desain.html', container_desain=container_desain, data_user=data_user)
    return render_template('form_login.html')

# MANUFAKTUR
@app.route('/manufaktur')
def manufaktur():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_manufaktur = [] 
        container_manufaktur = model.selectManufaktur()
        return render_template('manufaktur.html', container_manufaktur=container_manufaktur, data_user=data_user)
    return render_template('form_login.html')

# TEKNOLOGI
@app.route('/teknologi')
def teknologi():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_teknologi = [] 
        container_teknologi = model.selectTeknologi()
        return render_template('teknologi.html', container_teknologi=container_teknologi, data_user=data_user)
    return render_template('form_login.html')

# PARIWISATA
@app.route('/pariwisata')
def pariwisata():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_pariwisata = [] 
        container_pariwisata = model.selectPariwisata()
        return render_template('pariwisata.html', container_pariwisata=container_pariwisata, data_user=data_user)
    return render_template('form_login.html')

# TRANSPORT
@app.route('/transport')
def transport():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_transport = [] 
        container_transport = model.selectTransport()
        return render_template('transport.html', container_transport=container_transport, data_user=data_user)
    return render_template('form_login.html')

# ONLINE SHOP
@app.route('/onlineshop')
def onlineshop():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_onlineshop = [] 
        container_onlineshop = model.selectOnlineShop()
        return render_template('onlineshop.html', container_onlineshop=container_onlineshop, data_user=data_user)
    return render_template('form_login.html')

# PERIKLANAN
@app.route('/periklanan')
def periklanan():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_periklanan = [] 
        container_periklanan = model.selectPeriklanan()
        return render_template('periklanan.html', container_periklanan=container_periklanan, data_user=data_user)
    return render_template('form_login.html')

# ARTIKEL SEO
@app.route('/artikelseo')
def artikelseo():
    if 'data_user' in session:
        data_user = session['data_user']
        username = data_user[1]
        container_artikel_seo = [] 
        container_artikel_seo = model.selectArtikelSeo()
        return render_template('artikel_seo.html', container_artikel_seo=container_artikel_seo, data_user=data_user)
    return render_template('form_login.html')
    
# ========================== PERTANYAAN ==========================
@app.route('/pertanyaan')
def pertanyaan():
    if 'data_user' in session:
        data_user = session['data_user']
        data_user = data_user[1]
        container_pertanyaan = [] 
        container_pertanyaan = model.selectPertanyaan()
        return render_template('pertanyaan.html', container_pertanyaan=container_pertanyaan, data_user=data_user)
    return render_template('form_login.html')

@app.route('/insert_pertanyaan', methods=['GET', 'POST'])
def insert_pertanyaan():
	if 'data_user' in session:
		if request.method == 'POST':
			no = request.form['no']
			username = request.form['username']
			kategori = request.form['kategori']
			pertanyaan = request.form['pertanyaan']
			penjawab = '-'
			jawaban = '-'
			tanggal_jawab = datetime.datetime.now()
			ranking = '-'
			keterangan = '-'
			data_p = (no, username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan)
			model.insertPertanyaan(data_p)
			return redirect(url_for('beranda'))
		else:
			data_user = session['data_user']
			return render_template('insert_pertanyaan.html', data_user=data_user)
	return render_template('form_login.html')

@app.route('/answer_pr', methods=['GET', 'POST'])
def answer_pr():
    if 'data_user' in session:
        no = request.form['no']
        username = request.form['username']
        kategori = request.form['kategori']
        pertanyaan = request.form['pertanyaan']
        penjawab = request.form['penjawab']
        jawaban = request.form['jawaban']
        tanggal_jawab = datetime.datetime.now()
        ranking = "-"
        keterangan = "-"
        data_pr = (username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan, no)
        model.updatePertanyaan(data_pr)
        return redirect(url_for('beranda'))
    return render_template('form_login.html')

@app.route('/answer/<no>')
def answer(no):
    if 'data_user' in session:
        data_pr = model.getPertanyaanbyNo(no)
        data_user = session['data_user']
        return render_template('edit_pertanyaan.html', data_pr=data_pr, data_user=data_user)
    return render_template('form_login.html') 

# KOREKSI
@app.route('/koreksi_pr', methods=['GET', 'POST'])
def koreksi_pr():
    if 'data_user' in session:
        no = request.form['no']
        username = request.form['username']
        kategori = request.form['kategori']
        pertanyaan = request.form['pertanyaan']
        penjawab = request.form['penjawab']
        jawaban = request.form['jawaban']
        tanggal_jawab = datetime.datetime.now()
        ranking = request.form['ranking']
        keterangan = request.form['keterangan']
        data_pr = (username, kategori, pertanyaan, penjawab, jawaban, tanggal_jawab, ranking, keterangan, no)
        model.koreksiPertanyaan(data_pr)
        return redirect(url_for('beranda'))
    return render_template('form_login.html')

@app.route('/koreksi_pertanyaan/<no>')
def koreksi_pertanyaan(no):
    if 'data_user' in session:
        data_pr = model.getPertanyaanbyNo(no)
        data_user = session['data_user']
        return render_template('koreksi.html', data_pr=data_pr, data_user=data_user)
    return render_template('form_login.html') 

@app.route('/delete_pertanyaan/<no>')
def delete_pertanyaan(no):
    if 'data_user' in session:
        model.deletePertanyaan(no)
        return redirect(url_for('beranda'))
    return render_template('form_login.html')

# ================================ PENGGUNA ==============================
@app.route('/freelancer')
def freelancer():
    if 'data_user' in session:
        data_user = session['data_user']
        data_user = data_user[1]
        container_freelancer = [] 
        container_freelancer = model.selectFreelancer()
        return render_template('freelancer.html', container_freelancer=container_freelancer, data_user=data_user)
    return render_template('form_login.html')
    
@app.route('/insert_freelancer', methods=['GET', 'POST'])
def insert_freelancer():
	if 'data_user' in session:
		if request.method == 'POST':
			id_freelancer = request.form['id_freelancer']
			username = request.form['username']
			password = request.form['password']
			nama = request.form['nama']
			tipe_akses = request.form['tipe_akses']
			data_f = (id_freelancer, username, password, nama, tipe_akses)
			model.insertFreelancer(data_f)
			return redirect(url_for('freelancer'))
		else:
			data_user = session['data_user']
			return render_template('insert_freelancer.html', data_user=data_user)
	return render_template('form_login.html')

@app.route('/update_fr', methods=['GET', 'POST'])
def update_fr():
    if 'data_user' in session:
        id_freelancer = request.form['id_freelancer']
        username = request.form['username']
        password = request.form['password']
        nama = request.form['nama']
        tipe_akses = request.form['tipe_akses']
        data_fr = (username, password, nama, tipe_akses, id_freelancer)
        model.updateFreelancer(data_fr)
        return redirect(url_for('freelancer'))
    return render_template('form_login.html')

@app.route('/update_freelancer/<id_freelancer>')
def update_freelancer(id_freelancer):
	if 'data_user' in session:
		data_fr = model.getFreelancerbyNo(id_freelancer)
		data_user = session['data_user']
		return render_template('edit_freelancer.html', data_fr=data_fr, data_user=data_user)
	return redirect(url_for('login')) 

@app.route('/delete_freelancer/<id_freelancer>')
def delete_freelancer(id_freelancer):
    if 'data_user' in session:
        model.deleteFreelancer(id_freelancer)
        return redirect(url_for('freelancer'))
    return render_template('form_login.html')

# ================================ LAPORAN ==============================
@app.route('/laporan')
def laporan():
    if 'data_user' in session:
        container_lp = []
        container_lp = model.selectLaporan()
        data_user = session['data_user']
        return render_template('laporan.html', container_lp=container_lp, data_user=data_user)
    return render_template('form_login.html')
    
@app.route('/insert_laporan', methods=['GET', 'POST'])
def insert_laporan():
    if 'data_user' in session:
        if request.method == 'POST':
            no = request.form['no']
            username = request.form['username']
            text_laporan = request.form['text_laporan']
            tanggal_lapor = datetime.datetime.now()
            status = '-'
            data_lp = (no, username, text_laporan, tanggal_lapor, status)
            model.insertLaporan(data_lp)
            return redirect(url_for('laporan'))
        else:
            data_user = session['data_user']
            return render_template('insert_laporan.html', data_user=data_user)
    return render_template('form_login.html')

# proses edit / update data laporan.
@app.route('/update_lp', methods=['GET', 'POST'])
def update_lp():
    if 'data_user' in session:
        no = request.form['no']
        username = request.form['username']
        text_laporan = request.form['text_laporan']
        tanggal_lapor = datetime.datetime.now()
        status = request.form['status']
        data_lp = (username, text_laporan, tanggal_lapor, status, no)
        model.updateLaporan(data_lp)
        return redirect(url_for('laporan'))
    return render_template('form_login.html')

# edit / update data laporan.
@app.route('/update_laporan/<no>')
def update_laporan(no):
    if 'data_user' in session:
        data_lp = model.getLaporbyNo(no)
        data_user = session['data_user']
        return render_template('edit_laporan.html', data_lp=data_lp, data_user=data_user)
    return render_template('form_login.html')

@app.route('/delete_laporan/<no>')
def delete_laporan(no):
    if 'data_user' in session:
        model.deleteLaporan(no)
        return redirect(url_for('laporan'))
    return render_template('form_login.html')
  
if __name__ == '__main__':
    app.run(debug=True)
  
  
  
  
  
  
  
  