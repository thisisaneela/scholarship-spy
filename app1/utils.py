import requests
import json
import warnings
warnings.filterwarnings('ignore')
from django.conf import settings
from django.core.mail import send_mail
import re
import numpy as np
import pandas as pd
from heapq import nsmallest
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from nltk.tokenize import word_tokenize

def get_all_countries():
    url = "https://restcountries.com/v3.1/all"

    response = requests.get(url)

    countries_response_json = json.loads(response.text)

    countries_list = []

    for country in countries_response_json:
        countries_list.append(country['name']['common'])


    return sorted(countries_list)

def send_email_token(email,token):
    try:
        subject = 'Welcome to Scholarship Spy'
        message = f'Hello, Thanks for signing up to Scholarship Spy! Explore our website. So, that you can search scholarships of your own and also get personalized recommendations from us as per your interest :)'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
                
        
    except Exception as e:
        return False
    
    return True

def Clean(text):
    text = text.lower()

                # Remove all characters which are not alphabetical or numerical
    text = re.sub(r'[\W_]', ' ', text)

                # Tokenization
    text = word_tokenize(text)

                # Filter out stop words
    text = [w for w in text if not w in set(stopwords.words('english'))]

    return text

def word_embeddings():
    embeddings = {}
    with open("glove.6B.50d.txt", 'r', encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], "float32")
            embeddings[word] = vector
    return embeddings

def Vectorize(text, embeddings):
                # Generate vector representation
    vec = np.zeros(50)
    count = 0
    for i in text:
        try:
            vec += embeddings[i]
            count += 1
        except:
            pass
    return vec/count

            #centroids = np.load('cluster_centers.npy', allow_pickle=True)

def recommend(text, embeddings, centroids, n=5):
    temp = Clean(text)
    temp = Vectorize(temp, embeddings)
    diff = centroids - temp
    dist = list(np.sum(diff**2, axis=-1) ** 0.5)
    idx = [i for i in map(dist.index, nsmallest(n, dist))]

    return idx