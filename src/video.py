from src.channel import Channel

class Video():
    def __init__(self, id_video):
        youtube = Channel.get_service()
        try:
            video_request = youtube.videos().list(
                part='snippet,statistics',
                id=id_video
            )
            video_response = video_request.execute()
            if video_response['items'] == []:
                raise NoVideoError

        except NoVideoError as e:
            print('Видео с таким  ID  не существует')
            self.id_video = id_video
            self.title = None
            self.url = None
            self.views = None
            self.like_count = None

        else:
            self.id_video = id_video
            self.title = video_response['items'][0]['snippet']['title']
            self.url = f'https://www.youtube.com/video/{id_video}'
            self.views = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title
class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist


class NoVideoError(Exception):
    pass
