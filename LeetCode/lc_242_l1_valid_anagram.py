"""

242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""


class Solution(object):
    def isAnagram_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        else:   
            return sorted(s) == sorted(t)


    def isAnagram_2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        return sorted(s) == sorted(t)
    

    def isAnagram_slow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        else:   
            list_s = []

            for letter in s:
                list_s.append(letter)


            for letter in t:
                if letter in list_s:
                    list_s.remove(letter)
                else:
                    return False

            return True