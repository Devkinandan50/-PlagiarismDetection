# import numpy as np
from pdfinformation import extract_text_from_pdfs
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity


# def Cosine_similarity(text_list1, text_list2):
#     # convert to string
#     preprocessed_text1 = ' '.join(text_list1)
#     preprocessed_text2 = ' '.join(text_list2)

#     # Create a TfidfVectorizer instance
#     tfidf_vectorizer = TfidfVectorizer()

#     # Fit and transform the preprocessed texts using TfidfVectorizer
#     tfidf_matrix = tfidf_vectorizer.fit_transform([preprocessed_text1, preprocessed_text2])

#     # Calculate cosine similarity between the two documents
#     cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

#     # Get feature names (words)
#     feature_names = tfidf_vectorizer.get_feature_names_out()

#     # Get the indices of the top features (words) based on their weights in the vectors
#     top_feature_indices = tfidf_matrix[0].indices[np.argsort(tfidf_matrix[0].data)[-10:]]

#     # Get the common words and their corresponding weights
#     common_words_and_weights = {feature_names[idx]: tfidf_matrix[0, idx] for idx in top_feature_indices}

#     return cosine_sim, common_words_and_weights


def campare(x, y):
    if x is None or y is None or x == "-" or y == "-":
        return False

    return x == y

def jaccard_similarity(text_list1, text_list2):
    # convert list to set
    set1 = set(text_list1)
    set2 = set(text_list2)

    # Calculate the intersection and union of the two sets
    common_words = set1.intersection(set2)
    intersection = len(common_words)
    union = len(set1.union(set2))
    
    # Calculate Jaccard similarity
    if union == 0:
        return 0.0
    else:
        jaccard_sim = intersection / union
        return jaccard_sim



def pdfData(file1, file2):
    # list all element of which get from extract_text_from_pdfs
    name = ["List of preprocess text", "Number of Pages", "Number of word","Font Information", "Page Layout and Format", "Author", "Creator", "Producer", "Subject", "Title"]
    ls1 = extract_text_from_pdfs(file1)
    ls2 = extract_text_from_pdfs(file2)

    diffrence_between_pdf_data = []

    # score1, common_words_and_weights = Cosine_similarity(ls1[0], ls2[0])
    score1 = 0
    common_words_and_weights = 0
    score2 = jaccard_similarity(ls1[0], ls2[0])


    for i in range(1, len(ls2)):
        result = campare(ls1[i], ls2[i])
        diffrence_between_pdf_data.append({
            "name": name[i],
            "val1": ls1[i],
            "val2": ls2[i],
            "val3": result
        })


    return diffrence_between_pdf_data, score1, score2, common_words_and_weights