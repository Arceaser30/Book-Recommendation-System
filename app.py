import os
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Get the base directory of the current file
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load pickled data using absolute paths
popular_df = pickle.load(open(os.path.join(base_dir, 'popular.pkl'), 'rb'))
pt = pickle.load(open(os.path.join(base_dir, 'pt.pkl'), 'rb'))
books = pickle.load(open(os.path.join(base_dir, 'books.pkl'), 'rb'))
similarity_scores = pickle.load(open(os.path.join(base_dir, 'similarity_scores.pkl'), 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )


@app.route('/about')
def about():
        return render_template('about.html')


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])



def recommend():
    user_input = request.form.get('user_input')
    
    if user_input in pt.index:
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Author')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Image-URL-M')['Image-URL-M'].values))

            data.append(item)

        return render_template('recommend.html', data=data)
    else:
        # Handling the case where the book is not found
        return render_template('recommend.html', data=[], error=f"Oops..Book '{user_input}' not found in the dataset.")

if __name__ == '__main__':
    app.run(debug=True)


