import requests
import os
import urllib3

urllib3.disable_warnings()


def get_img_habbl(name):
    url = f'https://hubblesite.org/api/v3/images/{name}'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    if not response:
        raise requests.exceptions.HTTPError('нет данных в json обьекте')

    photos = [i['id'] for i in response]
    counter_foto = len(photos)
    path = 'images'
    os.makedirs(path, exist_ok=True)
    for photo in photos:
        url = f'https://hubblesite.org/api/v3/image/{photo}'
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        image_files = response.get('image_files')
        url_photo = f"https:{image_files[-1]['file_url']}"
        file_extension = os.path.splitext(url_photo)[1]
        filname = f'{photo}{file_extension}'
        response = requests.get(url_photo, verify=False)
        response.raise_for_status()
        with open(os.path.join(path, filname), 'wb') as file:
            file.write(response.content)
        counter_foto -= 1
        print(f'Осталось скачать: {counter_foto} фото ')


def main():
    get_img_habbl('wallpaper')


if __name__ == '__main__':
    main()
