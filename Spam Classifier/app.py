import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

st.set_page_config(page_title = 'Abhitech - Spam Classifier')

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    return " " .join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb')) # rb = read binary
model = pickle.load(open('model.pkl', 'rb'))
st.title('Email or SMS Spam Classifier')
input_sms = st.text_area("Enter Message")
if st.button('Check'):
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    #2. vectorise
    vector_input = tfidf.transform([transformed_sms])
    #3. predict
    result = model.predict(vector_input)[0]
    #4. display
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')
st.header('A Machine Learning Project')
st.header('Check Git Hub Repo')
st.write('https://github.com/abhisekadhikari/Machine-Learning')
st.header('Give Me a Star')
st.write('https://github.com/abhisekadhikari/')
