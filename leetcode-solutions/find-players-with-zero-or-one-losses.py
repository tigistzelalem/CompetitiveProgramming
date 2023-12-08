class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)

        for match in matches:
            winner, loser = match
            losses[loser] += 1
        all_players = set(player for match in matches for player in match)
        no_losses = [player for player in all_players if losses[player] == 0]
        one_loss = [player for player in all_players if losses[player] == 1]

       
        no_losses.sort()
        one_loss.sort()

        return [no_losses, one_loss]
    


        
      

        
