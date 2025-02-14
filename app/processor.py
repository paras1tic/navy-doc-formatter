from docx import Document

def format_document(filepath):
    doc = Document(filepath)
    
    # Modify document formatting logic here
    for paragraph in doc.paragraphs:
        paragraph.alignment = 1  # Example: Center align text

    output_path = filepath.replace(".docx", "_formatted.docx")
    doc.save(output_path)
    
    return output_path
