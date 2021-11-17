"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
    
# Method 1: map + dp (dynamic programming)
## the idea is to add all the combinations for n into map/dictionary, 
## and based on the previous combinations and get current n solution since the subquestion for each n={2,3,4,5,...} is the same.
## time complexity: (n^2)*(m^2), m is average combinations for n
## space complexity: n*m (represents the dictionary space)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        dic = {1:['()']}
         
        # get total combinations for each n
        for i in range(2,n+1):
            
            comb = []
            # get combinations within n
            for j in range(1,i):
            
                # get combinations for each pairs. ex: 3=1+2,2+1; 4=1+3,3+1,2+2;...
                for item1 in dic[j]:
                    for item2 in dic[i-j]:
                        comb += [item1 + item2]
                    # add the special combination with n-1 inside brackets
                    if j == i - 1:
                        comb += ['(' + item1 + ')']
                        
            # add current n=i combination to the dictionary
            dic[i] = set(comb)
        
        return dic[n]
      
# Method 2: Backtracking (from leetcode)
## the idea is to get valid combinations based on index and the total length to keep tracking of 
## the combination result.
## for each n the total num of combinations is {1,1,2,5,14,42,132,...} where n is {0,1,2,3,4,5,...}
## the mathematical euqation for this is called Catalan number (Cn) = [1/(n+1)][2n n]=(2n)!/((n+1)!n!)
## time complexity is the Cn: O(4n/n*sqrt(n)) = O(4n/sqrt(n))
## space complexity: the list stores the total Cn combination which is also O(4n/sqrt(n))
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            # append each valid combination for the given n
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop() # clear the current valid combination
                
            # close the brackets within the combination
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
        
