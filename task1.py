class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        self.head = reverse_list(self.head)

    def sort(self):
        self.head = merge_sort(self.head)

    def merge_with(self, other_list):
        self.head = merge_sorted_lists(self.head, other_list.head)

# Функція для реверсування однозв'язного списку
def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Алгоритм сортування однозв'язного списку (сортування злиттям)
def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def sorted_merge(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)

    return result

# Функція для об'єднання двох відсортованих однозв'язних списків
def merge_sorted_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.data <= list2.data:
        result = list1
        result.next = merge_sorted_lists(list1.next, list2)
    else:
        result = list2
        result.next = merge_sorted_lists(list1, list2.next)

    return result

# Приклад використання
llist1 = LinkedList()
llist1.insert_at_end(15)
llist1.insert_at_end(10)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(25)
llist2.insert_at_end(20)

print("Перший зв'язний список:")
llist1.print_list()

print("Другий зв'язний список:")
llist2.print_list()

llist1.sort()
llist2.sort()

print("Відсортований перший зв'язний список:")
llist1.print_list()

print("Відсортований другий зв'язний список:")
llist2.print_list()

llist1.merge_with(llist2)

print("Об'єднаний зв'язний список:")
llist1.print_list()

llist1.reverse()
print("Реверсований об'єднаний зв'язний список:")
llist1.print_list()
