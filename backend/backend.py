from flask import Flask,request,jsonify,render_template
import sqlite3
app=Flask(__name__)

def init_db():
    conn=sqlite3.connect('reviews.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, name TEXT, review TEXT)''')
    conn.commit()
    conn.close()

init_db()
@app.route('/reviews',methods=['GET'])
def get_reviews():
    conn=sqlite3.connect('reviews.db')
    c=conn.cursor()
    c.execute('SELECT name,review FROM reviews')
    reviews=c.fetchall()
    conn.close()
    return jsonify(reviews)
@app.route('/reviews',methods=['POST'])
def add_review():
    data.request.get_json()
    name=data['name']
    review=data['review']
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('INSERT INTO reviews (name, review) VALUES (?, ?)', (name, review))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True)