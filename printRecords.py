#!/usr/bin/env python3

import argparse

def checkConstraints(n, scores):
    """ Checks based constraints for given input """
    if n != len(scores):
        return False

    if n not in range(1, 1001):
        return False

    for score in scores:
        if score not in range(1, 100000001):
            return False

    return True

def breakingRecords(n, scores):
    """ Prints the number of highest and lowest records """
    if not checkConstraints(n, scores):
        print("Contraints broken! \n Please review provided input")
        return False

    highest, lowest = scores[0], scores[0]
    highestCount, lowestCount = 0, 0
    highestIdxVal, lowestIdxVal = [],[]

    for idx, score in enumerate(scores):
        if score > highest:
            highestCount += 1
            highest = score
            highestIdxVal.append((str(idx+1), highest))
        elif score < lowest:
            lowestCount += 1
            lowest = score
            lowestIdxVal.append((str(idx+1), lowest))

    print("{} {}".format(highestCount, lowestCount))
    print("Best records: {}".format(highestIdxVal))
    print("Worst records: {}".format(lowestIdxVal))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--games', type=int, help="Number of games")
    parser.add_argument('--scores',nargs="+", type=int, help="Scores list (space separated)")
    args = parser.parse_args()
    breakingRecords(args.games, args.scores)