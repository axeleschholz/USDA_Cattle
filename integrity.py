
import pandas


def review_data(data):
    """Review dataframe and print out columns, datatypes, and null values. Also indicate any mixed types."""
    print(data.info())
    print(data.select_dtypes(include='object').map(type).eq(str).all().sum())
    print(data.select_dtypes(include='object').map(type).nunique())


def check_integrity(data):
    # if report_end_date is not datetime, convert it
    if data['report_end_date'].dtype != 'datetime64[ns]':
        data['report_end_date'] = pandas.to_datetime(data['report_end_date'])
    # if report_begin_date is not datetime, convert it
    if data['report_begin_date'].dtype != 'datetime64[ns]':
        data['report_begin_date'] = pandas.to_datetime(
            data['report_begin_date'])
    # if report_end_date is not in ascending order, sort it
    if not data['report_end_date'].is_monotonic_increasing:
        data = data.sort_values(by='report_end_date')

    # if final_inc is not represented by 0 or 1, convert it from 'Final'
    if data['final_inc'].dtype == 'object':
        data['final_inc'] = data['final_inc'].apply(
            lambda x: 1 if x == 'Final' else 0)
