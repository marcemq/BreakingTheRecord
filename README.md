# Breaking The Record
A programing exercise using python and the description of such problem is detailed [here](https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem).


### Solution
An initial solution is provided at [`initSolution.py`](/initSolution.py) and the main `breakingRecord(n, scores)` function is shown below:
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
A second solutions is proposed [`printRecords.py`](/printRecords.py), where we keep track of the best and worst records along with the game for these, in case the client would like to know this information maybe to remember its best games for nostalgy or something :blush:.

The proposed format for it is a tuple list, i.e.: `[('game', record)]` (and yes, the format shall always follow a client requirement but we don't have it for this one, that's why I'm proposing one). Some sample input/output is listed below too:
```
$ ./printRecords.py --games 9 --scores 10 5 20 20 4 5 2 25 1
2 4
Best record: [('3', 20), ('8', 25)]
Worst records: [('2', 5), ('5', 4), ('7', 2), ('9', 1)]

$./printRecords.py --games 10 --scores 3 4 21 36 10 28 35 5 24 42
4 0
Best record: [('2', 4), ('3', 21), ('4', 36), ('10', 42)]
Worst records: []
````

NOTE: And what if the season only have one game? should we considered the score for this game the best one? the worst one? or only have it as a base to starting comparing further scores against it? this situation is ambiguos in the problem statement :thinking_face: . The proposed solutions takes the first game as the base, so if only one game is provided the score of it is considered neutral, not the best nor the worst :speak_no_evil:.

### Complexity

The time complexity for the proposed solutions are `O(n)` since it iterates trought each element from the provided list of scores and the space complexity for:
* `initSolution.py`: `O(n)` since we only use an array to store the provided score list.
* `printRecords.py`: `O(2n) => O(n)` since we use extra arrays to keep track of the best and worst records, which at the end will be `O(n)`

Thinking on a better solution in term of complexity, shall be one that hits `O(c*log*n)` where `c in (0,1)`, and upto this moment I couldn't think of one like that :flushed:
