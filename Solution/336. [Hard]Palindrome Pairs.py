"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, 
so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]

"""
"""
# Brutal Method
## Time Complexity O(n^2*m), m is the average word length
## Space Complexity = Auxiliary space + Space use by input values. Here is O(n^2+m)=O(n^2) with m is average length of the word.
## O(n^2) is becuase in the output when we have the worst case we need to store total n*n pairs. m applies when we store each word.
## The problem here is it's really time-consuming and inefficient.
"""
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        l = len(words)
        palindrom = []
        
        for i in range(l):
            # get first element in pair
            first = words[i]
            for j in range(l):
                if i != j:
                    # get second element in pari
                    second = words[j]
                    sumstr = first+second
                    # get reverse of the sumstr
                    revstr = sumstr[::-1]
                    
                    if sumstr == revstr:
                        # if it is a palinrom
                        palindrom += [[i,j]]
        return palindrom
"""
# map method
First, we create a map with key is the word and the value is the corresponding index of the word.
For this question, we consider 3 cases:
1. Since the words list is unique, we know that there only could be one "" empty string. 
Here we consdier the situation when the pair is one palindromic word and one empty string. 
Ex: "aba" + "" is a palindrome pair on both pairing orders [0,1] and [1,0].

2. Here we consider when there's a reverse word alreadyd existed in the map. So we can simply find and return the pair. 
Ex: "abcd"[0] and "dcba"[1] existed in map, return [0,1]. 
The pair "dcba" + "abcd" is also a palindrome, we return [1,0] when we consider "dcba".

3. The most interesting part is although we cannot find the whole reverse part in case 2 of the word, 
there exists the partial reversed part in the word in our map. In this siuation, 
we consider the sub two cases: left substr and right substr.

3.1 We check the left substring of the word. 
If the rest right part of the word is palindrome then we find if the reversed left substring exists in map. 
If we can find the reversed left substring, we then return the position [word_index, left_substr_index].
Ex: for "sssll" we get left substr "sssl" and right one is "ll", since "ll" is palindromic, 
we then find if reversed leftstr "lsss" is in the map. The pair should be "sssll" + "lsss".

3.2 We check the right substring of the word. 
If the rest left part of the word is palindrome then we find if the revsered right substring exists in map.
Under this case we don't have to check the whole reversed word palindrome since we've already checked in case 2. 
If we can find the reversed left substring, we then return the position [right_substr_index, word_index].
Ex: for "sssll" we get right substr "ssll" and left one is "s", since "s" is palindromic, 
we then find if reversed rightstr "llss" is in the map. The pair should be "llss" + "sssll".

Time Complexity: O(n*m^2) n is number of total words, m is avg words length. 
isPal takes linear time O(n), and we are getting the subtring of word so by checking substr is O(m^2) in checking
each char of this word(i.e. a list of char).
Space Complexity: O(n)
"""
   
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        l = len(words)
        mword = {}
        result = [] # result list
        
        for i in range(l):
            # add word to map with key is word and value is index
            mword[words[i]] = i
        
        def isPal(word: str) -> bool:
            # check if the word is palindorme or not
            rword = word[::-1]
            if rword == word:
                return True
            return False        

        # consider the case: word + ""
        if "" in mword.keys():
            empty_p = mword[""]
            for word in mword.keys():
                if word != "" and isPal(word):
                    word_p = mword[word]
                    result += [[empty_p,word_p],[word_p,empty_p]]
        
        # consider the case: exists entire reversed word
        for word in mword.keys():
            rword = word[::-1]
            word_p = mword[word]
            if rword in mword.keys() and mword[rword] != word_p:
                result += [[word_p, mword[rword]]]
                
        
        # consdier the caes: exists the reversed subword of the word
        for word in mword.keys():
            wordl = len(word)
            if wordl > 1:
                # consdier left subword
                for i in range(1,wordl): # don't check the entire word
                    left = word[0:i]
                    right = word[i:]
                    if isPal(right):
                        word_p = mword[word]
                        # if the right substr is Palindrome then we find if rleft str is in the map
                        rleft = left[::-1] # reversed left substr
                        if rleft in mword.keys() and mword[rleft] != word_p:
                            result += [[word_p, mword[rleft]]]
                
                # consider right subword
                for i in range(wordl-1,0,-1):
                    right = word[wordl-i:]
                    left = word[:-i]
                    if isPal(left):
                        word_p = mword[word]
                        # if the left substr is Palindrome then check if rright str is in the map
                        rright = right[::-1]
                        if rright in mword.keys() and mword[rright] != word_p:
                            result += [[mword[rright],word_p]]
           
        
        return result
      
      
      
"""
# Trie method



"""
