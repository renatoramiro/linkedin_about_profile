from langchain_community.document_loaders import PyPDFLoader

def load_resume(path):
    file_path = (path)
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()

    document = ''
    for i in range(len(pages)):
        document += pages[i].page_content

    return document
