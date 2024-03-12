"""
Given an array of n names arr of candidates in an election, where each name is a string of lowercase characters. A candidate name in the array represents a vote casted to the candidate. Print the name of the candidate that received the maximum count of votes. If there is a draw between two candidates, then print lexicographically smaller name.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

You only need to complete the function winner() that takes an array of strings arr, and length of arr n as parameters and returns an array of string of length 2. First element of the array should be the name of the candidate and second element should be the number of votes that candidate got in string format.
"""

from collections import Counter


def winner(arr, n):
    new_dict = Counter(arr)
    highestVote = max(new_dict.values())
    winner = min(key for key in new_dict.keys() if new_dict[key] == highestVote)
    return (winner, highestVote)


n = 13
arr = [
    "john",
    "johnny",
    "jackie",
    "johnny",
    "john",
    "jackie",
    "jamie",
    "jamie",
    "john",
    "johnny",
    "jamie",
    "johnny",
    "john",
]

results = winner(arr, n)
print(f"The winner is {results[0]} with the total of {results[1]} votes")
