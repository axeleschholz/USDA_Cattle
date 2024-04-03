import pandas
import requests
import sys


def retrieve_data_raw(slug, start_date, end_date):
    url = f'https://marsapi.ams.usda.gov/services/v1.2/reports/{slug}?q=report_begin_date={start_date}:{end_date}'
    response = requests.get(url, auth=('7XWk8PBs9+OacpqUItFCYTpfnq8yCqSS', ''))
    data = response.json()
    return data


def retrieve_report_instances(report, month, year):
    url = f'https://mymarketnews.ams.usda.gov/get_previous_release/{report}?type=month&month={month}&year={year}'
    response = requests.get(url)
    data = response.json().get('data')
    return data


def load_report_data(slug):
    try:
        data = pandas.read_csv(f'data_silos/{slug}_data.csv')
    except:
        print(f"Data for report {slug} does not exist")
        sys.exit(1)

    return data


def save_report_data(slug, data: pandas.DataFrame):
    data.to_csv(f'data_silos/{slug}_data.csv', index=False)


def load_report_instances(report):
    return pandas.read_csv(f'ams_reports/{report}_reports.csv')
