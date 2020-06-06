# ==================================================
# dg202004 Ini adalah contoh file untuk python Flask
# jadi untuk web. Dan pengetesannya menggunakan web
# browser, tapi tidak perlu pakai Postman
# ===================================================

from flask import Flask, render_template

# =============================================
# Ini untuk membuat object dari class Flask
# dengan nama folder templatenya bukan yang
# default. note, yg default nama foldernya
# adalah templates (tidak perlu dituliskan)
# =============================================
app = Flask('web', template_folder='views')

# ==================================================
# Ini digunakaan untuk membuat rute untuk menentukan
# url. Dan fungsi di bawahnya adalah fungsi yang
# akan dijalankan, bila url tersebut diakses oleh
# pengguna / client
# ==================================================
@app.route('/')
def index():
    return 'Hello World dan halo semua'

# ==================================================
# Ini adalah contoh untuk url login bila diakses 
# oleh pengguna / client
# ==================================================
@app.route('/login')
def login():
    return 'yuk login'

# =================================================
# Ini adalah contoh url untuk register
# =================================================
@app.route('/register')
def register():
    return 'daftar dulu yaa..'

# =================================================
# Ini adalah contoh route dengan parameter 1 buah
# pada request dari client dan mengembalikan 1 buah 
# parameter ke client untuk ditampilkan oleh web
# browser 
# =================================================
@app.route('/users/<id>')
def users_by_id(id):
    return f'Ini adalah user yang ke {id}'
    
# =================================================
# - Menerima parameter tanggal (date)
# - Mengirimkan variable langsung pada browser
# =================================================
@app.route('/tanggal/<path:valueTanggalMasuk>')
def func_tanggalMasuk(valueTanggalMasuk):
    return valueTanggalMasuk

app.run(debug=True)