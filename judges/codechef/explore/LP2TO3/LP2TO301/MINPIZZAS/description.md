---
Contest Name: LP2TO301 - Basic programming concepts
Problem Code: MINPIZZAS
Problem Title: Minimum Number of Pizzas
Problem Difficulty: 
Problem Url: https://www.codechef.com/LP2TO301/problems/MINPIZZAS
Problem Tags: ; 
Editorial Url: 
Video Editorial Url: https://video.gumlet.io/62c2db7b1a5e497c7a49783d/62cd766223a6daa5ba1fa995/main.mpd
Discussion Url: https://discuss.codechef.com/search?q=MINPIZZAS
IsTemplate: No
---


# Problem Statement

Chef is throwing a party for his $N$ friends. There is a pizza store nearby and he wants to buy pizza for his friends. Each pizza has exactly $K$ slices. Chef's friends get sad if one gets more slices than the other. Also, Chef gets sad if there are some pizza slices left. More formally, suppose Chef buys $P$ pizzas, then everyone is happy if and only if there is a way to distribute $K \cdot P$ slices between $N$ friends.

You need to find the minimum number of pizzas Chef has to buy to share all the slices among his friends so that none of his friends gets sad. Note that Chef hates pizza and doesn't take any slices.

# Constraints

- $1 \leq T \leq 2 \cdot 10^5$
- $1 \leq N, K \leq 10^9$


# Format

## Input

- First line of input contains $T$, the number of test cases. Then the test cases follow.
- Each test case contains two space-separated integers $N$ and $K$, where $N$ is the number of friends of chef and $K$ is the number of slices in a pizza.


## Output

For each test case, print the minimum number of pizzas chef has to buy to share among his friends so that none of his friends gets sad.


# Subtasks

- **Subtask 1 (100 points):** Original constraints

# Sample Testcases

## Sample Test 1

**Input:**
3
2 2
2 3
4 2


**Output:**
1
2
2


**Explanation:**
- **Test case $1$:** One pizza has $2$ slices. And there are $2$ friends. So chef can just buy one pizza and give one slice to one friend and another slice to another friend.
- **Test case $2$:** One pizza has $3$ slices. And there are $2$ friends. So chef can't share one pizza without being left out with a slice. So he needs to buy at least $2$ pizzas. And if he buys $2$ pizzas, he can give $3$ slices to one friend and $3$ to another. So the minimum number of pizzas chef needs to buy is equal to $2$.
- **Test case $3$:** One pizza has $2$ slices. And there are $4$ friends. So chef can't share one pizza among the $4$ friends. So he needs to buy at least $2$ pizzas. And if he buys $2$ pizzas, he can give $1$ slice to each of his friends. So the minimum number of pizzas chef needs to buy is equal to $2$.


# Useful References/Discussions


