import streamlit as st
import pickle
import numpy as np


Books_list_df = pickle.load(open('Books.pkl','rb'))
Books_list = Books_list_df.index.values

similarity_scores = pickle.load(open('similarity.pkl','rb'))

Books_url = pickle.load(open('Image_URL.pkl','rb'))

def recommend(book_name):
  # index fetch
  index = np.where(Books_list_df.index==book_name)[0][0]
  similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]

  recommended_books = []
  recommended_books_posters = []

  for i in similar_items:
    recommended_books.append(Books_list_df.index[i[0]])
    # fetch book poster from image URL
    recommended_books_posters.append(Books_url.loc[Books_url[Books_url['Book-Title'] == Books_list_df.index[i[0]]].index.values[0]].at['Image-URL-L'])

  return  recommended_books ,recommended_books_posters

st.title("Book Recommender System")


Selected_book_name = st.selectbox(
    'Search your book here',
    (Books_list))



if st.button('Recommend'):
    names,posters= recommend(Selected_book_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
      st.text(names[0])
      st.image(posters[0])

    with col2:
      st.text(names[1])
      st.image(posters[1])

    with col3:
      st.text(names[2])
      st.image(posters[2])

    with col4:
      st.text(names[3])
      st.image(posters[3])

    with col5:
      st.text(names[4])
      st.image(posters[4])






