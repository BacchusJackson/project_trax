import click
from prettytable import PrettyTable


class Hero():
    def __init__(self, name=None):
        self.name = name or click.prompt('Character Name')
        self.pro_bonus = 2
        self.abilities = []
        self.skills = []

    def add_proficiency(self, skill):
        if not skill.proficiency:
            skill.proficiency = True
            skill.add_proficiency(self.pro_bonus)

    @property
    def abilities_table(self):
        tbl = PrettyTable()
        tbl.field_names = ['Ability', 'Score', 'Modifier']
        for ability in self.abilities:
            tbl.add_row([ability.name, ability.score, ability.mod_str])
        tbl.align['Ability'] = 'l'
        return tbl

    @property
    def skills_table(self):
        tbl = PrettyTable()
        tbl.field_names = ['Skill', 'Modifier']
        for skill in self.skills:
            tbl.add_row([skill.name, skill.mod_str])
        tbl.align['Skill'] = 'l'
        return tbl
    @property
    def all_abilities(self):
        x = ''
        for ability in self.abilities:
            x += ability.__str__() + '\n'
        return x

    @property
    def all_skills(self):
        x = ''
        for skill in self.skills:
            x += skill.__str__() + '\n'
        return x

class Ability():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def mod(self):
        return (self.score - 10) // 2

    @property
    def mod_str(self):
        if self.mod >= 0:
            return f'+{self.mod}'
        else:
            return f'-{self.mod}'

    def __str__(self):
        return f'{self.name} {self.score} ({self.mod_str})'


class Skill():

    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
        self.effects = []
        self.proficiency = False

    def add_effect(self, name, value):
        e = self.Effect(name, value)
        self.effects.append(e)

    def add_proficiency(self, value):
        self.add_effect('proficiency', value)

    @property
    def mod(self):
        mod_total = 0
        for effect in self.effects:
            mod_total += effect.modifer
        return self.ability.mod + mod_total

    @property
    def mod_str(self):
        if self.mod >= 0:
            return f'+{self.mod}'
        else:
            return f'-{self.mod}'

    class Effect():
        def __init__(self, name, modifer):
            self.name = name
            self.modifer = modifer

    def __str__(self):
        p = '*' if self.proficiency else ''
        return f'{self.name} [{self.ability.name}] ({self.mod_str}){p}'


class DefaultHero(Hero):
    def __init__(self, name=None):
        Hero.__init__(self, name)
        self.strength = Ability('Strength', 18)
        self.dexterity = Ability('Dexterity', 16)
        self.intelligence = Ability('Intelligence', 16)
        self.wisdom = Ability('Wisdom', 12)
        self.charisma = Ability('Charisma', 12)
        self.constitution = Ability('Constitution', 10)
        self.abilities = [self.strength, self.dexterity,
                          self.intelligence, self.wisdom,
                          self.charisma, self.constitution]

        self.perception = Skill('Perception', self.wisdom)
        self.stealth = Skill('Stealth', self.dexterity)
        self.skills = [self.perception, self.stealth]


