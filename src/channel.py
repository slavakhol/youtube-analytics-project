import json
import os
from googleapiclient.discovery import build

channel_id = 'UCt_Sgcd_wTB8qiGym1lkgGg'

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Channel:
    """Класс для ютуб-канала"""
    __api_key: str = os.getenv('YOUTUBE_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        youtube = Channel.get_service()
        # youtube = build('youtube', 'v3', developerKey=Channel.__api_key)
        request = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        )
        self.response = request.execute()
        items = self.response.get('items', [])

        self.__channel_id = channel_id
        self.title = items[0]['snippet']['title']
        self.description = items[0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscribers = items[0]['statistics']['subscriberCount']
        self.video = items[0]['statistics']['videoCount']
        self.views = items[0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=Channel.__api_key)
        return youtube

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
        # channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj(self.response)
