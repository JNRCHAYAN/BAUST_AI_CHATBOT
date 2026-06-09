from langchain_community.document_loaders import PyPDFLoader

def load_pdfs():
   
    # Here we can put all the file name in the data folder 
    files =[
        "data\CSE-OBE-Syllabus.pdf"
    ]
    docs = []
    for file in files:
        loader = PyPDFLoader(file)
        docs.extend(loader.load())
    return docs 