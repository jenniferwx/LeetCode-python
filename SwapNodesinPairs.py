'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if (not head):
            return None
        phead = ListNode(0)
        phead.next = head
        p = phead
        curr = head
        while curr and curr.next:
            N = curr.next
            NN = N.next
            phead.next = N
            N.next = curr
            curr.next = NN
            phead = curr
            curr = NN
        
        return p.next 
