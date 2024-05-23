"""

49. Group Anagrams
Solved
Medium

Topics
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Dictionary to hold the grouped anagrams
        anagrams = {}
        
        for word in strs:
            # Sort the word to use it as a key
            sorted_word = ''.join(sorted(word))
            
            # If the sorted word is not in the dictionary, add it with the original word in a list
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                # If the sorted word is already a key, append the original word to the list
                anagrams[sorted_word].append(word)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())