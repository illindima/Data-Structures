class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None
		
class LinkedList(object):
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
			
	def get_position(self, position):
		"""Get an element from a particular position.
		Assume the first position is "1".
		Return "None" if position is not in the list."""
		current = self.head
		counter = 1
	
		while current:
			if counter == position:
				return current
			else:
				counter += 1
				current = current.next
		
		return None
		
	
	def insert(self, new_element, position):
		"""Insert a new node at the given position.
		Assume the first position is "1".
		Inserting at position 3 means between
		the 2nd and 3rd elements."""
		if position > 1:
			current = self.get_position(position - 1)

			if current:
				next_element = current.next
				
				current.next = new_element
				current.next.next = next_element
		elif (position == 1):
			new_element.next = self.head
			self.head = new_element
	
	
	def delete(self, value):
		"""Delete the first node with a given value."""
		current = self.head
		previous = None

		while current.value != value and current.next:
			previous = current
			current = current.next

		if current.value == value:
			if previous:
				previous.next = current.next
			else:
				self.head = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print(ll.get_position(1).value)
print(ll.get_position(2).value)

# Insert some Element

ll.insert(e4, 1)



