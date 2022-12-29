class Node :
    def __init__(self, data) :
        self.data = data

class LinkedList : 
    pass
    
head = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = None

def countNodes(head) :
    count = 1
    current = head
    while (current.next != None) :
        current = current.next
        count += 1
    print(count)
    
countNodes(head)

def countNode(head, count) :
    if head.next == None :
        print(count)
        return
    else : 
        countNode(head.next, count+1)
        
countNode(head, 1)