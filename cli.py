#!/usr/bin/env python
import click
import pandas
from helpers import *
from constants import *
from extract import *
from report import *
from integrity import *


@click.group()
def cli():
    pass


@click.command()
def extract():
    # check if data extists, if so ask for confimation
    # Reload all data
    pass


@click.command()
@click.option('--slug', default=None, help='Slug of the report to update')
@click.option('--all', is_flag=True, help='Update all reports')
def update(slug, all=False):
    """This command updates a report"""
    if all and slug:
        click.echo('Either --all or --slug must be provided, not both.')
        return
    if all:
        for report_slug in report_slugs:
            print(f'Updating {report_slug}')
            update_report(report_slug)
    elif slug:
        update_report(slug)
    else:
        click.echo('Either --all or --slug must be provided.')


@click.command()
@click.argument('slug')
def review(slug):
    """This command reviews a report"""
    df = load_report_data(slug)
    review_data(df)
    pass


@click.command()
def load():
    """This command loads data"""
    # Your loading code here
    pass


cli.add_command(update)

cli.add_command(review)
cli.add_command(load)

if __name__ == "__main__":
    cli()
