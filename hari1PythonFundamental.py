# ==============================================
# dg202004. Ini adalah contoh latihan hari 1 pada
# workshop python praxis dan padepokan ASA
# cara menjalankan : 
# $ python3 hari1PythonFundamental.py
# ==============================================

print(5 * '=')
# =======================================
# contoh hello world
print("Hello world")

print(5 * '=')
# =======================================
# contoh for dengan increment default
print("Ini adalah contoh for dengan increment default")
for angka in range(10) :
    print(angka)


print(5 * '=')
# =======================================
# contoh for dengan dari 1 sampai 11, increment lompat 2
print("Ini adalah contoh for dengan dari 1 sampai 11, increment lompat 2")
for angka in range(1, 11, 2) :
    print(angka)

print(5 * '=')
# ========================================
# contoh for, dengan index pertama bukan 0, tapi 5, yaitu pakai fungsi enumerate, 
# yaitu fungsi built in - nya python
print('Ini adalah contoh for, dengan index bukan dari 0, tapi 5, ')
print('yaitu dengan menggunakan fungsi bawaan python, yaitu enumerate')
data = [80, 90, 75]
for index, val in enumerate(data, start = 5) :
    print(f'index{index} - {val}')

print(5 * '=')
# =========================================
# contoh struktur data List
print('Ini adalah contoh struktur data List')
nilai = [80, 90, 75]
print(nilai)
print(nilai[2])

print(5 * '=')
# ==========================================
# contoh fungsi
print('Ini adalah contoh fungsi')
def sapa():
    print('halo')

sapa()

print(5 * '=')
# ==========================================
# contoh fungsi dengan paramenter
print('Ini adalah contoh fungsi dengan parameter')
def panggil(nama):
    print(f'selamat datang {nama}')

panggil('Dedi Gunawan')

print(5 * '=')
# ===========================================
# contoh menampilkan di layar dengan menggunakan format
print('Ini adalah contoh menampilkan di layar dengan format')
def panggilFormat(nama):
    print('Selamat datang {}'.format(nama))

panggilFormat('Dedi Gunawan2')

print(5 * '=')
# ===========================================
# contoh for dan list, dan juga for di dalam for
print('Ini adalah contoh for dan list, dan juga for di dalam for')
datas = [
    {
        'nama': 'praxis',
        'nilai': [80, 90, 75]
    },
    {
        'nama': 'padepokan ASA',
        'nilai': [60, 50, 70]
    }
]

for index in datas:
    print(f"Selamat datang {index['nama']}")
    for nil in index['nilai']:
        print(nil)









