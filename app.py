from flask import Flask, render_template, request, redirect

app = Flask(__name__)

rehber = []

@app.route('/')
def ana_sayfa():
    return render_template('index.html', rehber=rehber)

@app.route('/kisi_ekle', methods=['POST'])
def kisi_ekle():
    ad = request.form['ad']
    telefon = request.form['telefon']
    rehber.append({'ad': ad, 'telefon': telefon})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
