from pdfinformation import extract_text_from_pdfs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def Cosine_similarity(text_list1, text_list2):
    # convert to string
    preprocessed_text1 = ' '.join(text_list1)
    preprocessed_text2 = ' '.join(text_list2)

    # Create a TfidfVectorizer instance
    tfidf_vectorizer = TfidfVectorizer()

    # Fit and transform the preprocessed texts using TfidfVectorizer
    tfidf_matrix = tfidf_vectorizer.fit_transform([preprocessed_text1, preprocessed_text2])

    # Calculate cosine similarity between the two documents
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return cosine_sim



def jaccard_similarity(text_list1, text_list2):
    # convert list to set
    set1 = set(text_list1)
    set2 = set(text_list2)

    # Calculate the intersection and union of the two sets
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    # Calculate Jaccard similarity
    if union == 0:
        return 0.0
    else:
        jaccard_sim = intersection / union
        return jaccard_sim



def pdfData(file1, file2):
    preprocess_text_list1, filesize1, no_of_pages1, no_of_word1, font_information1, page_layout_and_format1, author1, creator1, producer1, subject1, title1 = extract_text_from_pdfs(file1)
    preprocess_text_list2, filesize2, no_of_pages2, no_of_word2, font_information2, page_layout_and_format2, author2, creator2, producer2, subject2, title2 = extract_text_from_pdfs(file2)

    diffrence_between_pdf_data = []

    score1 = Cosine_similarity(preprocess_text_list1, preprocess_text_list2)
    score2 = jaccard_similarity(preprocess_text_list1, preprocess_text_list2)
    
    print(score1)
    print(score2)

    diffrence_between_pdf_data.append({
        "name": "File Size",
        "val1": filesize1,
        "val2": filesize2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Number of Pages",
        "val1": no_of_pages1,
        "val2": no_of_pages2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Number of word",
        "val1": no_of_word1,
        "val2": no_of_word2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Font Information",
        "val1": font_information1,
        "val2": font_information2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Page Layout and Format",
        "val1": page_layout_and_format1,
        "val2": page_layout_and_format2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Author",
        "val1": author1,
        "val2": author2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Creator",
        "val1": creator1,
        "val2": creator2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Producer",
        "val1": producer1,
        "val2": producer2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Subject",
        "val1": subject1,
        "val2": subject2,
        "val3": "0"
    })

    diffrence_between_pdf_data.append({
        "name": "Title",
        "val1": title1,
        "val2": title2,
        "val3": "0"
    })


    return diffrence_between_pdf_data