import click
from update_tracker.utils import Level, PackageData

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
        HEADER = """\n\n[REPORT]\n""" + "-" * 80
        FORMAT = "{:<20}" * (len(PackageData._fields) + 1)
        click.echo(HEADER)
        for l in Level:
            if result[l.value - 1]:
                click.echo(f"**{l.name}**")
                click.echo(FORMAT.format('package_name', *PackageData._fields))
                for package_name, package_data in result[l.value - 1].items():
                    click.echo(FORMAT.format(package_name, *package_data))

            if self.level == l.name:
                break
    
    def print_error(self, error) -> None:
        HEADER = """\n**ERROR**"""
        FORMAT = "{:<20} {:<40}"
        click.echo(HEADER)
        click.echo(FORMAT.format('package_name', 'error_reason')) 
        for package_name, error_reason in error.items():
            click.echo(FORMAT.format(package_name, error_reason)) 
        click.echo("-" * 80)