from src.channel import Channel
import isodate, datetime

class PlayList():

    def __init__(self, playlist_id):
        youtube = Channel.get_service()
        playlist_request = youtube.playlists().list(
            part='snippet',
            id=playlist_id,
            maxResults=50
        )
        playlist_response = playlist_request.execute()
        self.playlist_id = playlist_id
        self.title = playlist_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'
        PlayList.total_duration(self)
    def total_duration(self):
        total_duration = datetime.timedelta()
        youtube = Channel.get_service()
        playlistitems_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=self.playlist_id,
            maxResults=50
        )
        playlistitems_response = playlistitems_request.execute()
        for item in playlistitems_response['items']:
            video_id = item['contentDetails']['videoId']
            youtube = Channel.get_service()
            video_request = youtube.videos().list(
                part='contentDetails',
                id=video_id
            )
            video_response = video_request.execute()
            video_duration_timedelta = isodate.parse_duration(video_response['items'][0]['contentDetails']['duration'])
            total_duration += video_duration_timedelta
        self.total_duration = total_duration
        return self.total_duration

    def show_best_video(self):
        youtube = Channel.get_service()
        playlistitems_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=self.playlist_id,
            maxResults=50
        )
        playlistitems_response = playlistitems_request.execute()

        top_likes = 0

        for item in playlistitems_response['items']:
            video_id = item['contentDetails']['videoId']

            youtube = Channel.get_service()
            video_request = youtube.videos().list(
                part='statistics',
                id=video_id
            )
            video_response = video_request.execute()
            if int(video_response['items'][0]['statistics']['likeCount']) > top_likes:
                top_likes = int(video_response['items'][0]['statistics']['likeCount'])

                best_video = f'https://youtu.be/{video_id}'
        return best_video