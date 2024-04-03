from helpers import *
from constants import *
import pandas


def extract_report(slug, start, end):
    blob = retrieve_data_raw(slug, start, end)
    df = pandas.DataFrame(blob['results'])
    df = df.drop(DROPPED_ATTRIBUTES, axis=1)
    df['report_end_date'] = pandas.to_datetime(df['report_end_date'])
    df['report_begin_date'] = pandas.to_datetime(df['report_begin_date'])
    return df
