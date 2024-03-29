import numpy as np
import tensorFlow as tf
import pandas as pd

dataset = pd.read_csv('Data_new.tsv',delimiter='\t\t\t\t\t\t\t\t\t\t\t\t\t', quoting = 3, encoding='latin-1')

"""## Cleaning the texts"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

print(dataset['text of the tweet'].shape)
print(dataset['text of the tweet'].head())

corpus = []
for i in range(39999):
  review = re.sub('[^a-zA-Z]', ' ',  dataset['text of the tweet'][i]) #remove non necessary characters
  review = review.lower() #lowercaing letters
  review = review.split() #splitting into indivisual words
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  corpus.append(review)

print(corpus)

"""## Creating the Bag of Words model"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 36000)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,-1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

## Buliding and compiling the model
ann = tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=36000, activation='relu'))
ann.add(tf.keras.layers.Dense(units=36000, activation='relu'))
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
ann.fit(X_train, y_train, batch_size=32, epochs=100)

"""## Saving the model"""
ann.save('deep_sentiment_model.h5')