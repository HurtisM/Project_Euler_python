# Problem 54
# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins; for example,
# a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example,
# both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
# if the highest cards tie then the next highest cards are compared, and so on.
#
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards
# (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in
# no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win
from collections import Counter

VALUE_MAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, 'T': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}


def parse_card(card):
    """card like '5H' or 'TD' -> (value_int, suit_char)"""
    return VALUE_MAP[card[0]], card[1]


def is_straight(values):
    """values: list of ints (not necessarily unique sorted). Return (True, top_value)"""
    vals = sorted(set(values))
    if len(vals) != 5:
        return False, None
    # normal straight
    if max(vals) - min(vals) == 4:
        return True, max(vals)
    # wheel straight: A,2,3,4,5 represented as [2,3,4,5,14]
    if vals == [2,3,4,5,14]:
        return True, 5  # treat top as 5 for tie-breaking
    return False, None


def rank_hand(cards):
    """
    cards: list of 5 strings like ['5H','5C','6S','7S','KD']
    returns: tuple (rank, tie1, tie2, ...)
        higher tuple -> stronger hand
    Rank order (higher is better):
      9: Straight Flush (incl. Royal as top case)
      8: Four of a Kind
      7: Full House
      6: Flush
      5: Straight
      4: Three of a Kind
      3: Two Pairs
      2: One Pair
      1: High Card
    """
    vals = []
    suits = []
    for c in cards:
        v, s = parse_card(c)
        vals.append(v)
        suits.append(s)

    vals.sort(reverse=True)  # descending
    counts = Counter(vals)
    # Frequency groups sorted by (count desc, value desc)
    freq_sorted = sorted(counts.items(), key=lambda iv: (iv[1], iv[0]), reverse=True)
    # e.g. freq_sorted = [(value_of_most_common, count), (...), ...]

    is_flush = len(set(suits)) == 1
    straight, top_straight = is_straight(vals)

    # Straight Flush (including Royal)
    if straight and is_flush:
        return (9, top_straight)

    # Four of a kind
    if freq_sorted[0][1] == 4:
        four_val = freq_sorted[0][0]
        kicker = [v for v in vals if v != four_val][0]
        return (8, four_val, kicker)

    # Full house (3 + 2)
    if freq_sorted[0][1] == 3 and freq_sorted[1][1] == 2:
        three_val = freq_sorted[0][0]
        pair_val = freq_sorted[1][0]
        return (7, three_val, pair_val)

    # Flush
    if is_flush:
        return (6, ) + tuple(vals)

    # Straight
    if straight:
        return (5, top_straight)

    # Three of a kind
    if freq_sorted[0][1] == 3:
        three_val = freq_sorted[0][0]
        kickers = sorted([v for v in vals if v != three_val], reverse=True)
        return (4, three_val) + tuple(kickers)

    # Two pairs
    if freq_sorted[0][1] == 2 and freq_sorted[1][1] == 2:
        pair_high = max(freq_sorted[0][0], freq_sorted[1][0])
        pair_low = min(freq_sorted[0][0], freq_sorted[1][0])
        kicker = [v for v in vals if v != pair_high and v != pair_low][0]
        return (3, pair_high, pair_low, kicker)

    # One pair
    if freq_sorted[0][1] == 2:
        pair_val = freq_sorted[0][0]
        kickers = sorted([v for v in vals if v != pair_val], reverse=True)
        return (2, pair_val) + tuple(kickers)

    # High card
    return (1, ) + tuple(vals)


def compare_hands(hand1, hand2):
    """Return 1 if hand1 > hand2, -1 if hand1 < hand2, 0 if tie (Problem says no ties)."""
    r1 = rank_hand(hand1)
    r2 = rank_hand(hand2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return -1
    else:
        return 0


def count_player1_wins_from_file(filename):
    wins = 0
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            p1 = parts[:5]
            p2 = parts[5:]
            if compare_hands(p1, p2) == 1:
                wins += 1
    return wins


if __name__ == "__main__":
    print("Player 1 wins:", count_player1_wins_from_file("P054input.txt"))
