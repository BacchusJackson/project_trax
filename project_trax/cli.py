"""Console script for project_trax."""
import sys
import click
from project_trax.trax_shell import TraxShell


@click.command()
def main(args=None):
    """Console script for project_trax."""
    shell = TraxShell()
    shell.cmdloop()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
