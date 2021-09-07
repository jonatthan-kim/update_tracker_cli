import click
from update_tracker.utils import Level

class Printer():
    def __init__(self, verbose, level) -> None:
        self.verbose = verbose
        self.level = level
        self.longest_package_name = 0

    def make_output(self, result, error) -> None:
        self.print_package_report(result)
        if error:
            self.print_error(error)      
    
    def print_package_report(self, result) -> None:
        for l in Level:
            click.echo(f"{l.name}: {result[l.value - 1].keys()}")
            if self.level == l.name:
                break
    
    def print_error(self, error) -> None:
        HEADER = """[ERROR]\n--------------------------"""
        FORMAT = "{:<15} {:<40}"
        click.echo(HEADER)
        click.echo(FORMAT.format('package_name', 'error_reason')) 
        for package_name, error_reason in error.items():
            click.echo(FORMAT.format(package_name, error_reason)) 