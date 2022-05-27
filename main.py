from flask import Flask,jsonify,request
import csv

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles =[]
unliked_articles =[]

app = Flask(__name__)

@app.route('/get-articles')
def get_articles():
    return jsonify({
        'data':all_articles[0],
        'status':'success'
    })

@app.route('/liked-articles',methods=['POST'])
def liked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        'status':'success'
    })

@app.route('/unliked-articles',methods=['POST'])
def unliked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(articles)
    return jsonify({
        'status':'success'
    })

if __name__ == '__main__':
    app.run()