from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'nithis', 'barcode': '1248r9223','marks': 95},
        {'id': 2, 'name': 'yash', 'barcode': '123985473165', 'marks': 50},
        {'id': 3, 'name': 'saurabh', 'barcode': '231985128446', 'marks': 150}
    ]
    return render_template('market.html', items=items)

if __name__=="__main__":
    app.run(debug=True)
