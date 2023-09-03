# NLP Subtitles difficulty level (english)

Develop an ML solution to automatically determine the difficulty level of English-language movies. Watching movies 
in their original language is a popular and effective method for language learning. However, it can be challenging 
for students to select movies that match their language proficiency level. Typically, a teacher must watch a movie to 
determine its difficulty level, which is time-consuming. To address this issue, I have developed an ML solution that 
automatically determines the difficulty level of English-language movies based on their subtitles.

## Project Goal

Our goal is to develop an ML model that can automatically classify English-language movies into four different 
difficulty levels: A2, B1, B2, and C1. These levels are based on the percentage of dialogue a student can understand, 
with A2 representing the lowest level (50-70% comprehension) and C1 representing the highest level 
(90-100% comprehension). This classification will help language learners choose movies that match their proficiency 
and enhance their language skills.

## Prerequisites

- Python 3.6 or above.
- Internet connection to access the Hugging Face translation model or 
a local copy of the model (`sentence-transformers/all-mpnet-base-v2`).
- The required Python packages are listed in the `requirements.txt` file.

#### OR

- Docker installed on your machine. You can download and install Docker 
from the official Docker website: [https://www.docker.com/get-started](https://www.docker.com/get-started).

----

## Setup and Installation (Local)

1. Clone the repository:
    
```bash
git clone https://github.com/KirillFazi/tex_difficulty_level_en.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

*P.s. If you need to run it global, you have to change ip address and port.*

## Usage (Local)

1. Start the web service by running the following command:

```bash
python app/app.py
```
The service will be accessible at `http://0.0.0.0:8000/`.

2. Open your web browser and make GET request to `http://0.0.0.0:8000//subtitle_level/?subs={<Your_subtitels_text_her>}`.
Subtitles text have to be less long than 45_000 symbols.

3. You will get response looks like this - `{'subtitle_level': 'C1', 'confidence': 0.9517925977706909}`

*You can make GET request without browser. One way to do it, use `test_get_request.py` script in root dir of project*
------

## Setup and Installation (Docker)

1. Clone the repository:
    
```bash
git clone https://github.com/KirillFazi/jpn_eng_ocr_translator.git
```

2. Build the Docker image:

```bash
docker build -t subs_level .
```

## Usage (Docker)

1. Run the Docker container:

```bash
docker run -d --name subs_level -p 8000:8000 subs_level
```

2. Open your web browser and make GET request to `http://0.0.0.0:8000//subtitle_level/?subs={<Your_subtitels_text_her>}`.
Subtitles text have to be less long than 45_000 symbols.

3. You will get response looks like this - `{'subtitle_level': 'C1', 'confidence': 0.9517925977706909}`

*You can make GET request without browser. One way to do it, use `test_get_request.py` script in root dir of project*

## Project Structure

- `app/app.py`: The main script that runs the FastApi service.
- `app/prediction_core.py`: Module containing the prediction model and function to return prediction.
- `app/data_preprocessing.py`: Module containing the data preprocessing functions. 
- `static/movie_subs_level.csv`: Data to test app with GET request. 
- `test_get_request.py`: Python script to test app with GET request. 
- `app/model/saved_weights.pt`: Saved weights of trained model.

## Contributing

Contributions to this project are welcome. If you find any issues or 
have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

---------

---------

# NLP Subtitles difficulty level (english)

Разработать ML-решение для автоматического определения уровня сложности англоязычных фильмов. Просмотр фильмов 
на языке оригинала является популярным и эффективным методом изучения языка. Однако студентам бывает непросто 
для студентов выбрать фильмы, соответствующие их уровню владения языком. Как правило, преподаватель должен просмотреть фильм, чтобы определить его уровень сложности. 
чтобы определить уровень сложности фильма, что отнимает много времени. Для решения этой проблемы я разработал ML-решение, которое 
автоматически определяет уровень сложности англоязычных фильмов на основе их субтитров.

## Цель проекта

Наша цель - разработать ML-модель, позволяющую автоматически классифицировать англоязычные фильмы по четырем различным 
уровням сложности: A2, B1, B2 и C1. Эти уровни основаны на проценте диалогов, которые может понять студент, 
при этом A2 представляет собой самый низкий уровень (50-70% понимания), а C1 - самый высокий уровень 
(90-100% понимания). Такая классификация поможет изучающим язык выбрать фильмы, соответствующие их уровню владения языком 
и улучшить свои языковые навыки.

## Необходимые условия

- Python 3.6 или выше.
- Подключение к Интернету для доступа к модели перевода Hugging Face или 
локальная копия модели (`sentence-transformers/all-mpnet-base-v2`).
- Необходимые пакеты Python перечислены в файле `requirements.txt`.

#### ИЛИ

- На машине установлен Docker. Вы можете скачать и установить Docker 
с официального сайта Docker: [https://www.docker.com/get-started](https://www.docker.com/get-started).

----

## Настройка и установка (локально)

1. Клонируйте репозиторий:
    
```bash
git clone https://github.com/KirillFazi/tex_difficulty_level_en.git
```

2. Установите необходимые пакеты Python:

```bash
pip install -r requirements.txt
```

*P.s. Если необходимо запустить глобально, то необходимо изменить ip-адрес и порт.

## Использование (локально)

1. Запустите веб-сервис, выполнив следующую команду:

```bash
python app/app.py
```
Сервис будет доступен по адресу `http://0.0.0.0:8000/`.

2. Откройте веб-браузер и сделайте GET-запрос по адресу `http://0.0.0.0:8000//subtitle_level/?subs={<Ваш_субтитры_текст_гер>}`.
Длина текста субтитров не должна превышать 45_000 символов.

3. Вы получите ответ следующего вида - `{'subtitle_level': 'C1', 'confidence': 0.9517925977706909}`

*Вы можете сделать GET-запрос без браузера. Для этого можно использовать скрипт `test_get_request.py` в корневом каталоге проекта*.
------

## Настройка и установка (Docker)

1. Клонируем репозиторий:
    
```bash
git clone https://github.com/KirillFazi/jpn_eng_ocr_translator.git
```

2. Собрать образ Docker:

```bash
docker build -t subs_level .
```

## Использование (Docker)

1. Запустите контейнер Docker:

```bash
docker run -d --name subs_level -p 8000:8000 subs_level
```

2. Откройте веб-браузер и сделайте GET-запрос по адресу `http://0.0.0.0:8000//subtitle_level/?subs={<Ваш_субтитры_текст_гер>}`.
Текст субтитров должен быть не длиннее 45_000 символов.

3. Вы получите ответ следующего вида - `{'subtitle_level': 'C1', 'confidence': 0.9517925977706909}`

*Вы можете сделать GET-запрос без браузера. Для этого можно использовать скрипт `test_get_request.py` в корневом каталоге проекта*

## Структура проекта

- `app/app.py`: Основной скрипт, запускающий сервис FastApi.
- `app/prediction_core.py`: Модуль, содержащий модель предсказания и функцию, возвращающую предсказание.
- `app/data_preprocessing.py`: Модуль, содержащий функции предварительной обработки данных. 
- `static/movie_subs_level.csv`: Данные для тестирования приложения с помощью GET-запроса. 
- `test_get_request.py`: Python-скрипт для тестирования приложения с помощью GET-запроса. 
- `app/model/saved_weights.pt`: Сохраненные веса обученной модели.

## Вклад

Вклад в этот проект приветствуется. Если вы обнаружили какие-либо проблемы или 
предложения по улучшению, пожалуйста, откройте проблему или отправьте запрос на исправление (pull request) в репозитории GitHub.
