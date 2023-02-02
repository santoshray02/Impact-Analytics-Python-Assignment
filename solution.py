def solve(n):
    if n<4:
        return f"{2**(n-1)}/{2**n}"
    A=2 # The number of ways to attend classes for the current day.
    AA=1 # The number of ways to attend classes for the current day and the previous day.
    AAA=1 # The number of ways to attend classes for the current day, the previous day, and the day before that.
    P = 4 # The number of ways to attend classes for the current day, the previous day, the day before that, and the day before that.
    count = 8 # The total number of ways to attend classes over n + 4 days.
    for i in range(4,n+1):
        temp= AAA
        AAA=AA
        AA=A
        A=P
        P= count
        count = (count-temp)*2+temp
    return f"{AAA+AA+A}/{count}"
  
  
if __name__ == "__main__":
  n = int(input("Enter N : "))
  ans = solve(n)
  print(ans)
  
  
# Explanation-
# The code starts by checking if n is less than 4. If n is less than 4, it returns 2 ** (n-1) as the number of ways to attend classes over n days and 2 ** n as the total number of ways to attend classes.

# For n greater than or equal to 4, the code iterates from 4 to n, updating the values of A, AA, AAA, P, and count in each iteration. The values are updated in a way that takes into account the constraint that one cannot miss classes for four or more consecutive days.

# Finally, the function returns the result by adding up AAA, AA, and A, and dividing it by count. The result is returned as a string in the format (AAA + AA + A) / count.
