import json
import sys
import os
from googleapiclient.discovery import build
import config
from tqdm import tqdm

def youtube_data(api_key, video_id):
    service = build("youtube", "v3", developerKey=api_key)
    result = service.videos().list(part='snippet', id=video_id).execute()
    return result

if __name__ == '__main__':
    video_ids_file = sys.argv[1]
    my_api_key = config.api_key

    if not os.path.exists('youtube_data'):
        os.makedirs('youtube_data')
        
    with open(video_ids_file) as f:
        video_ids = f.readlines()
        for video_id in tqdm(video_ids):
            result = youtube_data(my_api_key, video_id)
            with open('youtube_data/' + video_id + '.json', 'w') as f:
                json.dump(result, f)
