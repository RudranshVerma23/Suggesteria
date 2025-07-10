import os
import streamlit as st
import pandas as pd
from annoy import AnnoyIndex
import pickle

def download_annoy_index(url, filename):
    if not os.path.exists(filename):
        st.info("Downloading model file. Please wait...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            st.success("Model downloaded successfully!")
        else:
            st.error(f"Failed to download model file: {response.status_code}")
            st.stop()

# 📌 URL of the pre-trained Annoy model (change this to your actual Hugging Face link)
annoy_model_url = "https://huggingface.co/your-username/book-recommendation-model/resolve/main/Book_Recommendation.ann"
annoy_model_file = "Book_Recommendation.ann"
download_annoy_index(annoy_model_url, annoy_model_file)

# 📌 Load book data (Title & Index)
# Reads book dataset from a CSV file. Ensure the file exists in the correct directory.
books = pd.read_csv("Book_Recommendation_Model/new_books.csv")  # Replace with your dataset

# Alternatively, load from a pickle file if needed
# books = pickle.load(open("books.pkl", "rb"))  # Uncomment if using pickle instead

# 📌 Load the Annoy index for book recommendations
dimension = 5000  # Ensure this matches the saved Annoy index dimension
annoy_index = AnnoyIndex(dimension, 'angular')
#annoy_index.load("Book_Recommendation_Model/Book_Recommendation.ann")  # Loads the pre-trained Annoy index
annoy_index.load(annoy_model_file)  # Loads the pre-trained Annoy index


# 📌 Function to get book recommendations
def recommend(book):
    """
    Given a book title, return a list of similar books using Annoy index.
    Filters out books with words like 'sampler', 'boxset', or 'box set' in the title.
    Sorts recommendations based on book rating in descending order.
    """
    
    # Get the index of the selected book
    book_index = books[books['title'] == book].index[0]
    
    # Get the 15 most similar books using Annoy
    similar_books = annoy_index.get_nns_by_item(book_index, 15)

    # Remove books with 'sampler', 'boxset', or 'box set' in the title
    similar_books = [i for i in similar_books if "sampler" not in books.iloc[i]['title'].lower()]
    similar_books = [i for i in similar_books if "boxset" not in books.iloc[i]['title'].lower()]
    similar_books = [i for i in similar_books if "box set" not in books.iloc[i]['title'].lower()]

    # Sort recommendations based on book rating (higher-rated books first)
    similar_books = sorted(similar_books, key=lambda x: books.iloc[x]['rating'], reverse=True)

    return similar_books

# 📌 Streamlit UI Setup
st.title("📚 Book Recommendation System")  # Set the title of the Streamlit app

# 📌 Dropdown for book selection
selected_book = st.selectbox(
    "Type or select a book from the dropdown:",  # Label for dropdown
    books['title'].values  # Load book titles as options
)

# 📌 Button to generate recommendations
if st.button("Get Recommendations"):
    recommendations = recommend(selected_book)
    st.write("### Recommended Books:")

    # 📌 Create layout: Two rows with 5 columns each (for displaying 10 books)
    row1 = st.columns(5)
    row2 = st.columns(5)

    counter = 0  # Track the number of books displayed

    for book in recommendations:
        if counter >= 10:  # Display only the top 10 recommendations
            break

        # Select the appropriate row: first 5 go in row1, next 5 in row2
        col = row1[counter] if counter < 5 else row2[counter - 5]

        # 📌 Retrieve book details
        book_title = books.loc[book, 'title']  # Get book title
        book_image = books.loc[book, 'coverImg']  # Get book cover image
        book_link = f"https://www.goodreads.com/search?q={book_title}"  # Generate Goodreads search link

        with col:
            # 📌 Display hyperlinked book image (clicking opens Goodreads search)
            st.markdown(
                f'<a href="{book_link}" target="_blank">'
                f'<img src="{book_image}" width="150"></a>',
                unsafe_allow_html=True
            )
            
            # 📌 Display hyperlinked book title (styled white, no underline)
            st.markdown(
                f'<a href="{book_link}" target="_blank" '
                f'style="color: white; text-decoration: none; font-size: 16px;">'
                f'{book_title}</a>',
                unsafe_allow_html=True
            )

        counter += 1  # Increment counter for next book
