votes = {"A": 0, "B": 0, "C": 0}

def add_vote(candidate):
    if candidate in votes:
        votes[candidate] += 1

def winner():
    print("Winner:", max(votes, key=votes.get))
