# ==========================================================
# dg202004. Ini adalah contoh Python Rest API sebagai server
# service yang dibuat adalah GET, POST, dan POST untuk login
# untuk mengetesnya maka gunakan Postman bukan pakai web lagi
# ==========================================================

from flask import Flask, request
import json

# =================================================
# ini adalah contoh membuat object dari class Flask
# =================================================
app = Flask('praxis')

# ====================================================
# Ini adalah contoh membuat Rest API dengan method GET
# Method : GET, url : localhost:5000
# ====================================================
@app.route('/', methods=['GET'])
def index():
    data = {
        'message': 'Hallo semuanya :)'
    }
    return json.dumps(data)

# =====================================================
# Ini adalah contoh membuat Rest API dengan method POST
# Method : POST, url : localhost:5000
# parameter dari client : username dan password
# =====================================================
@app.route('/', methods=['POST'])
def index_post():
    data = request.get_json()
    return json.dumps(data)

# =====================================================
# Ini adalah contoh membuat Rest API dengan method POST
# Method : POST, url : localhost:5000/login
# parameter dari client : username dan password
# =====================================================
@app.route('/login', methods=['POST'])
def index_post_login():
    data = request.get_json()
    # TODO algoritma login
    berhasil = {
        'message': f'Selamat datang {data["username"]} '
    } 
    return json.dumps(berhasil)

# =====================================================
# Ini adalah untuk menjalankan aplikasi
# =====================================================
app.run(debug=True)