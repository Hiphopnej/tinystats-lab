import click
from .core import mean as mean_fn, median as median_fn

@click.group()
def cli():
    """tinystats command-line interface."""

@cli.command()
@click.argument("numbers", nargs=-1, type=float)
def mean(numbers):
    """Compute the mean of NUMBERS."""
    if not numbers:
        raise click.UsageError("Provide at least one number")
    click.echo(str(mean_fn(numbers)))

@cli.command()
@click.argument("numbers", nargs=-1, type=float)
def median(numbers):
    """Compute the median of NUMBERS."""
    if not numbers:
        raise click.UsageError("Provide at least one number")
    click.echo(str(median_fn(numbers)))
