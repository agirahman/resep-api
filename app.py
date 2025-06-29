from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('gabungan_resep.csv')

@app.route('/')
def home():
    return 'API Resep Siap Digunakan 🍽️'

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    keyword = data.get('makanan', '').lower()

    # Filter berdasarkan keyword dalam judul
    result = df[df['Title'].str.lower().str.contains(keyword)]

    if result.empty:
        return jsonify({'message': 'Resep tidak ditemukan'})

    row = result.iloc[0]
    return jsonify({
        'title': row['Title'],
        'ingredients': row['Ingredients'],
        'steps': row['Steps'],
        'love': int(row['Loves']),
        'url': row['URL']
    })

if __name__ == '__main__':
    app.run(debug=True)
