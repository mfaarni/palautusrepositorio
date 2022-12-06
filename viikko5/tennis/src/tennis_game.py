class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0


    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        
        result = self.m_score1 - self.m_score2
        if result == 0:
            return self.even(
                self.m_score1
            )

        if self.m_score1 >=4 or self.m_score2 >= 4:
            return self.over_forty(result)

        else:
            return self.under_forty()

        

    def even(self, score):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }.get(score, "Deuce")

    
    def over_forty(self, score):
            
        if score == 1:
            return "Advantage player1"
        if score == -1:
            return "Advantage player2"
        if score >= 2:
            return "Win for player1"
        else:
            return "Win for player2"


    def under_forty(self):
        dictionary = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        return f"{dictionary.get(self.m_score1)}-{dictionary.get(self.m_score2)}"