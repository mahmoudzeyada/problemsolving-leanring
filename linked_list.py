class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linked_list:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def delete(self, value):
        current = self.head
        prev = None
        while current.value != value and current.next:
            prev = current
            current = current.next
        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    def get_postion(self, postion):
        counter = 0
        current = self.head
        if postion > 0:
            while counter != postion and current:
                current = current.next
                counter += 1
            if counter == postion:
                return current
            return None
        return None

    def insert(self, element, postion):
        prev = None
        try:
            current_element = self.get_postion(postion)
        except:
            return None
        current = self.head
        while current and current.value != current_element.value:
            prev = current
            current = current.next

        if current:
            if prev:
                prev.next = element
                element.next = current_element
            else:
                self.head = element


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

ll = linked_list(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
print(ll.get_postion(1).value)
ll.insert(n5, 2)
print(ll.get_postion(2).value)
ll.delete(10)
