#!/usr/bin/env python
import click
import pandas
from helpers import *
from constants import *
from extract import *
from report import update_report
from integrity import check_integrity_and_convert, review_data
from combine import combine_reports


@click.group()
def cli():
    pass


@click.command()
def extract():
    # check if data extists, if so ask for confimation
    # Reload all data
    pass


@click.command()
@click.argument('slug')
def update(slug):
    """Attempts to update a report with new data"""
    if slug == 'all':
        for report_slug in REPORT_SLUGS:
            print(f'Updating {report_slug}')
            update_report(report_slug)
    else:
        update_report(slug)


@click.command()
@click.argument('slug')
def review(slug):
    """Prints data on a report"""
    df = load_report_data(slug)
    review_data(df)


@click.command()
@click.argument('slug')
def convert(slug):
    """Checks the integrity of a report and converts it to the correct format"""
    if slug == 'all':
        for report_slug in REPORT_SLUGS:
            data = load_report_data(report_slug)
            data = check_integrity_and_convert(data)
            save_report_data(report_slug, data)
            print(f'Integrity check complete for {report_slug}')
    else:
        data = load_report_data(slug)
        data = check_integrity_and_convert(data)
        save_report_data(slug, data)
        print(f'Integrity check complete for {slug}')


@click.command()
def combine():
    """Loads all reports for analysis"""
    combine_reports()


cli.add_command(extract)
cli.add_command(update)
cli.add_command(review)
cli.add_command(convert)
cli.add_command(combine)

if __name__ == "__main__":
    cli()
