class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

    def get_score_tie(self):
        if self.player1_score < 3:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"
        return "Deuce"
    
    def get_score_advantage_or_win(self):
        difference_in_scores = self.player1_score - self.player2_score

        if difference_in_scores == 1:
            return f"Advantage {self.player1_name}"
        elif difference_in_scores == -1:
            return f"Advantage {self.player2_name}"
        elif difference_in_scores >= 2:
            return f"Win for {self.player1_name}"
        elif difference_in_scores <= -2:
            return f"Win for {self.player2_name}"
        
    def get_score_current(self):
        player1_score_name = self.SCORE_NAMES[self.player1_score]
        player2_score_name = self.SCORE_NAMES[self.player2_score]
        return f"{player1_score_name}-{player2_score_name}"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_score_tie()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_score_advantage_or_win()
        else:
            return self.get_score_current()
