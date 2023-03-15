
# Used python version 9.2

import streamlit as st
import pickle
import numpy as np
import re
import contractions

all_stopwords = pickle.load(file=open(file="Save Model/all_stopwords", mode="rb"))
gensim_model = pickle.load(file=open(file="Save Model/gensim_model", mode="rb"))
ml_model = pickle.load(file=open(file="Save Model/ml_model", mode="rb"))


def test(text):
    sentence_of_words = []
    transformed = []
    # Regular expression that removes all the html tags present in the reviews
    text = re.sub(pattern='(<[\w\s]*/?>)', repl="", string=text)

    # Expanding all the contractions present in the review to is respective actual form
    text = contractions.fix(text)

    # Removing all the special characters from the review text
    text = re.sub(pattern='[^a-zA-Z0-9\s]+', repl="", string=text)

    # Removing all the digits present in the review text
    text = re.sub(pattern='\d+', repl="", string=text)

    # Making all the review text to be of lower case as well as removing the stopwords and words of length less than 3
    text = " ".join([word.lower() for word in text.split() if word not in all_stopwords and len(word) >= 3])

    # Splitting the sentences into words
    sentence_of_words.append(text.split())

    for i in range(len(sentence_of_words)):
        avg = np.mean([gensim_model.wv.get_vector(key=word) for word in sentence_of_words[i] if
                       word in gensim_model.wv.index_to_key], axis=0)
        transformed.append(avg)
    # convert into array
    avgword2vec_array = np.asarray(transformed)

    if ml_model.predict(X=avgword2vec_array)[0] == 1:
        return True
    else:
        return False


def run():
    st.image(image="images/email.png")
    st.markdown("<h1 style='text-align: center;'>Email Classification</h1>", unsafe_allow_html=True)
    # st.title("Email Classifications")

    title = st.text_input(label="Enter your Email text")

    if st.button(label="Submit"):
        result = test(text=title)
        if result:
            st.write("**The Email is Spam**") # * used for bold the text
        else:
            st.write("**The Email is not Spam**")


if __name__ == "__main__":
    run()

# to run the file: streamlit run app.py
