---
Contest Name: START54D - Starters 54 Division 4 (Rated)
Problem Code: CREDS
Problem Title: Number of Credits
Problem Difficulty: 
Problem Url: https://www.codechef.com/START54D/problems/CREDS
Problem Tags: Basic Maths; Mathematics
Editorial Url: https://discuss.codechef.com/problems/CREDS
Video Editorial Url: https://video.gumlet.io/62c2db7b1a5e497c7a49783d/630f71ce4dbb69bbe11334f1/main.mpd
Discussion Url: https://discuss.codechef.com/search?q=CREDS
IsTemplate: No
---


# Problem Statement

In the current semester, you have taken $X$ RTP courses, $Y$ Audit courses and 
$Z$ Non-RTP courses. 

The credit distribution for the courses are:
- $4$ credits for clearing each RTP course.
- $2$ credits for clearing each Audit course.
- No credits for clearing a Non-RTP course. 

Assuming that you cleared all your courses, report the number of credits you 
obtain this semester.

# Constraints

- $1 \le T \le 10$
- $1 \le X, Y, Z \le 10$

# Format

## Input

The first line contains a single integer $T$, the number of test cases. 
$T$ test cases follow. Each test case consists of one line, containing $3$ 
integers separated by spaces.
- The first integer is $X$, the number of RTP courses.
- The second integer is $Y$, the number of Audit courses.
- The third integer is $Z$, the number of non-RTP courses.

## Output

The output must consist of $T$ lines. The $i^{th}$ should consist of a single 
integer: the number of credits one gets for the $i^{th}$ test case.

# Sample Testcases

## Sample Test 1

**Input:**
4
6 6 5
8 7 2
9 3 8
9 2 4

**Output:**
36
46
42
40

**Explanation:**
**Test case $1$:** You obtain $4$ credits for each of the RTP courses, 
accounting for $4 \cdot 6 = 24$ credits. You also obtain $2$ credits for each 
audit course, accounting for $2 \cdot 6 = 12$ credits. Finally, you get $0$ 
credits for each of the non-RTP courses, accounting for $0 \cdot 5 = 0$ credits. 
This accounts for a total of $24 + 12 + 0 = 36$ credits.

**Test case $2$:** You obtain $4$ credits for each of the RTP courses, 
accounting for $4 \cdot 8 = 32$ credits. You also obtain $2$ credits for each 
audit course, accounting for $2 \cdot 7 = 14$ credits. Finally, you get $0$ 
credits for each of the non-RTP courses, accounting for $0 \cdot 2 = 0$ credits. 
This accounts for a total of $32 + 14 + 0 = 46$ credits.

**Test case $3$:** You obtain $4$ credits for each of the RTP courses, 
accounting for $4 \cdot 9 = 36$ credits. You also obtain $2$ credits for each 
audit course, accounting for $2 \cdot 3 = 6$ credits. Finally, you get $0$ 
credits for each of the non-RTP courses, accounting for $0 \cdot 8 = 0$ credits. 
This accounts for a total of $36 + 6 + 0 = 42$ credits.

**Test case $4$:** You obtain $4$ credits for each of the RTP courses, 
accounting for $4 \cdot 9 = 36$ credits. You also obtain $2$ credits for each 
audit course, accounting for $2 \cdot 2 = 4$ credits. Finally, you get $0$ 
credits for each of the non-RTP courses, accounting for $0 \cdot 4 = 0$ credits. 
This accounts for a total of $36 + 4 + 0 = 40$ credits.

# Useful References/Discussions
