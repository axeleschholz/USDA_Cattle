import requests
import json


def retrieve_data(slug, start_date, end_date):
    url = f'https://mymarketnews.ams.usda.gov/public_data/ajax-search-data-by-report/{slug}?q=report_begin_date={start_date}:{end_date}'
    response = requests.get(url)
    data = response.json()
    rows = data['results']
    return rows
