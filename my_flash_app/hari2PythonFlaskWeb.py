# =================================================
# dg202004. Ini adalah Flask web dengan menggunakan
# template jinja2. File index harus ditempatkan
# pada folder templates
# =================================================
from flask import Flask, render_template

app = Flask('web')

# =================================================
# route untuk url '/'. Dan file index.html harus
# ditempatkan pada folder tempates
# =================================================
@app.route('/')
def index():
    return render_template('hari2Index.html')

# =================================================
# ini untuk mengirimkan nama yang dikirim oleh
# client pada saat http request, pada parameternya
# dan dikembalikan pada saat response ke file 
# view haloNama.html
# =================================================
@app.route('/nama/<valueNama>')
def index_haloNama(valueNama):
    return render_template('hari2HaloNama.html', fieldNama = valueNama)

# ==================================================
# ini adalah untuk :
# - menerima 2 angka dari http request
# - kemudian melakukan perhitungan tambah
# - kemudian mengirimkan hasil perhitungan pada file
#   templatenya (hari2Hitung.html)
# ==================================================
@app.route('/hitung/<valueAngka1>/<valueAngka2>')
def hitung(valueAngka1, valueAngka2):
    hasil = int(valueAngka1) + int(valueAngka2)
    return render_template('hari2Hitung.html', fieldHasil = hasil)

app.run(debug = True, port=8089)