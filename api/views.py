from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from evaluation.dataset_tester import DatasetTester
from .utils import validate_data


@api_view(['POST'])
def get_text_sentiment(request):
    validate, message = validate_data(request)
    if not validate:
        return Response(message, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    config_data = request.data.get('config')
    order_data = request.data.get('data')
    text = order_data.get('text')
    try:
        sentiment = DatasetTester.getsentiment(config_data, order_data)
    except Exception as e:
        raise ValidationError(e)
    return Response({"sentiment": sentiment, "text": text}, status=status.HTTP_200_OK)
