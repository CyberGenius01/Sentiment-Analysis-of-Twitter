import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def __cleanString(string):
    clean_string = re.sub('[^a-zA-Z]', ' ', string)
    clean_string = clean_string.lower()
    clean_string = clean_string.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    clean_string = [ps.stem(word) for word in clean_string if not word in set(all_stopwords)]
    clean_string = ' '.join(clean_string)
    
    return clean_string

with open('sentiment_model.pkl', 'rb') as f:
    cVizer, classifier = pickle.load(f)

def sentimentAnalysis(string):
    clean_string = __cleanString(string)
    string = cVizer.transform([clean_string]).toarray()
    result = classifier.predict(string)
    if int(result[0]) == 0:
        return 'Negative', clean_string.split()
    else:
        return 'Positive', clean_string.split()