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
        avg = np.mean([gensim_model.wv.get_vector(key=word) for word in sentence_of_words[i] if word in gensim_model.wv.index_to_key], axis=0)
        transformed.append(avg)
    # convert into array
    avgword2vec_array = np.asarray(transformed)

    if ml_model.predict(X=avgword2vec_array)[0] == 1:
        print("The Email is Spam")
    else:
        print("The Email is Not Spam")


if __name__ == "__main__":
    test(text="Hay, You got iphone 11 pro max")