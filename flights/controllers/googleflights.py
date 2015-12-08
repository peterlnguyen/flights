from apiclient.discovery import build
config = open('../config/api-key.json')
QPX_API_SERVICE_NAME = 'qpxexpress'
QPX_API_KEY = config.developer_key
QPX_API_VERSION = 'v1'

qpx_client = build(QPX_API_SERVICE_NAME, QPX_API_VERSION, developerKey=QPX_API_KEY)

def search_flights(query):
    qpx_client.search().list().execute()
    return 'Fizzbuzz'


