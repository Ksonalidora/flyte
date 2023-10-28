import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources (stopwords and punkt tokenizer)
nltk.download('stopwords')
nltk.download('punkt')

def clean_text(text):
    # Remove HTML tags (if applicable)
    text = re.sub(r'<.*?>', '', text)

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Remove non-alphabetic words
    words = [word for word in words if word.isalpha()]

    # Join the words back into a cleaned text
    cleaned_text = ' '.join(words)

    return cleaned_text

# Example usage
unstructured_text = "This is an example of unstructured text data with <html> tags and some punctuations! It needs cleaning."
cleaned_text = clean_text(unstructured_text)
print(cleaned_text)
