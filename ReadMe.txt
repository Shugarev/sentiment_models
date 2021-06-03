Старт сервера:
python manage.py runserver

# save environment settings to file.
pip freeze > requirements.txt

------------------------------------------------------------------------------------------------------------
Открыть доступ для всех ip. в файерволе.
sudo ufw allow 8040

Проверить в файле create-docker_image.sh, в settings.py установлен:
    DEBUG = False

для запуска на сервере нужно:
- создать папку для сервиса
- в нее положить docker-compose.yml
- созадать поддиректорию media и положить в нее сохраненные модели и файлы с моделями если необходимо.
- для поднятия сервиса выполнить docker-compose up
- пример url по которому произовдится проверка ордреа,

http://192.168.0.105:8040/api/v4/check_text_order/ - из локальной сети
http://127.0.0.1:8040/api/v4/check_text_order/ - с сервера
и в файлах: curl-api-keras.sh, curl-api-sgd.sh

Пример config c необходимыми полями:
{"config": {"profile": "sgd_classifier_multiclass", "vectorized_model": "tf_idf"},
"data": { "text": "Celcuity Q EPS Misses Estimate"}}

В docker-compose нужно задать порт по которому будет слушаться: 8040

Если мы не хотим пушить образ в докер репозиторий, то используем команды для сохранения и загрузки образа:
docker save -o ~/check_text_order_with_finbert.tar shugarev1974/check_text_order_with_finbert

Копируем файл в корневую папку докер контейнера.
Делаем из папки контейнера архив.
tar -czvf  docker_sentiment_models_with_finbert_3_06_2021.tar.gz .

Как развернуть контейнер:
Для записи на сервер поменять пользователя:
sudo chown sergey:sergey check_text_order_with_finbert.tar
скопировать файл на сервер и распаковать образ.
docker load -i check_text_order_v4.tar

Для работы 'pytorch' нужно добавлять модель в файл pytorch_models.py. Пример модели в классе 'MLP'. Файл
pytorch_models.py должен быть в папке 'media' докер-контейнера.
-----------------------------------------------------------------------------------------------------------
Для тестирования приложения на сервере по локальной запустить curl-api-keras.sh
Для тестирования приложения на сервере скрипт curl-api-keras.sh нужно запускать под sudo

Пример ответа, где "negative" - предсказаный сентимент текста:
{"sentiment":"negative","text":"Celcuity Q EPS Misses Estimate"}

