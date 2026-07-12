class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        return [ranks[x] for x in arr]
        