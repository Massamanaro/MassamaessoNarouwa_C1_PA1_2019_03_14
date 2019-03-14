#PART II
pa = int
n = int

class Node(object) :
    def __init__(self,a ):# Node object class definition with two attributes
        self.data = a                 #a attribute stands for the data (integer) stored in the node
        self.next_node  = None          #n is the reference to access the next node


    def getData(self):     # this method is built to get data in a given node.its runtime is O (n),space complexity
                           # is also O (n)
         return self.data
    def set_data (self, a): # this is built  to set data in a given node
        self.data = a
    def get_next_node(self): # This method aims to access to the next node in the linked list,runtime =O(n), space= (On)
        return self.next_node
    def set_next_node(self): # this method permits us to set the next node. Space = O(n), runtime = O(n)
        self.next_node = None    # it will allow us to step trough nodes

class CircularLinkedList(object): # Circular linked list class definition
    def __init__(self, current = None): # the classe has the attribute current as reference to point the current node
        self.head = current
        self.size = 0
    def get_size(self):      # this methode allow to get the list size
        return self.size

    def insertion(self,a):            # this method is built to allow user to insert a link in the Circular linked List
        if self.get_size() == 0:       # in the case an if or else condition is true the program runtime = O(1),space(1)
                                       # given that our circular linked list has no beginning and no end
            self.head = Node(a)
            self.head.set_next_node(self.head)
        else:
            new_node = Node(a,self.head.get_next_node())
            self.set_next_node(new_node)
        self.size +=1
    def deletion(self,a):  # this method allow us to remove a link in the list . The runtime = O (n^2) and space =O(n)
        target_node = self.head    # target _node stand for the node we want to delete
        previous_node = None
        while True :
            if target_node.getData() == a :
                if previous_node is not None :
                    previous_node.set_next_node(target_node.get_next_node())
                else:
                    while target_node.get_next_node() != self.head:
                           target_node = target_node.get_next_node()
                    target_node.set_next_node(self.head.get_next_node())
                    self.head = self.head.get_next_node()
                self.size -=1
                return True
            elif target_node.get_next_node() == self.head :
                return False
            previous_node = target_node
            target_node  = target_node.get_next_node()
    def searching(self,a):          # this method allows us to  seacrch a node and get data from it. The runtime = O(n^2)
                                    # the space (n)
        target_node = self.head # the target_node here is the node we are searching .
        while True :
            if target_node.getData() == a :
                return  a
            elif target_node.get_next_node()== self.head:
                return False
            target_node = target_node.get_next_node()
    def Display_list(self):    #This function will print for us the the List.its runtime will be O(n*n), and space = O(n)
        print ("Display list........" )
        if self.head is None :
            return
        target_node = self.head      # here it will print the node we want us our target node
        print (target_node.to_string())
        while target_node.get_next_node() != self.head:
              target_node = target_node.get_next_node()
              print (target_node.to_string())









