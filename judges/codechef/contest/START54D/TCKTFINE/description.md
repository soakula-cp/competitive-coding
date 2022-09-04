---
Contest Name: START54D - Starters 54 Division 4 (Rated)
Problem Code: TCKTFINE
Problem Title: Ticket Fine
Problem Difficulty: 
Problem Url: https://www.codechef.com/START54D/problems/TCKTFINE
Problem Tags: Basic Maths; Mathematics
Editorial Url: https://discuss.codechef.com/problems/TCKTFINE
Video Editorial Url: https://video.gumlet.io/62c2db7b1a5e497c7a49783d/630f24365047db4af4ef0a40/main.mpd
Discussion Url: https://discuss.codechef.com/search?q=TCKTFINE
IsTemplate: No
---


# Problem Statement

On a certain train, Chef-the ticket collector, collects a fine of Rs. $X$ if a 
passenger is travelling without a ticket. It is known that a passenger carries 
either a single ticket or no ticket. 

$P$ passengers are travelling and they have a total of $Q$ tickets. Help Chef 
calculate the total fine collected.

# Constraints

- $1 \le T \le 10$
- $1 \le X \le 10$
- $0 \le Q \le P \le 10$

# Format

## Input

The first line contains a single integer $T$, the number of test cases. $T$ 
lines follow. Each following line contains three integers separated by spaces, 
whose description follows.
- The first integer, $X$, is the fee in rupees.
- The second integer, $P$, is the number of passengers on the train.
- The third integer, $Q$, is the number of tickets Chef collected.

## Output

The output must consist of $T$ lines.
- The $i^{th}$ line must contain a single integer, the total money(in rupees) 
  collected by Chef corresponding to the $i^{th}$ test case.

# Sample Testcases

## Sample Test 1

**Input:**
4
4 1 1
2 10 7
8 5 4
9 7 0

**Output:**
0
6
8
63

**Explanation:**
**Test case $1$:** The total number of passengers travelling without ticket are 
$1 - 1 = 0$. So the total fine collected is $0 \cdot 4 = 0$ rupees.

**Test case $2$:** The total number of passengers travelling without ticket are 
$10 - 7 = 3$. So the total fine collected is $3 \cdot 2 = 6$ rupees.

**Test case $3$:** The total number of passengers travelling without ticket are 
$5 - 4 = 1$. So the total fine collected is $1 \cdot 8 = 8$ rupees.

**Test case $4$:** The total number of passengers travelling without ticket are 
$7 - 0 = 7$. So the total fine collected is $7 \cdot 9 = 63$ rupees.

# Useful References/Discussions
