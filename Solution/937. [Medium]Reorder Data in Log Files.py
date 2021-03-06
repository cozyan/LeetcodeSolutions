# 937. Reorder Data in Log Files

# ## Description
# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

 

# Example 1:

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
# Example 2:

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


## Solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Solution1: Comparator
        # seperate dig and letter logs
        l = len(logs)
        dig = []
        let = []
        for i in range(l):
            log_type =  logs[i].split(' ',1)
            # add dig and letter logs to different arraies
            if log_type[1][0].isdigit():
                dig += [logs[i]]
            else:
                let += [logs[i]]

        def split(log):
            return log.split(' ',1)
                  
        def compare(log1, log2):
            # compare the letter logs
            # first compare the contenct
            if split(log1)[1] < split(log2)[1]:
                return -1
            elif split(log1)[1] > split(log2)[1]:
                return 1
        
            # compare the identifiers
            if split(log1)[0] < split(log2)[0]:
                cmp = -1
            elif split(log1)[0] > split(log2)[0]:
                cmp = 1
            else:
                cmp = 0
            return cmp

        # Calling
        let.sort(key=functools.cmp_to_key(compare))
        return let+dig
"""
Time Complexity: O(mnlog(n))
Explaination: 
Python list sort() function uses Timsort algorithm which has time complexity of O(nlogn). 
In our question, n means the total number of letter logs. We then consider the compare() function within the letter log,
this will take up m time for each comparison. So in total it's mnlog(n).

Space Complexity: O(mlog(n))
Explaination:
Python list sort space complexity is O(log(n)), since we compare each letter log, then it's O(mnlog(n)).
Moreover, for each comparision, we need to temporarily store each letter log which also takes O(m) space.
Intotal, it's O(m+mlog(n)) => O(mlog(n)) space.

Some Info:
Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort.
"""
