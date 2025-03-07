# 📚 Book Recommendation System

## Credits

This Book Recommendation System app was developed by [**Rudransh Verma**](https://github.com/RudranshVerma23) and [**Khushi Jain**](https://github.com/jainkhushi23) as a final group assignment of the Google Developer Groups (GDG) Project - **Suggesteria**

---
## App Link

You can try the live version of this Book Recommendation System app by clicking the link below:
NOTE: The site may be temporarily closed when you visit it. If it is mentioned that the app has gone to sleep, click on "Yes, get it back up". It may take a few minutes to be functional again.

[📚 Book Recommendation System](https://book-recommendation-system-gdg.streamlit.app/)

---

## Dataset

The dataset used for this book recommendation system was retrieved from [Goodreads BBE Dataset](https://github.com/scostap/goodreads_bbe_dataset). 

This dataset contains book details, including titles, ratings, authors, and cover images, which were used to generate the recommendations.

---

## Description

This Book Recommendation System uses a hybrid of *Content-based filtering* and *Collaborative filtering* machine learning approach to recommend book. It utilizes the Goodreads dataset, leveraging the power of Annoy (Approximate Nearest Neighbors Oh Yeah) for fast and efficient book similarity retrieval. Users can select a book from a dropdown, and the app will suggest the top 10 most similar books based on various attributes, such as book titles and ratings.

### Key Features:
- **Book Recommendations**: The app suggests similar books based on a selected book's title.
- **Interactive UI**: Built with Streamlit for an easy-to-use interface, allowing users to select a book and get recommendations instantly.
- **Goodreads Integration**: Each book recommendation is linked to Goodreads, where users can explore more information about the book.
- **Efficient Search**: Uses Annoy for fast similarity search.

---

## Algorithms and Implementation

### 1. **Annoy (Approximate Nearest Neighbors Oh Yeah)**

The core algorithm used in this system for finding similar books is **Annoy**, which is a library designed to perform fast approximate nearest neighbor searches. It allows us to find the most similar books to a given book in a large dataset efficiently.

#### Implementation:
- **Annoy Index**: We load a pre-trained Annoy index (`Book_Recommendation.ann`) with a dimension of 5000. The index is created based on the book's features (like embeddings derived from the book titles, descriptions, etc.).
- **Angular Distance**: The Annoy index uses angular distance to measure similarity between books. The lower the angular distance, the more similar the books are.
- **Search Mechanism**: The `recommend` function retrieves the top 15 most similar books to the selected book using the `get_nns_by_item` function.

### 2. **Filtering and Ranking**
Once the 15 similar books are retrieved:
- **Filtering**: Books with certain words like 'sampler', 'boxset', or 'box set' in the title are filtered out.
- **Sorting**: The remaining books are sorted based on their ratings in descending order, ensuring that higher-rated books are recommended first.

---

## Libraries and Technologies Used

- **Streamlit**: For creating the interactive web application interface. It helps in displaying the UI components and visualizing the book recommendations.
- **Annoy**: For efficient similarity search and retrieval of the most similar books. The Annoy index is pre-trained and loaded from a file for fast lookups.
- **Pandas**: For handling and processing the book dataset. Pandas is used to load and manipulate the book data (such as titles, ratings, and cover images).
- **Pickle**: Optionally used for loading the book dataset if you prefer using pickle files over CSV.

---

## Installation

1. Clone this repository:
```bash
   git clone https://github.com/yourusername/book-recommendation-system.git
```
2. Install dependencies:
```bash
   pip install -r requirements.txt
  ```
3. Run the Streamlit app:
  ```bash
    streamlit run app.py
  ```
4. Open the app in your browser at http://localhost:8501.
## Files in the Repository

- **app.py**: Main Streamlit app file which contains the core logic and UI components.
- **new_books.csv**: Dataset containing book details (e.g., title, author, rating, cover image). Ensure this file is available in the correct directory.
- **Book_Recommendation.ann**: Pre-trained Annoy index used for book recommendations.
- **requirements.txt**: List of Python dependencies required for the project.

## Contributing

Feel free to fork the repository. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

