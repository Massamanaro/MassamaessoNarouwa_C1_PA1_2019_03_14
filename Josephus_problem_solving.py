# PART 3 Josephus problem solving 
m = int


class Node:
    def __init__(self, m):   # definition of the node class
        self.data = m         # In this part 3 we have to mention that our circular linked list has an end and a beginning
                              # so we will have  a previous node and an after node
        self.next = None


class CircularLinkedList ():    #definition  of the List class
    def __init__(self):
        self.head = None     # the head intialy is null (has no reference)

    def append(self, a):      # the method append allow us to add data at the end of our list
        node = Node(a)
        self.insert_at_end(node)

    def get_node(self, index, start): # here the method aims to get a given node in the list
        if self.head is None:           # index stands for node index in the list range
            return None
        current = start
        for i in range(index):
            current = current.next
        return current

    def get_prev_node(self, ref_node): # here we want to get previous node using head as current to point the current node
        if self.head is None:
            return None
        current = self.head
        while current.next != ref_node: # when the current next node is different from the refered node the current becomes the next node
            current = current.next
        return current

    def insert_after(self, ref_node, new_node): # this method allows to insert a new node after a node set us reference .
        new_node.next = ref_node.next
        ref_node.next = new_node

    def insert_before(self, ref_node, new_node):# the method iserts node before the refered node
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)

    def insert_at_end(self, new_node):   # the method append the new node in the list structure
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            self.insert_before(self.head, new_node)

    def remove(self, node): # this method deletes a given node in the list
        if self.head.next == self.head:
            self.head = None
        else:
            prev_node = self.get_prev_node(node)
            prev_node.next = node.next
            if self.head == node:
                self.head = node.next


def has_one_node(josephuslist): # this method defines the josephus problem solving modelling
    if josephuslist.head.next == josephuslist.head: # josephuslist stands for the range of the number of people in our list
        return True
    else:
        return False


def get_josephus_solution(josephuslist, m):  # m stands for the position of the first person to start counting in circle
    if josephuslist.head is None:
        return None
    start = josephuslist.head
    while not has_one_node(josephuslist):
        to_remove = josephuslist.get_node(m - 1, start)# once someone is killed it discount the position by doing minus one
        start = to_remove.next
        josephuslist.remove(to_remove)
    return josephuslist.head.data

josephuslist = CircularLinkedList()    # it will print the result when inputs are executed and will tell which person will die
                                       # by showing his position
n = int(input('Type the number of people in the Josephus circle : '))
m = int(input('The mth person will be executed. Input m: '))
for i in range(1, n + 1): # this for loop allows to add people in the list as the list will be updating untill we got
                           # the last person that will not be killed. The runtime here is O(n).
    josephuslist.append(i)

ans = get_josephus_solution(josephuslist, m)
print('The person at position {} won\'t be killed.'.format(ans))