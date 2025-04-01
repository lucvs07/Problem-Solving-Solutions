from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions) # number of questions
        dp = [0] * (n + 1) # dp array to store max points
        
        # Iterate through the questions in reverse order
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i] # points for the question, brainpower to skip
            # Calculate the maximum points by either skipping the current question or answering it
            # If we answer the question, we add its points and the points from the next question we can answer
            dp[i] = max(dp[i + 1], points + (dp[i + brainpower + 1] if i + brainpower + 1 <= n else 0))
        return dp[0]