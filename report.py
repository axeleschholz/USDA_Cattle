from helpers import *
from constants import *
from extract import *
import pandas
import sys
import datetime


def update_report(slug):
    try:
        data = load_report_data(slug)
    except:
        print(f"Data for report {slug} does not exist")
        sys.exit(1)

    # get the last date in the data
    last_report_date = data['report_end_date'].max()
    start_date = last_report_date.strftime('%m/%d/%Y')
    print(f"Last date in data: {start_date}")

    # get the current date
    current_date = datetime.datetime.now().strftime('%m/%d/%Y')
    print(f"Current date: {current_date}")

    # extracting new data
    print(f"Extracting new data for report {slug}")
    # new_data = extract_report(slug, start_date, current_date)

    # new_data['report_end_date'] = pandas.to_datetime(new_data['report_end_date'])
