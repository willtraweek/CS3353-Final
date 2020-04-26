# CS 3353 Algorithms Final Project

We had to choose an algorithm to study and write a program to examine a trivial and non-trivial solution to the problem.  I chose the Knapsack problem, as I was interested in its uses for stock portfolio creation and awed by how quickly the difficulty scales.

Rather than just create blank test data to run this on in a raw test of speed, I decided to make it a little more fun with the real world application of a truck that needs to fill itself with boxes of assorted goods, weights, and prices.  The truck clearly wants to take the most value it can with it, and thus requires a result from a knapsack-like problem.

## Test Data

I pulled a list of items from the [North American Product Classification System](https://www.census.gov/eos/www/napcs/index.html).  That was used to produce the list of 100 importable items.  Prices, weights, and quantities are randomly generated at this moment.  This allows you to test the algorithm implementation on up to 100 items.  Given that the dynamic programming approach to the Knapsack problem is O(nW) where n is the num of items and W is the capacity of the knapsack, there is enough variability in 100 items that I found this sufficient to test on.