import os
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd

from argparse import ArgumentParser
from dotenv import load_dotenv
from sqlalchemy import create_engine

parser = ArgumentParser(description="Collect Youtube Comments")
parser.add_argument('--videoid', type=str, default='mBoX_JCKZTE', help='The ID of the YouTube Video')
args = parser.parse_args()

load_dotenv()
developer_key = os.getenv('DEVELOPER_KEY')
api_service_name = os.getenv('API_SERVICE_NAME')
api_version = os.getenv('API_VERSION')
db_name = os.getenv('DB_NAME')

def extract():
    print('==> EXTRACT')

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)
    request = youtube.commentThreads().list(
        part='snippet',
        maxResults=100,
        order="relevance",
        videoId=args.videoid
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
    print('==> LOAD SERVER')
    df = pd.DataFrame(list_data)
    df.to_csv(file_path, index=False)

def load_db(list_data, table_name):
    print('==> LOAD SERVER')
    database_location =f'sqlite:///database/{db_name}.sqlite'
    engine = create_engine(database_location)

    df = pd.DataFrame(list_data)
    df['inserted_at'] = pd.Timestamp.now()

    df.to_sql(table_name, engine, index=False, if_exists='append')

if __name__ == '__main__':
    file_name = 'youtube'
    file_path = os.path.join('.', 'server_outputs', f'{file_name}.csv')

    # Extraccion
    dict_extracted = extract()

    # Transformacion
    list_transformed = transform(dict_extracted)

    # Carga
    load_server(list_transformed, file_path)
    load_db(list_transformed, table_name=file_name)
