import re

def word_tokenizer(text):
    words = re.findall(r'\b\w+\b', text)
    return words


user_input = input("Please enter text to tokenize: ")

tokenized_text = word_tokenizer(user_input)

print(tokenized_text)

input("Press Enter to exit...")