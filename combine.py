import pandas

report_slugs = [2006, 2056, 1907, 1704, 1933, 2041, 1976, 2167, 1895, 2193, 1821, 2111, 1778, 1860, 1784, 2091, 2100, 1831, 1919, 1963, 2027, 2063, 1955, 2039, 2187, 2240, 2106,]

df = pandas.DataFrame()

for slug in report_slugs:
    temp_df = pandas.read_csv(f'raw_summary_data/{slug}_data.csv')
    df = pandas.concat([df, temp_df])

df.to_csv('fulldata.csv', index=False)

    
