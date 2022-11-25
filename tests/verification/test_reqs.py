from verify import expect
from util import score_letter


def test_score_letter():
    score_ranges = [
        range(0, 60),
        range(60, 70),
        range(70, 80),
        range(80, 90),
        range(90, 101)
    ]
    score_letters = ['F', 'D', 'C', 'B', 'A']

    for score_range, letter in zip(score_ranges, score_letters):
        for score in score_range:
            assert expect(score_letter(score)).Equal(letter)


