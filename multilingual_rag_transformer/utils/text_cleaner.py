import re
import unicodedata
from langdetect import detect
import nltk
import string

nltk.download('punkt')
from nltk.tokenize import sent_tokenize


def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"


def clean_text_english(text: str) -> str:
    # Normalize Unicode characters
    text = unicodedata.normalize("NFKC", text)

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Remove non-printable characters and excessive whitespace
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    
    
    
    #remove the email
    text = re.sub(r'\S+@\S+', '', text)

    # Only keep English letters/numbers
    # text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    #remove the links
    text = re.sub(r'http\S+', '', text)
    
    #remove the / alone follwed by space 
    text = re.sub(r'/\s', '', text)
    

    return text.strip()


def clean_text_french(text: str) -> str:
    
   # Normalize Unicode characters
    text = unicodedata.normalize("NFKD", text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    
    text = text.replace('œ', 'oe').replace('Œ', 'OE')
    
    text = re.sub(r'[^\w\s-]', '', text)

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    #remove the email
    text = re.sub(r'\S+@\S+', '', text)


    #remove the links
    text = re.sub(r'http\S+', '', text)
    


    return text.strip()


def tokenize_sentences(text: str) -> list:
    return sent_tokenize(text)


def preprocess_file(input_path: str, output_path: str):
    with open(input_path, 'r', encoding='utf-8') as infile:
        raw = infile.read()

    # Use file name to select language-specific cleaner
    if 'french' in input_path.lower():
        cleaned = clean_text_french(raw)
    else:
        cleaned = clean_text_english(raw)
    sentences = tokenize_sentences(cleaned)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for sent in sentences:
            outfile.write(sent.strip() + '\n')
