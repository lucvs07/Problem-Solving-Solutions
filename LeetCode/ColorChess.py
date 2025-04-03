class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        c1 = coordinates[0]
        c2 = coordinates[1]
        if c1 in ['a', 'c', 'e', 'g'] and c2 in ['1', '3', '5', '7'] :
            return False
        if c1 in ['b', 'd', 'f', 'h'] and c2 in ['2', '4', '6', '8']:
            return False
        return True
        