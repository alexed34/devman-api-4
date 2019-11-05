###1. Короткое описание проекта
Скачивание фото с двух сайтов hubblesite.org, spacexdata.com и публикация их в инстаграм.
###2 Описание файлов
fetch_hubble.py - скачивает  фото из коллекции hubblesite (wallpaper, news и т.д) в папку images
fetch_spacex.py - скачивает  фото последних запусков spacex в папку images
main.py - обрезает фото до квадратного вида и публикует в инстаграм
###3 Требования к окружению
Python 3
###4 Как установить
запишите в файл .env данные инстаграма username=ваш_логин и password=ваш_пароль
Python3 должен быть уже установлен. Затем используйте pip(или pip3, если есть конфликт с Python2) для установки зависимостей:

pip install -r requirements.txt