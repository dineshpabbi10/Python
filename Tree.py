class Node:
	def __init__(self,value):
		self.data = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self,value):
		self.root = Node(value)

	def insert(self,inode,node):
		if inode.data < node.data:
			if node.left is None:
				node.left = inode
			else:
				node = node.left
				self.insert(inode,node)
		elif inode.data > node.data :
			if node.right is None:
				node.right = inode
			else:
				node = node.right
				self.insert(inode,node)

		else:
			node.left = inode

	def find(self,value,node):
		if value == node.data:
			return True

		if value < node.data:
			if node.left is None:
				return False
			else:
				node = node.left
				return self.find(value,node)

		if value > node.data:
			if node.right is None:
				return False
			else:
				node = node.right
				return self.find(value,node)

	def preorder(self,node):
		print(node.data)
		if node.left is not None:
			self.preorder(node.left)
		if node.right is not None:
			self.preorder(node.right)


	def findNode(self,value,node):
		if value < node.data:
			if node.left is None:
				return None,None
			if value == node.left.data:
				return node,node.left
			else:
				return self.findNode(value,node.left)
		elif value > node.data:
			if node.right is None:
				return None,None
			if value == node.right.data:
				return node,node.right
			else:
				return self.findNode(value,node.right)
		else:
			if value == node.data:
				return node,node
			else:
				return None,None


	def delete(self,value,node):
		p,n = self.findNode(value,node)
		if n is None:
			print("Could not find the element")
		else:
			if n.left is None and n.right is None:
				n = None
			elif n.right is None and n.left is not None:
				if parent.left is n:
					parent.left = n.left
				else:
					parent.right = n.left
			elif n.right is not None and n.left is None:
				if parent.left is n:
					parent.left = n.right
				else:
					parent.right = n.right
			else:
				s = n.right
				p = n
				while (s.left is not None):
					p = s
					s = s.left
				n.data = s.data
				if p.left.data == s.data:
					p.left = s.right
				else:
					p.right = s.right


				



t = Tree(15)
r = t.root
# print(r.data)
n1 = Node(10)
n2 = Node(7)
n3 = Node(12)
n4 = Node(20)
n5 = Node(30)
n6 = Node(25)
t.insert(n1,r)
t.insert(n2,r)
t.insert(n3,r)
t.insert(n4,r)
t.insert(n5,r)
t.insert(n6,r)

# print(r.left.data)
# print(r.left.left.data)
# print(r.right.data)
# print(r.left.right.data)
# print(t.find(7,r))
# print(t.find(15,r))
# print(t.find(11,r))
# print(t.find(12,r))
# print(t.find(20,r))
# print(t.find(30,r))
# print(t.find(25,r))

print("Preorder Traversal is :")
t.preorder(r)

print("testing the findNode")

p,n = t.findNode(11,r)
print(p,n)

print("test element deletion")

t.delete(10,r)
t.preorder(r)
