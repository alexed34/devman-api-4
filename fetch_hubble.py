import requests
import os
import urllib3
urllib3.disable_warnings()


def get_img_habbl(name): # создаем список фото из коллекции hubblesite и скачиваем их
  url = f'https://hubblesite.org/api/v3/images/{name}'
  response = requests.get(url).json()
  list_id = [i['id'] for i in response]
  print(list_id)
  print(len(list_id))
  sc = len(list_id)
  path = 'images'
  if  not os.path.exists(path):
    os.makedirs(path)
  for id in list_id: # скачиваем картинки  с hubblesite по номеру фото
    url = f'https://hubblesite.org/api/v3/image/{id}'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    image_files = response.get('image_files')
    url_photo = f"https:{image_files[-1]['file_url']}"
    file_extension = url_photo.split('.')[-1]
    filname = f'{id}.{file_extension}'
    response = requests.get(url_photo, verify=False)
    response.raise_for_status()
    with open(os.path.join(path, filname), 'wb') as file:
      file.write(response.content)
    sc -= 1
    print(sc) # отслеживание оставшихся фото
    
def main():
  get_img_habbl('wallpaper')

if __name__ == '__main__':
    main()

