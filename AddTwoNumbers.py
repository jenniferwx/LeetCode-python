# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        res = ListNode(0)
        head = res
        carry = 0
        while(l1 and l2):
            sum = l1.val+l2.val+carry
            res.next = ListNode(sum%10)
            carry = sum/10
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        while(l1):
            sum = carry + l1.val
            res.next = ListNode(sum%10)
            carry = sum/10
            res = res.next
            l1 = l1.next
        
        while(l2):
            sum = carry + l2.val
            res.next = ListNode(sum%10)
            carry = sum/10
            res = res.next
            l2 = l2.next    
        if(carry):
            res.next = ListNode(carry)
        
        return head.next 
