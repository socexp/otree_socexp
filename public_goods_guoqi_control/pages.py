from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from decimal import * 
import time

class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return self.round_number == 1

class Contribute(Page):
    """Player: Choose how much to contribute"""
    # this is an attribute
    timeout_seconds = 60
    form_model = 'player'
    form_fields = ['contribution']	
     

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "请等待其他参与者做出贡献。"


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        return {
            'total_earnings': round(float(self.group.total_contribution.quantize(Decimal('0.0'))), 2) * Constants.multiplier,
			'own_holdings': round(float((self.player.payoff-self.group.individual_share).quantize(Decimal('0.0'))), 2),
			'contribution':round(float(self.player.contribution.quantize(Decimal('0.0'))), 2),
			'total_contribution':round(float(self.group.total_contribution.quantize(Decimal('0.0'))), 2),
			'individual_share':round(float(self.group.individual_share.quantize(Decimal('0.0'))), 2),
			'payoff':round(float(self.player.payoff.quantize(Decimal('0.0'))), 2)
		
        }


class ResultsSummary(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'total_payoff': sum(
                [round(float(p.payoff.quantize(Decimal('0.0'))), 2) for p in player_in_all_rounds]),
			'total_payoff_rmb': sum(
                [p.payoff for p in player_in_all_rounds])*0.2,	
            'player_in_all_rounds': player_in_all_rounds,
        }
		
page_sequence = [Introduction,Contribute,ResultsWaitPage,Results,ResultsSummary]
