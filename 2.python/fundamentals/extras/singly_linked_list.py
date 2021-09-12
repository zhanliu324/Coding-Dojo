class SLnode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class SList:
    def __init__(self) -> None:
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLnode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLnode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head == None:
            return self
        self.head = self.head.next
        return self
    
    def remove_from_back(self):
        if self.head == None:
            return self
        runner = self.head
        runner2 = runner.next
        while runner2.next != None:
            runner2 = runner2.next
            runner = runner.next
        runner.next = None
        return self

    def remove_val(self, val):
        if self.head.value == val:
            self.remove_from_front()
            return self
        runner = self.head
        runner2 = runner.next
        while runner2.value != val and runner2.next != None:
            runner2 = runner2.next
            runner = runner.next
        if runner2.value == val:
            runner.next = runner2.next
        else:
            print(f"Value {val} is not in list.")
        return self
        
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        new_node = SLnode(val)
        runner = self.head
        runner2 = runner.next
        m = 1
        while runner2.next != None and m != n:
            runner = runner.next
            runner2 = runner2.next
            m += 1
        if m == n:
            runner.next = new_node
            new_node.next = runner2
        elif m < n:
            runner2.next = new_node
        return self



my_list = SList()
my_list.add_to_front(2).add_to_front(1).add_to_back(3).print_values()  
# my_list.remove_from_front().print_values()  
# my_list.remove_from_back().print_values()  
# my_list.remove_val(12).print_values()
my_list.insert_at(20,3).print_values()