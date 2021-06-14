import os
from os import listdir
from os.path import isfile, join
from gensim.models import Word2Vec

import joblib
import keras
from check_text_order_api.settings import BASE_DIR

from transformers import AutoModelForSequenceClassification
from finbert.finbert import predict

models = {}
_positive = 'positive'
_negative = 'negative'
_neutral = 'neutral'
finbert_label = {0: 'positive', 1:  'negative', 2: 'neutral'}


def get_full_path(name):
    return "{}/media/{}".format(BASE_DIR, name)


def get_model_list():
    media_path = "{}/media/".format(BASE_DIR)
    onlyfiles = [f for f in listdir(media_path) if isfile(join(media_path, f)) and '.' not in f]
    return onlyfiles

def get_model(model_name: str):
    if models.get(model_name):
        return models[model_name]
    model_path = get_full_path(model_name)
    if model_name.startswith('sgd') or model_name.startswith('tf'):
        model = joblib.load(model_path)
        models[model_name] = model
    elif model_name.startswith('wordtovec'):
        # Загружаем обученную модель
        w2v_model = Word2Vec.load('wordtovec_model.w3v')
        models[model_name] = w2v_model
        return w2v_model
    elif model_name.startswith('tokenizer'):
        tokenizer = joblib.load(model_path)
        models[model_name] = tokenizer
        return tokenizer
    elif model_name.startswith('keras'):
        model_keras = keras.models.load_model(model_path)
        models[model_name] = model_keras
        return model_keras
    elif model_name.startswith('pytorch'):
        model_path = "{}/media/{}".format(BASE_DIR, 'finbert_model')
        model_finbert = AutoModelForSequenceClassification.from_pretrained(model_path, cache_dir=None, num_labels=3)
        models[model_name] = model_finbert
        return model_finbert

    return model


def validate_data(request):
    message = {}
    validate = True
    data = request.data.get('data')
    if not data:
        message['data_error'] = 'Data is required'
        validate = False
    else:
        text = data.get('text')
        if not text:
            message['data_text'] = 'Field text in data is required'
            validate = False

    config = request.data.get('config')
    if not config:
        message['config_error'] = 'Config is required'
        validate = False
    else:
        profile_name = config.get('profile')
        if not profile_name:
            message['profile_error'] = 'Profile is required in config'
            validate = False

    return validate, message

def get_finbert_prediction(model_finbert, text):
    result = predict(text, model_finbert)
    predict_label = _neutral
    label = result['prediction'].values

    if _positive in label and _negative not in label:
        predict_label = _positive
    elif _positive not in label and _negative in label:
        predict_label = _negative
    return predict_label