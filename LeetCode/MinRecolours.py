class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        moves = 0
        whites = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                whites += 1
        moves = whites
        for i in range(k, n):
            if blocks[i - k] == 'W':
                whites -= 1
            if blocks[i] == 'W':
                whites += 1
            moves = min(moves, whites)
        return moves
