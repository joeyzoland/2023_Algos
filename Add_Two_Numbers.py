"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        #Check nodes of similar position
        #If both exist:
            #Add both together (as well as any carryover from last calculation)
            #Push anything over 10 to next calculation
        #If one exists:
            #Append it to previous node and return list's head
        #If neither exist:
            #Return list's head
        firstSum = l1.val + l2.val
        if firstSum >= 10:
            head = ListNode(firstSum - 10)
            carryover = 1
        else:
            head = ListNode(firstSum)
            carryover = 0
        currentNew = head
        currentL1 = l1.next
        currentL2 = l2.next
        while True:
            if (currentL1 != None and currentL2 != None):
                sum = currentL1.val + currentL2.val + carryover
                if (sum >= 10):
                    currentNew.next = ListNode(sum - 10)
                    carryover = 1
                else:
                    currentNew.next = ListNode(sum)
                    carryover = 0
                currentL1 = currentL1.next
                currentL2 = currentL2.next
                currentNew = currentNew.next
            elif (carryover == 1):
                if (currentL1 != None):
                    if (currentL1.val == 9):
                        currentNew.next = ListNode(0)
                        carryover = 1
                        currentL1 = currentL1.next
                        currentNew = currentNew.next
                    else:
                        currentNew.next = ListNode(currentL1.val + 1)
                        currentNew.next.next = currentL1.next
                        return head
                elif (currentL2 != None):
                    if (currentL2.val == 9):
                        currentNew.next = ListNode(0)
                        carryover = 1
                        currentL2 = currentL2.next
                        currentNew = currentNew.next
                    else:
                        currentNew.next = ListNode(currentL2.val + 1)
                        currentNew.next.next = currentL2.next
                        return head
                else:
                    currentNew.next = ListNode(1)
                    return head
            else:
                if (currentL1 != None):
                    currentNew.next = currentL1
                elif (currentL2 != None):
                    currentNew.next = currentL2
                return head

    def linkedListConstructor(self, list):
        head = ListNode(list[0])
        current = head
        for i in range(1, len(list)):
            current.next = ListNode(list[i])
            current = current.next
        return head

    def linkedListPrinter(self, head):
        print (head.val)
        current = head.next
        while current != None:
            print (current.val)
            current = current.next

#Note: I created the linkedListConstructor and linkedListPrinter functions previously, solely for testing purposes.

print("First Question:")
solution = Solution()
inputL1 = solution.linkedListConstructor([2,4,3])
inputL2 = solution.linkedListConstructor([5,6,4])
solutionHead = solution.addTwoNumbers(inputL1, inputL2)
solution.linkedListPrinter(solutionHead)

print("Second Question:")
solution = Solution()
inputL1 = solution.linkedListConstructor([0])
inputL2 = solution.linkedListConstructor([0])
solutionHead = solution.addTwoNumbers(inputL1, inputL2)
solution.linkedListPrinter(solutionHead)

print("Third Question:")
solution = Solution()
inputL1 = solution.linkedListConstructor([9,9,9,9,9,9,9])
inputL2 = solution.linkedListConstructor([9,9,9,9])
solutionHead = solution.addTwoNumbers(inputL1, inputL2)
solution.linkedListPrinter(solutionHead)
