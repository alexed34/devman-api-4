import requests
import os
import urllib3

urllib3.disable_warnings()


def get_response(url, name):
    urll = f'{url}{name}'
    response = requests.get(urll)
    response.raise_for_status()
    return response.json()


def get_img_habbl(response):
    if not response:
        raise Exception('нет данных в json обьекте')
    return [i['id'] for i in response]


def get_photo(photo, response):
    image_files = response.get('image_files')
    url_photo = f"https:{image_files[-1]['file_url']}"
    file_extension = os.path.splitext(url_photo)[1]
    filename = f'{photo}{file_extension}'
    response = requests.get(url_photo, verify=False)
    response.raise_for_status()
    date = {'filname': filename,
            'response': response}
    return date


def write_photo(date, path):
    with open(os.path.join(path, date['filname']), 'wb') as file:
        file.write(date['response'].content)


def main():
    path = 'images'
    os.makedirs(path, exist_ok=True)
    url_images = 'https://hubblesite.org/api/v3/images/'
    name = 'wallpaper'
    response = get_response(url_images, name)
    photos_name = get_img_habbl(response)
    url_image = 'https://hubblesite.org/api/v3/image/'
    for photo in photos_name:
        response = get_response(url_image, photo)
        date = get_photo(photo, response)
        write_photo(date, path)


if __name__ == '__main__':
    main()
