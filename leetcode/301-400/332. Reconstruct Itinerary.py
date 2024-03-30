from operator import itemgetter
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def find(tickets: List[List[str]], begin: str) -> List[str]:
            if len(tickets) == 1 and tickets[0][0] == begin:
                return tickets[0]


            ans = [begin]
            queue = []
            for i in range(len(tickets)):
                if tickets[i][0] == begin:
                    queue.append(tickets[i])

            if not queue:
                return []

            queue = sorted(queue, key= itemgetter(1) )

            for next in queue:
                remainder = tickets.copy()
                remainder.remove(next)
                res = find(remainder, next[1])
                if res:
                    ans.extend(res)
                    return ans

        return find(tickets, 'JFK')


if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
    print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))

