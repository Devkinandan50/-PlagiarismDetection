import re
import nltk
nltk.download('punkt')  # Download the Punkt tokenizer models
nltk.download('stopwords')  # Download the stopwords data
nltk.download('wordnet')  # Download the WordNet lemmatizer data

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def remove_stopwords(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Get the set of English stopwords
    stop_words = set(stopwords.words('english'))

    # Remove stopwords from the text
    f_words = [word for word in words if word.lower() not in stop_words]

    return ' '.join(filtered_words)





def stem_text(f_words):
    
    # Initialize the Porter Stemmer
    stemmer = PorterStemmer()

    # Perform stemming on each word
    stemmed_words = [stemmer.stem(word) for word in f_words]

    return ' '.join(stemmed_words)



def lemmatize_text(f_words):
    
    # Initialize the WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Perform lemmatization on each word
    lemmatized_words = [lemmatizer.lemmatize(word) for word in f_words]

    return ' '.join(lemmatized_words)



def clean_text(text):
    # Remove special characters, numbers, and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned_text = cleaned_text.lower()
    return cleaned_text



def preprocessing_using_nlp(text1, text2):
    return 34

my_variable = 42





