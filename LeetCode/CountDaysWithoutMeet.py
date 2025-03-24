from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        free = 0
        end = 0

        meetings.sort()

        for st, ed in meetings:
            if st > end + 1 :
                free += st - end - 1
            end = max(end, ed)
        free += days - end

        return free
