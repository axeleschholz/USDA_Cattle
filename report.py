from helpers import *
from constants import *
from extract import *
from integrity import *
import pandas
import sys
import datetime


def update_report(slug):

    data = load_report_data(slug)

    # get the last date in the data
    last_report_date = pandas.to_datetime(data['report_end_date']).max()
    start_date = last_report_date.strftime('%m/%d/%Y')
    print(f"Last date in data: {start_date}")

    # get the current date
    current_date = datetime.datetime.now().strftime('%m/%d/%Y')
    print(f"Current date: {current_date}")

    # extracting new data
    print(f"Extracting new data for report {slug}")
    new_data = extract_report(slug, start_date, current_date)
    if new_data.empty:
        print(f"Report {slug} is up to date: no new data to extract")
        sys.exit(0)
    new_data = check_integrity_and_convert(new_data)

    # append new data to existing data, but only after the last date
    new_data = new_data[new_data['report_end_date'] > last_report_date]
    data = pandas.concat([data, new_data], ignore_index=True)
    data = check_integrity_and_convert(data)
    print("REMEMBER THIS ISN'T SAVING THE DATA")
    # save_report_data(slug, data)
