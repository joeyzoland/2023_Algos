"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints:

The given address is a valid IPv4 address.
"""

class Solution:
    def defangIPaddr(self, address):
        listAnswer = []
        for i in range(0, len(address)):
            if address[i] == ".":
                listAnswer.append("[.]")
            else:
                listAnswer.append(address[i])
        return "".join(listAnswer)

solution = Solution()
print solution.defangIPaddr("1.1.1.1")
