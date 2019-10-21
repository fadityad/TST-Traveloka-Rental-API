import requests
from flask import Flask, Response, request, jsonify
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config["DEBUG"] = True
url = "https://www.traveloka.com/id-id/rental-mobil/"
board_members = []


@app.route('/', methods=['GET'])
def home():
    return '''API Rental Mobil di beberapa kota Indonesia'''

@app.route('/kota/<city>', methods=['GET'])
def kota(city):
    #Kota/Region yang menyediakan rental mobil
    list_city = ['bali', 'yogyakarta', 'jakarta', 'bandung', 'surabaya', 'malang', 'makassar', 'semarang', 'medan']

    #Ada dalam list_city
    if city in list_city:
        #Region yang menyediakan rental mobil
        if city == 'bali' or city == 'yogyakarta' or city == 'jakarta':
            _kota = requests.get(url + 'region/' + city)

        #Kota yang menyediakan rental mobil
        else:
            _kota = requests.get(url + 'city/' + city)

    #Tidak ada dalam list_city
    else:
        return Response(status=404)

    _soup = BeautifulSoup(_kota.text, 'html.parser')    
    #List dari keterangan tabel
    data = []
    
    #Parsing HTML ke JSON
    table = _soup.find('tbody')

    #Untuk semua tr.b yang ada di tbody
    #Kemudian di append object
    for tr in table.find_all('tr'):
        data.append({
            'MOBIL': tr.find('b').string    
        })
  
    return jsonify(data)
        
app.run()
#app.run (debug = true)
