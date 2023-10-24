import bisect
import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        return [bisect.bisect_right(start, t) - bisect.bisect_left(end, t) for t in people]