class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1a = coordinate1[0]
        c1b = coordinate1[1]
        c2a = coordinate2[0]
        c2b = coordinate2[1]
        color_1 = True
        color_2 = True

        if c1a in ['a', 'c', 'e', 'g'] and c1b in ['1', '3', '5', '7'] :
            color_1 = False
        if c1a in ['b', 'd', 'f', 'h'] and c1b in ['2', '4', '6', '8']:
            color_1 = False
        if c2a in ['a', 'c', 'e', 'g'] and c2b in ['1', '3', '5', '7'] :
            color_2 = False
        if c2a in ['b', 'd', 'f', 'h'] and c2b in ['2', '4', '6', '8']:
            color_2 = False
        
        if color_1 == color_2:
            return True
        else :
            return False