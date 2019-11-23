import requests
import os
import urllib3

urllib3.disable_warnings()

def get_response(url, name):
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    return response.get(name)


def write_photo(date, path):
    with open(os.path.join(path, date['filname']), 'wb') as file:
        file.write(date['response'].content)


def main():
    path = 'images'
    os.makedirs(path, exist_ok=True)
    url = 'https://api.spacexdata.com/v3/launches/latest?filter=links/flickr_images'
    name = 'links'
    links = get_response(url, name)
    flickr_images = links.get('flickr_images')
    if not flickr_images:
        raise requests.exceptions.HTTPError('в последнем запуске нет фото ')
    for number, url in enumerate(flickr_images, 1):
        response = requests.get(url)
        response.raise_for_status()
        filname = f'spacex{number}.jpg'
        date = {'response': response,
                'filname': filname}
        write_photo(date, path)


if __name__ == '__main__':
    main()
