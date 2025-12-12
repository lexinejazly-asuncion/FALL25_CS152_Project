import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer() #reduces a word to its base form
stop_words = set(stopwords.words('english')) #common english words 

VERB_CODES = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'} #tags that idetify the verb category

#returns keywords from the clubs mission and benefits
def preprocess(text):
    text = text.lower()

    words = nltk.word_tokenize(text) #splits the words into individual tokens
    tags = nltk.pos_tag(words) #tags the words with part of speech

    temp_tokens = []

    #iterate through each token
    for i, word in enumerate(words):
        tag = tags[i][1]
  
        #for verbs, lemmatize to the verb's base form
        if tag in VERB_CODES:
            lemmatized = lemmatizer.lemmatize(word, 'v')
        #for others lemmatize using default, treating it as noun
        else:
            lemmatized = lemmatizer.lemmatize(word)

        #if a word is an alphabetic token and is not a common english work, keep it
        if lemmatized.isalpha() and lemmatized not in stop_words:
            temp_tokens.append(lemmatized)

    #concatenate all tokens into one string
    tokens = " ".join(temp_tokens)

    tokens = tokens.replace("n't", " not")
    tokens = tokens.replace("'m", " am")
    tokens = tokens.replace("'s", " is")
    tokens = tokens.replace("'re", " are")
    tokens = tokens.replace("'ll", " will")
    tokens = tokens.replace("'ve", " have")
    tokens = tokens.replace("'d", " would")

    return tokens


