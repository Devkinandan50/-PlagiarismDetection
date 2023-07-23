import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# def get_font_information(file):
#     font_info = {}
#     pdf_reader = PyPDF2.PdfFileReader(file)
#     for page_number in range(pdf_reader.getNumPages()):
#         page = pdf_reader.getPage(page_number)
#         text = page.extractText()
#         for char in text:
#             font_name = char.fontname
#             font_size = char.size
#             if font_name not in font_info:
#                 font_info[font_name] = set()
#             font_info[font_name].add(font_size)
#     return font_info





# def get_page_layout_and_format(pdf_path):
#     page_info = []
    
#     with open(pdf_path, "rb") as file:
#         pdf_reader = PyPDF2.PdfFileReader(file)

#         for page_number in range(pdf_reader.getNumPages()):
#             page = pdf_reader.getPage(page_number)

#             page_width = page.mediaBox.getWidth()
#             page_height = page.mediaBox.getHeight()

#             # Determine orientation based on aspect ratio
#             is_landscape = page_width > page_height

#             page_data = {
#                 "page_number": page_number + 1,
#                 "page_width": page_width,
#                 "page_height": page_height,
#                 "is_landscape": is_landscape,
#             }

#             page_info.append(page_data)
#     return page_info




# def get_file_size(file_object):
#     try:
#         # Get the current position of the file pointer
#         current_position = file_object.tell()

#         # Move the file pointer to the end of the file
#         file_object.seek(0, 2)

#         # Get the size of the file in bytes
#         file_size = file_object.tell()

#         # Reset the file pointer to the original position
#         file_object.seek(current_position)

#         return file_size
#     except Exception as e:
#         return f"Error: {str(e)}"




def count_words_using_regex(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)



def stem_text(f_words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in f_words]
    return stemmed_words


def lemmatize_text(f_words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in f_words]
    return lemmatized_words



def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize text into words
    words = nltk.word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Lemmatization and stem
    lemmat_text_list = lemmatize_text(words)
    # lemmat_text = stem_text(words)

    # convert to string
    return lemmat_text_list




def extract_text_from_pdfs(file):
    pdf_text = ''
    no_of_word = 0
    filesize = "-"
    font_information = "-"
    page_layout_and_format = "-"
    ai_score = 0

    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        pagetext = page.extract_text()
        no_of_word += count_words_using_regex(pagetext)
        pdf_text += pagetext
    
    meta = pdf_reader.metadata
    no_of_pages = len(pdf_reader.pages)
    preprocess_text_list = preprocess_text(pdf_text)

    ls = [preprocess_text_list, filesize, no_of_pages, no_of_word, font_information, page_layout_and_format, meta.author, meta.creator, meta.producer, meta.subject, meta.title]
    
    return ls










