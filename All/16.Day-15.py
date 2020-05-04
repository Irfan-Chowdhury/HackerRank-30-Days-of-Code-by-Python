class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head is None:
            head = Node(data)
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = Node(data)
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);



# ==== Without Linked List ====
'''
data=[]
T= int(input())
for i in range(T):
    value = int(input())
    data.insert(i, value)


#Print a list of space-separated elements in Python 3
print(*data)
print(*data, sep=', ')
print(*data, sep=' -> ')

joined_string = ' '.join([str(v) for v in data])
print(joined_string)
'''