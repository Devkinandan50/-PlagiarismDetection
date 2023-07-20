from pdfinfo import extract_text_from_pdfs


def pdfData(file1, file2):
    pdf_text1, filesize1, no_of_pages1, no_of_word1, font_information1, page_layout_and_format1, author1, creator1, producer1, subject1, title1 = extract_text_from_pdfs(file1)
    pdf_text2, filesize2, no_of_pages2, no_of_word2, font_information2, page_layout_and_format2, author2, creator2, producer2, subject2, title2 = extract_text_from_pdfs(file2)

    diffrence_between_pdf_data = []

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


    return pdf_text1, pdf_text2, diffrence_between_pdf_data