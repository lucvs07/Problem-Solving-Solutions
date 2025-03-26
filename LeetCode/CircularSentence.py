class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(" ")
        print(arr)
        n = len(arr)
        j = 0
        if n == 1 :
            if arr[0][0] == arr[0][-1]:
                return True
            else :
                return False
        else :
            if arr[0][0] != arr[-1][-1]:
                return False
            while j < n - 1:
                if arr[j][-1] != arr[j+1][0]:
                    return False
                j += 1
        return True
        