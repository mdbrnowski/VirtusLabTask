#!/usr/bin/env python

import click
from join.utils.join import join


@click.command()
@click.argument('file_1', type=click.Path(exists=True))
@click.argument('file_2', type=click.Path(exists=True))
@click.argument('column_name')
@click.argument('join_type', required=False, default='inner')
def main(file_1, file_2, column_name, join_type):
    if join_type not in ('inner', 'left', 'right'):
        raise click.BadParameter(message="JOIN_TYPE should be 'inner', 'left' or 'right'.")

    with open(file_1) as f:
        headers_1 = f.readline().strip().split(',')
    with open(file_2) as f:
        headers_2 = f.readline().strip().split(',')

    if join_type == 'right':
        join_type = 'left'
        file_1, file_2 = file_2, file_1

    if column_name not in headers_1 or column_name not in headers_2:
        raise click.BadParameter(message='COLUMN_NAME does not exist in one of the files.')

    join(file_1, file_2, headers_1.index(column_name), headers_2.index(column_name), join_type)


if __name__ == "__main__":
    main()
