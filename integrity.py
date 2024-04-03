import json
import pandas
import sys
from constants import *

ENCODING_FLAG = False  # whether to potentially rewrite encodings


def review_data(data):
    """Review dataframe and print out columns, datatypes, and null values. Also indicate any mixed types."""
    print(data.info())
    print(data.select_dtypes(include='object').map(type).eq(str).all().sum())

    # object_columns = data.select_dtypes(include='object')
    # for column in object_columns.columns:
    #     unique_types = object_columns[column].apply(type).unique()
    #     labels, uniques = pandas.factorize(object_columns[column])
    #     print(f"  Factorized: {uniques}")
    #     if len(unique_types) > 1:
    #         print(f"Column '{column}' has multiple types:")
    #         for unique_type in unique_types:
    #             example_value = object_columns[column][object_columns[column].apply(
    #                 type) == unique_type].iloc[0]
    #             print(f"  Type {unique_type} example: {example_value}")


def encode_objects(data):
    """Encode object columns to integers. Save encodings to file."""
    try:
        with open('encodings.json') as f:
            encodings = json.load(f)
    except FileNotFoundError:
        if ENCODING_FLAG:
            encodings = {}
        else:
            print("No encodings file found. Exiting.")
            sys.exit(1)

    if (len(encodings)) > 0 and ENCODING_FLAG:
        for column in data.select_dtypes(include='object').columns:
            if column in EXCLUDED_COLUMNS:
                continue
            data[column], uniques = pandas.factorize(data[column])
            encodings[column] = uniques.tolist()
            data[column] = data[column].where(
                pandas.notnull(data[column]), None)
            data[column] = data[column].astype('Int64')
        with open('encodings.json', 'w') as f:
            json.dump(encodings, f)
    else:
        for column in data.select_dtypes(include='object').columns:
            if column in encodings and column not in EXCLUDED_COLUMNS:
                data[column] = data[column].map(
                    lambda x: {value: key for key, value in enumerate(encodings[column])}.get(x) if pandas.notna(x) else None)
                data[column] = data[column].astype('Int64')

    return data


def check_integrity_and_convert(data):
    if list(data.columns) != STORED_COLUMNS:
        print("FATAL ERROR: Shape does not match")
        sys.exit(1)
    # convert dates
    for column in data.columns:
        if 'date' in column:
            data[column] = pandas.to_datetime(data[column])

    # if report_end_date is not in ascending order, sort it
    if not data['report_end_date'].is_monotonic_increasing:
        data = data.sort_values(by='report_end_date')

    # if final_inc is not represented by 0 or 1, convert it from 'Final'
    if data['final_ind'].dtype == 'object':
        data['final_ind'] = data['final_ind'].apply(
            lambda x: 1 if x == 'Final' else 0)

    # factorize object columns
    data = encode_objects(data)

    return data
