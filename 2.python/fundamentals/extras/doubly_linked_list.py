class DLnode:
    def __init__(self, val) -> None:
        self.value = val
        self.prev = None
        self.next = None

class Dlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_values(self):
        runner = self.head
        while runner != None:
            print(f"Value: {runner.value}, previous: {runner.prev}, next: {runner.next}.")
            runner = runner.next
        return self

    def add_to_end(self, val):
        new_node = DLnode(val)
        if self.tail == None:
            self.tail, self.head = new_node, new_node
            return self
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return self
    
    def insert_before(self, val_before, val):
        new_node = DLnode(val)
        if self.head == None:
            self.tail, self.head = new_node, new_node
            return self
        runner = self.head
        while runner.value != val_before and runner.next != None:
            runner = runner.next
        if runner.value != val_before:
            print(f"Value {val_before} doesn't exist.")
            return self
        new_node.next = runner
        new_node.prev = runner.prev
        if runner.prev == None:
            runner.prev = new_node
            self.head = new_node
            return self
        runner.prev.next = new_node
        runner.prev = new_node
        return self

    def insert_after(self, val_after, val):
        new_node = DLnode(val)
        if self.head == None:
            self.tail, self.head = new_node, new_node
            return self
        runner = self.head
        while runner.value != val_after and runner.next != None:
            runner = runner.next
        if runner.value != val_after:
            print(f"Value {val_after} doesn't exist.")
            return self
        new_node.prev = runner
        new_node.next = runner.next
        if runner.next == None:
            runner.next = new_node
            self.tail = new_node
            return self
        runner.next.prev = new_node
        runner.next = new_node
        return self

    def remove_val(self, val):
        runner = self.head
        while runner.value != val and runner.next != None:
            runner = runner.next
        if runner.value != val:
            print(f"Value {val} doesn't exist.")
            return self
        if runner.prev == None:
            self.head = runner.next
        else:
            runner.prev.next = runner.next
        if runner.next == None:
            self.tail = runner.prev
        else:
            runner.next.prev = runner.prev
        return self

list = Dlist()
list.add_to_end(1).add_to_end(2).add_to_end(3)
# list.insert_before(1, 5)
# list.print_values()
# list.remove_val(5).print_values()
list.insert_after(3,5).print_values()