from helpers import *
from constants import *
from extract import *

start = '01/1/2020'
end = '02/29/2024'

while __name__ == '__main__':
    for slug in REPORT_SLUGS:
        print(f'Retrieving {slug}')
        extract_report(slug, start, end)
