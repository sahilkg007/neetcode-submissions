import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [[-cnt, char] for cnt, char in [
            (a, 'a'), (b, 'b'), (c, 'c')
        ] if cnt > 0]

        heapq.heapify(heap)

        res = []

        while heap:
            cnt, char = heapq.heappop(heap)

            # Can't put 3 same characters together
            if len(res) >= 2 and res[-1] == char and res[-2] == char:

                # No other character available
                if not heap:
                    break

                # Take second most frequent character
                cnt2, char2 = heapq.heappop(heap)

                res.append(char2)
                cnt2 += 1

                if cnt2 != 0:
                    heapq.heappush(heap, [cnt2, char2])

                # Put original character back
                heapq.heappush(heap, [cnt, char])

            else:
                res.append(char)
                cnt += 1

                if cnt != 0:
                    heapq.heappush(heap, [cnt, char])

        return ''.join(res)