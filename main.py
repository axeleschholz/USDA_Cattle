from retrieve import retrieve_data
import pandas

while __name__ == '__main__':
    slug = '2006'
    start = '01/1/2020'  # MM/DD/YYYY
    end = '02/29/2024'
    blob = retrieve_data(slug, start, end)
    df = pandas.DataFrame(blob)
    df.to_csv('output.csv', index=False)
    break
