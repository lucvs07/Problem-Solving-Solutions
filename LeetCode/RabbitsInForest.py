class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash_map = {}
        for ans in answers :
            if ans in hash_map :
                hash_map[ans] += 1
            else :
                hash_map[ans] = 1
        
        res = 0
        for num in hash_map :
            res += ceil(float(hash_map[num]) / (num + 1)) * (num + 1)
        
        return int(res)
