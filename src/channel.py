import json
import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str, title: str, description: str, url: str, subscribers: int, video: int, views: int) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = title
        self.description = description
        self.url = url
        self.subscribers = subscribers
        self.video = video
        self.views = views

    @classmethod
    def get_service(cls):
        channel_id = 'UCt_Sgcd_wTB8qiGym1lkgGg'
        request = youtube.channels().list(
            part='snippet',
            id=channel_id
        )
        response = request.execute()


        # extract channel title from response data
        items = response.get('items', [])
        title = items[0]['snippet']['title']
        description = items[0]['snippet']['description']
        url = f'https://www.youtube.com/channel/{channel_id}'

        request = youtube.channels().list(
            part='statistics',
            id=channel_id
        )
        response = request.execute()
        items = response.get('items', [])
        subscribers = items[0]['statistics']['subscriberCount']
        video = items[0]['statistics']['videoCount']
        views = items[0]['statistics']['viewCount']
        print(title, description, url, subscribers, video, views)
        return cls(channel_id, title, description, url, subscribers, video, views)
    def to_json(self, filename):
        data = {
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscribers': self.subscribers,
            'number of videos': self.video,
            'total views': self.views,
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj(channel)
