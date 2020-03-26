#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            self.head=newnode
            newnode.next=temp
    #printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            else:
                print(currentnode.data)
                currentnode=currentnode.next
    #deleting a node at a given position
    def delete(self,position):
        temp=self.head
        #if linkedlist is empty
        if temp is None:
            return
        #if position is zero i.e. headnode
        if position == 0 : 
            self.head=temp.next
            temp=None
            return
        for i in range(position-1):
            if temp is None:
                break
            temp=temp.next
        #if linkedlist is  smaller than the given position    
        if temp is None:
            return
        if temp.next is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
if __name__=="__main__":
    llist=LinkedList()
    firstnode=Node(4)
    secondnode=Node(3)
    thirdnode=Node(2)
    fourthnode=Node(1)
    llist.push(firstnode)
    llist.push(secondnode)
    llist.push(thirdnode)
    llist.push(fourthnode)
    print("linkedlist before deleting")
    llist.printllist()
    llist.delete(4)
    print("linkedlist after deleting")
    llist.printllist()
        

        
        

