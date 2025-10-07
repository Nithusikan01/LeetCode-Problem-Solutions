class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)-> ListNode:
        """
        1. Create a dummy head to initialize the LL.
        2. Assign dymmy to current node
        
    	3. loop it untill all the digits are added to result LL.
        	i. get the values of identical indexed nodes from both LL
            ii. sum them up with the old carry
            iii. find the new carry
            iv. store the digit in the next node
       		v. update pointers
            
        """
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get node values
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Find digit and carry
            total = v1 + v2 + carry
            digit = total % 10
            carry = total // 10
            current.next = ListNode(digit)
            
            # Update pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    
    def create_linked_list(self, num: int) -> ListNode:
        dummy = ListNode()
        current = dummy
        
        if num == 0:
            return ListNode(0)
        
        while num != 0:
            # Each digit
            digit = num % 10
            num = num // 10
            current.next = ListNode(digit)
            
            # Update pointers
            current = current.next
        return dummy.next
    
    def print_linked_list(self, node: ListNode) -> None:
        while node:
            print(node.val, end="->" if node.next else "\n")
            node = node.next
    
def run(num1: int, num2: int) -> None:
    if num1 == 0 and num2 == 0:
        print(0)
        return
    
    solution = Solution()
    l1 = solution.create_linked_list(num1)
    l2 = solution.create_linked_list(num2)

    l3 = solution.addTwoNumbers(l1, l2)

    print("The linked list output:")
    solution.print_linked_list(l3)

    print(f"The actual sum is {num1 + num2}.")

if __name__ == "__main__":
    run(120, 220)