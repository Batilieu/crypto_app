from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# قائمة العملات المتاحة
CRYPTO_IDS = {
    'bitcoin': 'Bitcoin',
    'ethereum': 'Ethereum',
    'fantom': 'Fantom',
    'binancecoin': 'Binance Coin',
    'ripple': 'XRP',
    'cardano': 'Cardano',
    'solana': 'Solana',
    'polkadot': 'Polkadot',
    'dogecoin': 'Dogecoin',
    'tether': 'Tether'
}

def get_crypto_data(crypto_id):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': '1'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['prices']

@app.route('/', methods=['GET', 'POST'])
def index():
    crypto_id = 'bitcoin'  # عملة افتراضية
    if request.method == 'POST':
        crypto_id = request.form.get('crypto_id', 'bitcoin')  # الحصول على العملة المختارة

    prices = get_crypto_data(crypto_id)
    current_price = prices[-1][1]
    previous_price = prices[0][1]
    trend = "صعود" if current_price > previous_price else "هبوط"
    return render_template('index.html', current_price=current_price, trend=trend, crypto_ids=CRYPTO_IDS, selected_crypto=crypto_id)

if __name__ == '__main__':
    app.run(debug=True)
