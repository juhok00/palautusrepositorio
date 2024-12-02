class TennisGame:
    POINT_NAMES = ["Love","Fifteen","Thirty","Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score +=  1
        elif player_name ==self.player2_name:
            self.player2_score += 1

    def get_score(self):

        if self.tied():
            return self.tied_score()
        if self.endgame():
            return self.endgame_score()
        return self.normal_score()


    def tied(self):
        return self.player1_score==self.player2_score
    
    
    def endgame(self):
        return self.player1_score>= 4 or self.player2_score >= 4
    
    def tied_score(self):
        if self.player1_score>3:
            return "Deuce"
        return f"{self.POINT_NAMES[self.player1_score]}-All"

    
    def endgame_score(self):
        score_difference= self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >=2:
            return f"Win for {self.player1_name}"
        elif score_difference >=-2:
            return f"Win for {self.player2_name}"

    def normal_score(self):
        player1_score_name= self.POINT_NAMES[self.player1_score]
        player2_score_name= self.POINT_NAMES[self.player2_score]
        return f"{player1_score_name}-{player2_score_name}"