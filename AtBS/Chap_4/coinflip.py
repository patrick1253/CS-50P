# AtBS Chap 4 problems: Coin Flip Streaks

"""
A program to find out how often a streak of six heasds or a streak of six tails comes up 
in a randomly generated list of heads and tails.

"""

import random

def main():
    number_of_runs = 10000
    streaks = 0

    for _ in range(number_of_runs):
        streaks = streaks + check_streaks()
        #print(streaks)
    avg = streaks/number_of_runs
    print(f"Avg percentage of six heads or tails in a row over {number_of_runs:,} trials: {avg:.2f}%")
    print(f"50% odds for 6 flips in a row, x2 (for Heads + Tails): {2*(0.5**6)*100}%")

def hundred_flips():
    flips = []
    for flip in range(100):
        flip = random.choice(['H', 'T'])
        flips.append(flip)
    return flips


def check_streaks():
    streaks = 0
    in_a_row = 0
    flips = hundred_flips()
    #print(flips)

    for i in range(0, 99):
        for j in range(6):
            #print(flips[i], flips[i-j])
            if flips[i] != flips[i-j]:
                in_a_row = 0
                break
            else:
                in_a_row += 1
                if in_a_row == 6:
                    #print(in_a_row)
                    streaks += 1
                    in_a_row = 0
                continue
    return streaks


if __name__ == "__main__":
    main()
