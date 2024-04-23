import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
def remove_stop_words(text):
    text=text.lower()
    swords=set(stopwords.words("english"))
    words=word_tokenize(text)
    words=[word for word in words if word.lower() not in swords]
    return words
def count_words(words):
    w_count = Counter(words)
    return w_count 
def main():
    try:
        # Read the contents of the file
        with open(r"./paragraphs.txt", "r") as file:
            text = file.read()

        # Remove stop words
        f_words = remove_stop_words(text)

        # Count word frequency
        word_counts = count_words(f_words)

        # Display word frequency count
        for w, c in word_counts.items():
            print(f"{w}: {c}")
            
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An I/O error occurred while reading the file.")

if __name__ == '__main__':
    main()
