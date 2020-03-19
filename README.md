# Breaking The Record
A programing exercise using python and the description of such problem is detailed [here](https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem).

An initial solution is provided at `initSolution.py` and the main `breakingRecord(n, scores)` function is shown below:
```
def breakingRecords(n, scores):
    """ Prints the number of highest and lowest records """
    if not checkConstraints(n, scores):
        print("Contraints broken! \n Please review provided input")
        return False

    highest, lowest = scores[0], scores[0]
    highestCount, lowestCount = 0, 0

    for score in scores:
        if score > highest:
            highestCount += 1
            highest = score
        elif score < lowest:
            lowestCount += 1
            lowest = score

    print("{} {}".format(highestCount, lowestCount))
```
The provided initial solution contains an usage guide and also an extra function to verify the stablished contraints such as:
* The provided number of games `n` *must be* the same as the scores length (**assumed**)
* `1<=n<=1000`
* `0<=scores[i]<=1000`

And some sample input/output is listed below too:
```
$ ./initSolution.py --games 10 --scores 3 4 21 36 10 28 35 5 24 42
4 0
$ ./initSolution.py --games 9 --scores 10 5 20 20 4 5 2 25 1      
2 4
```
The complexity of the proposed solution is `O(n)` since it iterates trought each element from the provided list of scores.
