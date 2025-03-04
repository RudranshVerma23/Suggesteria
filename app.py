import streamlit as st
import pandas as pd
from annoy import AnnoyIndex
import pickle

# Load book data (Title & Index)
books = pd.read_csv("./new_books.csv")  # Replace with your dataset
# books = pickle.load(open("books.pkl", "rb"))  # Replace with your dataset
# Load Annoy index
dimension = 5000  # Ensure this matches the saved index
annoy_index = AnnoyIndex(dimension, 'angular')
annoy_index.load("Book_Recommendation.ann")  # Load the saved Annoy index

# Function to get book recommendations
def recommend(book):
    book_index = books[books['title'] == book].index[0]
    similar_books = annoy_index.get_nns_by_item(book_index, 15)

    similar_books = [i for i in similar_books if "sampler" not in books.iloc[i]['title'].lower()]
    similar_books = [i for i in similar_books if "boxset" not in books.iloc[i]['title'].lower()]
    similar_books = [i for i in similar_books if "box set" not in books.iloc[i]['title'].lower()]
    similar_books = sorted(similar_books, key=lambda x: books.iloc[x]['rating'], reverse=True)
    return similar_books

# Streamlit UI
st.title("📚 Book Recommendation System")

selected_book = st.selectbox(
    "Type or select a book from the dropdown:",
    books['title'].values
)

if st.button("Get Recommendations"):
    recommendations = recommend(selected_book)
    st.write("### Recommended Books:")

    # Create two rows with 5 columns each
    row1 = st.columns(5)
    row2 = st.columns(5)

    counter = 0
    for book in recommendations:
        if counter >= 10:
            break
        
        # Select the appropriate row
        col = row1[counter] if counter < 5 else row2[counter - 5]

        with col:
            st.image(books.loc[book, 'coverImg'], width=150)  # Set larger width
            st.text(books.loc[book, 'title'])
        
        counter += 1
