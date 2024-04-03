import pandas
from constants import *
from helpers import *


def combine_reports():
    df = pandas.DataFrame()
    for slug in REPORT_SLUGS:
        print(f'Adding {slug}')
        temp_df = load_report_data(slug)
        temp_df = temp_df.drop(EXCLUDED_COLUMNS, axis=1)
        df = pandas.concat([df, temp_df])

    print('Writing to fulldata.csv')
    df.to_csv('fulldata.csv', index=False)
