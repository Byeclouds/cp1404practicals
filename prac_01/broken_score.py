"""
Rewrite the following program using the most efficient if, elif, else structure
you can. The code is available here at: broken_score.py

Remember to click Raw before copying and pasting so that you get proper
formatting!

The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent; 50 or more is a pass; below 50 is bad.

Be very careful of your boundary conditions... and test systematically.
"""

MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50
score = float(input("Enter score: "))
if score < 0 or score > MAX_SCORE:
    message = "Invalid score"
elif score >= EXCELLENT_SCORE:
    message = "Excellent"
elif score >= PASS_SCORE:
    message = "Passable"
else:
    message = "Bad"
print(message)
