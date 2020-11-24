# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #We make a previous node variable (prev) and set it to Null as the previous of the (1) node is Null. In Python, Null is None.
        prev = None
        
        while head is not None:
            
            next_node = head.next #Makes node 2 as our next node in the first iteration
            
            head.next = prev #Changes the pointer of the current node (1) from (2) to (NULL). Then from (2) from (3) to (1), then (3) from (4) to (2), and so on until the list is fully reversed.
            prev = head #Makes prev our current head (1) so that it can be used in the next loop when the head is at (2), the prev will be (1). It will then be changed to (2), (3), etc. in each passing iteration of the loop.
            
            head = next_node #Finally, we change our head to be the next node. It would go from 1 to 2.
            
        return prev
