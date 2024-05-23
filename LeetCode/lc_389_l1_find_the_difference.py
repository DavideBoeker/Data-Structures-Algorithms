"""

389. Find the Difference
Solved
Easy

Topics
Companies
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
 

Constraints:

0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters.

"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        t = list(t)

        for i in range(len(s)):

            if s[i] in t:
                t.remove(s[i])
            else:
                return s[i]

            i =+ 1

        return t[0]
    

    def findTheDifference_ii(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        xor = 0
        for char in s:
            xor ^= ord(char)
        for char in t:
            xor ^= ord(char)
        return chr(xor)