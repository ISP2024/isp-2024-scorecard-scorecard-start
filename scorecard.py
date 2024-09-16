"""
This code contains common errors that can by detected 
by static type checking -- if the type is known!
Please do not fix this code by inspection.

Instead, add type hints and watch your IDE (or mypy) find errors.

Add these hints ONE AT A TIME.  SAVE the file after each one and run mypy.
Observe how the type hint helps it perform static checking.

1) add type to parameter:                `add_score(self, score: float)` /
2) add type to return value of average:  `average(self) -> ???` /
3) add type to self.scores attribute:    `self.scores: ???[???] = []` /
4) add type hints for all parameters and return values.
   If a function does not return a value, don't write a type hint. /
5) add type to the `suffixes` variable in `ordinal()` function. 
   Include the type of keys and values. /

"""
from typing import Iterable, Sized


class Scorecard(Iterable[float], Sized):
    """Accumulate scores and compute their average."""

    def __init__(self):
        """Initialize a new Scorecard."""
        self.scores: list[float] = []

    def add_score(self, score: float) -> None:
        """Add a score to the Scorecard."""
        self.scores.append(score)

    def average(self) -> float:
        """Return the average of all scores, 0 if no scores."""
        return sum(self.scores) / max(1, len(self.scores))

    def __len__(self) -> int:
        """Return the number of scores."""
        return len(self.scores)

    def __iter__(self):
        """Return an iterator for the scores."""
        return iter(self.scores)


def print_scores(score_card: Scorecard) -> None:
    """Print statistics for the scorecard and the actual scores."""

    # What changes to Scorecard are needed in order to make this code work?
    print(f"Scorecard contains {len(score_card)} scores.")
    print(f"Min score: {min(score_card)}  Max score: {max(score_card)}.")
    # What change to Scorecard is needed to make this work?
    for score in score_card:
        print(score)


def ordinal(num) -> str:
    """Return the ordinal value of an integer; works for numbers up to 20.

    For examples: ordinal(1) is '1st', ordinal(2) is '2nd'.
    """
    suffixes: dict[int, str] = {1: "st", 2: "nd", 3: "rd"}
    return str(num) + suffixes.get(num, "th")


if __name__ == "__main__":
    # Interactively add scores and print some statistics.
    scorecard = Scorecard()

    print("Input 3 scores.")
    for count in range(1, 4):
        score = float(input(f"input {ordinal(count)} score: "))
        scorecard.add_score(score)

    print("The average is ", scorecard.average())

    print_scores(scorecard)
