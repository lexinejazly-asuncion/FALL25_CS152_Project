import pandas as pd
import json

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

#loads the club data from the json file
def load_clubs(CLUB_PATH):
    with open(CLUB_PATH, "r", encoding = "utf-8") as f:
        clubs = json.load(f)

    return clubs

#initializes a dataframe from the loaded club data
def json_to_dframe(clubs):
    df = pd.DataFrame(clubs)

    #create a new column 'tags' that concatenates the data from 'mission' and 'benefits'
    df["mission_and_benefits"] = (df["mission"] + " " + df["benefits"]).str.strip()
    
    df = df[["name", "category", "mission_and_benefits"]] #selects columns 'name' and 'tags'

    df = df.set_index("name") #set the name of club as the index

    return df

lemmatizer = WordNetLemmatizer() #reduces a word to its base form
stop_words = set(stopwords.words('english')) #common english words 

VERB_CODES = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'} #tags that idetify the verb category

#returns keywords from the clubs mission and benefits
def preprocess(text):
    text = text.lower()

    words = nltk.word_tokenize(text) #splits the words into individual tokens
    tags = nltk.pos_tag(words) #tags the words with part of speech

    temp_tokens = []

    #ite
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
    final_sent = " ".join(temp_tokens)

    final_sent = final_sent.replace("n't", " not")
    final_sent = final_sent.replace("'m", " am")
    final_sent = final_sent.replace("'s", " is")
    final_sent = final_sent.replace("'re", " are")
    final_sent = final_sent.replace("'ll", " will")
    final_sent = final_sent.replace("'ve", " have")
    final_sent = final_sent.replace("'d", " would")

    return final_sent


