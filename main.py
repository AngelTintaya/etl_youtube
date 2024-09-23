import os
import googleapiclient.discovery
import googleapiclient.errors
import configparser
import pandas as pd

from dotenv import load_dotenv

load_dotenv()
developer_key = os.getenv('DEVELOPER_KEY')
api_service_name = os.getenv('API_SERVICE_NAME')
api_version = os.getenv('API_VERSION')

def extract():
    print('==> EXTRACT')

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)
    request = youtube.commentThreads().list(
        part='snippet',
        maxResults=100,
        order="relevance",
        videoId='mBoX_JCKZTE'
        )
    response = request.execute()

    return response

def transform(dict_data):
    print('==> TRANSFORM')
    list_dict = list()

    for item in dict_data['items']:
        comment = item['snippet']['topLevelComment']['snippet']

        dict_tweet = {
            'author': comment['authorDisplayName'],
            'published_at': comment['publishedAt'],
            'updated_at': comment['updatedAt'],
            'like_count': comment['likeCount'],
            'text': comment['textDisplay'],
        }

        list_dict.append(dict_tweet)
    
    return list_dict

def load_server(list_data, file_path):
    print('==> LOAD')
    df = pd.DataFrame(list_data)
    df.to_csv(file_path, index=False)

if __name__ == '__main__':
    file_path = os.path.join('.', 'server_outputs', 'youtube.csv')

    # Extraccion
    dict_extracted = extract()

    # Transformacion
    list_transformed = transform(dict_extracted)

    # Carga
    load_server(list_transformed, file_path)