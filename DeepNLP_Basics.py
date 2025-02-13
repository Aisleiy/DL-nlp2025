import nltk
# Download the 'punkt' resource to enable tokenization
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')


# Word Tokenization
text = "Hello, how are you?"
tokens = nltk.word_tokenize(text)
print(tokens)  # Output: ['Hello', ',', 'how', 'are', 'you', '?']

# Character Tokenization
text = "hello"
char_tokens = list(text)
print(char_tokens)  # Output: ['h', 'e', 'l', 'l', 'o']
