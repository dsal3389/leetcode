from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses_track = defaultdict(int)
        players = set()

        for winner, loser in matches:
            loses_track[loser] += 1
            players.add(winner)
            players.add(loser)

        answer = [[], []]

        for player in sorted(players):
            if player not in loses_track:
                answer[0].append(player)
            elif loses_track[player] == 1:
                answer[1].append(player)
        return answer
