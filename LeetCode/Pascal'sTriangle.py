class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0 :
                res.append([1])
            else :
                row = [1]
                prev_row = res[i-1]
                for j in range(1, i):
                    row.append(prev_row[j-1] + prev_row[j])
                row.append(1)
                res.append(row)
        return res
        
