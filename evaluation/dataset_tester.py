import pandas as pd
from api.utils import get_model, finbert_label
from evaluation.datasetPrepocessing import DataPreprocessing
from keras.preprocessing.sequence import pad_sequences

SENTENCE_LENGTH = 43


def get_sequences(tokenizer, x):
    sequences = tokenizer.texts_to_sequences(x)
    return pad_sequences(sequences, maxlen=SENTENCE_LENGTH)


class DatasetTester:

    @classmethod
    def getsentiment(cls, config_data, order_data) -> str:
        model_name = config_data.get('profile')
        if model_name.startswith("sgd"):
            return cls.get_sentiment_sgd(config_data, order_data)
        elif model_name.startswith("keras"):
            return cls.get_sentiment_keras_rnn(config_data, order_data)

    @classmethod
    def get_sentiment_sgd(cls, config_data, order_data):
        model_name = config_data.get('profile')
        model_vectorized_name = config_data.get('vectorized_model')

        model_vectorized = get_model(model_vectorized_name)
        model_sgd = get_model(model_name)

        text = order_data.get('text')
        df_text = pd.DataFrame.from_dict({"text": [text]}, dtype=str)

        df_text = DataPreprocessing.arrange_text(df_text)
        X_test = model_vectorized.transform(df_text['text2'])

        model_predict = model_sgd.predict(X_test)[0]
        return finbert_label.get(model_predict)

    @classmethod
    def get_sentiment_keras_rnn(cls, config_data, order_data):

        model_cnn_name = config_data.get('profile')
        model_tokenizer_name = config_data.get('tokenizer_model')

        text = order_data.get('text')
        tokenizer = get_model(model_tokenizer_name)
        model_cnn = get_model(model_cnn_name)

        df_text = pd.DataFrame.from_dict({"text": [text]}, dtype=str)
        df_text = DataPreprocessing.arrange_text(df_text)

        x_test_seq = get_sequences(tokenizer, df_text['text2'].values)

        predict_proba = model_cnn.predict(x_test_seq)[0]
        predict_proba = list(predict_proba)

        max_index = predict_proba.index(max(predict_proba))
        return finbert_label.get(max_index)
