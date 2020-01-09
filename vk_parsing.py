import csv
import requests

token = 'e9d4c7b7e9d4c7b7e9d4c7b75de9ba3c56ee9d4e9d4c7b7b7c019dc9b1823749b24c2b3'
version = '5.103'
domain = 'fit4life_official'
count = 100
all_posts = []


def take_1000_posts(offset=0):
    while offset <= 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        all_posts.extend(data)
        offset += 100
    return all_posts


def file_writer(all_posts):
    with open('fit4life.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in all_posts:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                img_url = 'pass'
            a_pen.writerow((post['likes']['count'], post['text'], img_url))


if __name__ == '__main__':
    # получаем все посты
    all_posts = take_1000_posts()

    # записываем в файл csv
    file_writer(all_posts)
