from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("gabungan_resep.csv")

@app.route('/')
def home():
    return "API Resep Deta Siap Digunakan 🍽️"

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    keyword = data.get('makanan', '').lower()

    for i, row in df.iterrows():
        if keyword in row['Title'].lower():
            return jsonify({
                'title': row['Title'],
                'ingredients': row['Ingredients'],
                'steps': row['Steps'],
                'love': int(row['Loves']),
                'url': row['URL']
            })

    return jsonify({'message': 'Resep tidak ditemukan'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
