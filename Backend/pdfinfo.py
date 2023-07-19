import PyPDF2

def extract_text_from_pdfs(file):
    pdf_text = ''
    
    # for file in [file1, file2]:
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()


    # find author and other info of pdf
    meta = pdf_reader.metadata


    # All of the following could be None!
    print(len(pdf_reader.pages))
    print(meta.author)
    print(meta.creator)
    print(meta.producer)
    print(meta.subject)
    print(meta.title) 
    
    author = ""
    creation_date = ""
    update_date = ""
    return pdf_text, author, creation_date, update_date