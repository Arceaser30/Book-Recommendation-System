# Book-Recommendation-System

Introduction
This Book Recommender System is designed to help users discover popular books based on extensive analysis of user reviews. It leverages reviews from users who have given reviews at least 250 times and focuses on books that have been reviewed at least 50 times. This approach ensures that recommendations are based on a substantial amount of user feedback, providing reliable and popular book suggestions.

Features
1. Popular Books Analysis: Identifies and recommends books that are highly rated by prolific reviewers.
2. Similarity-Based Recommendations: Suggests books similar to a user-inputted book based on precomputed similarity scores.
3. Interactive UI: A user-friendly interface that allows users to easily get book recommendations.

Installation Prerequisites
1) Python 3.10
2) Flask
3) Numpy
4) Pandas
5) Pickle

Usage
* Homepage: Displays the top 50 books based on user reviews.
* Recommend Page: Allows users to input a book title and get similar book recommendations.

Screenshots
* Homepage -> ![ot1](https://github.com/user-attachments/assets/9747caab-7de0-4179-9216-4070a406daa0)

* About Page -> ![ot3](https://github.com/user-attachments/assets/24250441-6418-41dc-b85e-a9f7d4312b6e)

* Recommendation Page -> ![ot2](https://github.com/user-attachments/assets/7bad416e-cd4c-4a47-a7c1-8a380d9c6c8d)


File Structure
app.py: Main Flask application file.

templates/: Contains HTML templates for rendering web pages.
 -index.html: Homepage displaying top 50 books.
 -about.html: About page with project information.
 -recommend.html: Page for getting book recommendations.

popular.pkl: Pickle file containing popular books data.
pt.pkl: Pickle file containing pivot table data.
books.pkl: Pickle file containing book details.
similarity_scores.pkl: Pickle file containing similarity scores.
