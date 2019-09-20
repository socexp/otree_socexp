from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'TL'

doc = """
A simple public goods game for learning purposes
"""


class Constants(BaseConstants):
    name_in_url = 'my_public_goods'
    players_per_group = 3
    num_rounds = 1
    endowment = c(1000)
    multiplier  = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, 
        max=Constants.endowment, 
        label="Please decide how much you want to contribute"
    )
