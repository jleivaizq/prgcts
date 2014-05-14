Professor Normal
================

[Problem Link](https://code.google.com/codejam/contest/2845486/dashboard#s=p3)

## Problem

Professor Normal's three children have been causing trouble at school; so much so that the principal is threatening to
expel them. Clearly, Professor Normal has been doing a great job raising the next generation of recruits for the Evil
League of Evil. In order to appease the principal, he has agreed to organize a game for all of the students at the
school, to teach them valuable life skills. After all, he can't afford to stay at home with the kids -- he has a job to
do and a mortgage to pay.

The game is called Don't Lose Your Marbles. The children stand in an M-by-N grid. Each child is given some number of
marbles to start. Different children may be given a different number of marbles; this teaches them that life is unfair.

The game then proceeds in turns. On each turn, each child gives out 12 marbles shared equally among his neighbours.
Neighbours are the 4 children immediately in front, behind, to the left, and to the right of the child. Some children
will have fewer than 4 neighbours, if they happen to be standing on the edges or in the corners of the grid. This
exchange teaches the children about sharing.

Any children who do not have at least 12 marbles at the start of a turn are removed from the game before the marble
exchange takes place. Their spots will then remain empty until the end of the game, and their neighbours will have fewer
neighbours to exchange marbles with. This teaches the children that one must pay to play.

Children who do not have any neighbours are also then removed because they would have no one to exchange marbles with.
This teaches them not to be selfish.

At this point, if there are no children left in the game, the game ends. Otherwise, every remaining child has somebody
to exchange marbles with, and the game continues. This teaches the children that all things come to an end.

Or do they? Given the initial arrangement of the children and the number of marbles each child has, can you determine
how many turns (marble exchanges) will take place? And please do so quickly, if you can. Professor Normal has evil to
plan.

More precisely, the game proceeds according to the following algorithm:

    number_of_exchanges = 0
    repeat forever {
      while (any child has < 12 marbles or 0 neighbors) {
        remove all such children from play
      }
      if (there are no children left in play) {
        the game ends
      }
      simultaneously for each child in play {
        the child shares 12 marbles equally among neighbors
      }
      increment number_of_exchanges by 1
    }

## Input

The first line of the input gives the number of test cases, T. T test cases follow. Each one starts with a line
containing M followed by a line containing N. The next M lines each contain N space-separated integers -- the number of
marbles for each child in that row of the grid.

## Output

For each test case, output one line containing "Case #x: y turns", where x is the case number (starting from 1) and y is
the number of marble exchanges that will take place before the game is over. If the game goes on forever, then instead
output a line containing "Case #x: z children will play forever", where z is the number of children who will remain
standing in the school's courtyard forever, playing the game.

## Limits

1 ≤ T ≤ 100;

### Small dataset

1 ≤ M ≤ 10;
1 ≤ N ≤ 10;
Each child will start with at most 100 marbles.

### Large dataset

1 ≤ M ≤ 40;
1 ≤ N ≤ 40;
Each child will start with at most 1012 marbles.

## Sample

### Input

6
3
3
12 12 12
12 12 12
12 12 12
2
3
12 12 12
12 12 12
2
2
12 13
14 15
2
3
11 12 11
20 14 20
1
1
74
2
2
10 12
12 12

### Output

Case #1: 2 turns
Case #2: 2 children will play forever
Case #3: 4 children will play forever
Case #4: 2 turns
Case #5: 0 turns
Case #6: 1 turns

