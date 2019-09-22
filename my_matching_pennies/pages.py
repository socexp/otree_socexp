from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):
    form_model = 'player'
    form_fields = ['penny_side']

    def vars_for_template(self):
        return dict(
            player_in_previous_rounds = self.player.in_previous_rounds()
        )


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class ResultsSummary(Page):
    
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]