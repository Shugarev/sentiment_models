import re
import nltk
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')

from nltk.corpus import stopwords

ticker_pattern = re.compile(r'(^\$[A-Z]+|^\$ES_F)')
ht_pattern = re.compile(r'#\w+')

charonly = re.compile(r'[^a-zA-Z\s]')
handle_pattern = re.compile(r'@\w+')
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
url_pattern = re.compile(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
pic_pattern = re.compile('pic\.twitter\.com/.{10}')
special_code = re.compile(r'(&amp;|&gt;|&lt;)')
tag_pattern = re.compile(r'<.*?>')

STOPWORDS = set(stopwords.words('english')).union({'rt', 'retweet', 'RT', 'Retweet', 'RETWEET'})
lemmatizer = WordNetLemmatizer()


def hashtag(phrase):
    return ht_pattern.sub(' ', phrase)


def remove_ticker(phrase):
    return ticker_pattern.sub('', phrase)


def specialcode(phrase):
    return special_code.sub(' ', phrase)


def emoji(phrase):
    return emoji_pattern.sub(' ', phrase)


def url(phrase):
    return url_pattern.sub('', phrase)


def pic(phrase):
    return pic_pattern.sub('', phrase)


def html_tag(phrase):
    return tag_pattern.sub(' ', phrase)


def handle(phrase):
    return handle_pattern.sub('', phrase)


def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # DIS, ticker symbol of Disney, is interpreted as the plural of "DI"
    # in WordCloud, so I converted it to Disney
    phrase = re.sub('DIS', 'Disney', phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"(he|He)\'s", "he is", phrase)
    phrase = re.sub(r"(she|She)\'s", "she is", phrase)
    phrase = re.sub(r"(it|It)\'s", "it is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"(\'ve|has)", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


def onlychar(phrase):
    return charonly.sub('', phrase)


def remove_stopwords(phrase):
    return " ".join([word for word in str(phrase).split() \
                     if word not in STOPWORDS])


def tokenize_stem(phrase):
    tokens = word_tokenize(phrase)
    stem_words = []
    for token in tokens:
        word = lemmatizer.lemmatize(token)
        stem_words.append(word)
    buf = ' '.join(stem_words)
    return buf


class DataPreprocessing:

    @classmethod
    def arrange_text(cls, ds):
        ds = ds.copy()
        ds['text2'] = ds['text'].apply(emoji)
        print('emojy')
        ds['text2'] = ds['text2'].apply(handle)
        print('hadnle')
        ds['text2'] = ds['text2'].apply(specialcode)
        ds['text2'] = ds['text2'].apply(hashtag)
        ds['text2'] = ds['text2'].apply(url)
        print('url')
        ds['text2'] = ds['text2'].apply(pic)
        ds['text2'] = ds['text2'].apply(html_tag)
        ds['text2'] = ds['text2'].apply(onlychar)
        print('onlychar')
        ds['text2'] = ds['text2'].apply(decontracted)
        print('decontracted')
        ds['text2'] = ds['text2'].apply(onlychar)
        print('onlychar')
        ds['text2'] = ds['text2'].apply(tokenize_stem)
        print('tokenize strem')
        #     ds['text2'] = ds['text2'].str.lower()
        #     print('in_lower')
        ds['text2'] = ds['text2'].apply(remove_stopwords)
        print('remove_stopwords')
        return ds