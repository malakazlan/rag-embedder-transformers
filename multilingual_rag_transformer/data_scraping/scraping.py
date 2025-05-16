# I notice there are several issues with the code that need to be corrected. Here's the properly structured version:

import PyPDF2
import os
from typing import List, Dict, Any

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text content from a PDF file.
    Args:
        pdf_path (str): Path to the PDF file
    Returns:
        str: Extracted text content
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
            return text
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        return ""

def process_pdf_directory(directory_path: str) -> List[Dict[str, Any]]:
    """
    Process all PDF files in a directory and extract their text content.
    Args:
        directory_path (str): Path to directory containing PDF files
    Returns:
        List[Dict[str, Any]]: List of dictionaries containing file info and extracted text
    """
    results = []
    # Check if directory exists
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return results
    # Process each PDF file in directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            # Extract text from PDF
            text_content = extract_text_from_pdf(file_path)
            # Store results
            results.append({
                'filename': filename,
                'file_path': file_path,
                'text_content': text_content
            })
    return results

def save_texts_by_language(results, output_dir):
    """
    Save extracted texts into eng.txt and french.txt based on filename prefix.
    Args:
        results (list): List of dicts with 'filename' and 'text_content'.
        output_dir (str): Directory to save the output files.
    """
    eng_text = ""
    french_text = ""
    for result in results:
        fname = result['filename'].lower()
        if fname.startswith('eng'):
            eng_text += result['text_content'] + "\n\n"
        elif fname.startswith('french'):
            french_text += result['text_content'] + "\n\n"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'eng.txt'), 'w', encoding='utf-8') as f:
        f.write(eng_text)
    with open(os.path.join(output_dir, 'french.txt'), 'w', encoding='utf-8') as f:
        f.write(french_text)

