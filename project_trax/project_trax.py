"""Main module."""
import click
from cmd import Cmd
from project_trax.object_manager import ObjectManager


class TraxShell(Cmd):
    intro = 'welcome to Trax shell. Type help or ? to list commands.\n'
    prompt = '(trax) ~> '
    oManager = ObjectManager()

    def do_exit(self, arg):
        """Exits the Shell"""
        click.echo('See you later!')
        return True

    def do_add(self, arg):
        """Add an something to Trax (hero, feature, etc.)"""
        try:
            self.oManager.add(arg)
            click.secho('done!', fg='green')
        except KeyError:
            click.secho('That object type does not exist', err=True, fg='red')

    def do_heros(self, arg):
        """Print all of the saved Heros"""
        for key, value in self.oManager.heros.items():
            print(key)

    def do_activate(self, arg):
        """Activate a specfic Hero by name"""
        hero = self.oManager.heros.get(arg)
        if not hero:
            click.echo("Hero not found...  Use: 'heros' to see list")
        else:
            hShell = HeroShell()
            hShell.load_hero(hero)
            hShell.cmdloop()

    def default(self, arg):
        click.secho(f'*** Uknown syntax: {arg}', fg='red')


class HeroShell(Cmd):

    def load_hero(self, hero):
        self.hero = hero
        self.prompt = f'(trax:{self.hero.name}) ~> '

    def do_abilities(self, arg):
        click.echo(self.hero.abilities_table)

    def do_exit(self):
        return True
