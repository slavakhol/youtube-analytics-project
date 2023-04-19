from src.channel import Channel
class Video():
    def __init__(self, id_video):
        youtube = Channel.get_service()
        video_request = youtube.videos().list(
            part='snippet,statistics',
            id=id_video
        )
        video_response = video_request.execute()
        self.id_video = id_video
        self.title = video_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/video/{id_video}'
        self.views = video_response['items'][0]['statistics']['viewCount']
        self.likes = video_response['items'][0]['statistics']['likeCount']
    def __str__(self):
        return self.title
class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist