class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_min(node):
    # Function to find the minimum element in a binary search tree
    if node is None:
        return None
    if node.left:
        return find_min(node.left)
    else:
        return node

def insert(node, data):
    # Function to insert a new element into the binary search tree
    if node is None:
        return TreeNode(data)
    if data > node.data:
        node.right = insert(node.right, data)
    elif data < node.data:
        node.left = insert(node.left, data)
    return node

def delete(node, data):
    # Function to delete an element from the binary search tree
    if node is None:
        print("Element Not Found")
    elif data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.right and node.left:
            temp = find_min(node.right)
            node.data = temp.data
            node.right = delete(node.right, temp.data)
        else:
            temp = node
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            del temp

    return node

def search(node, data):
    # Function to search for an element in the binary search tree
    if node is None:
        return None
    if data > node.data:
        return search(node.right, data)
    elif data < node.data:
        return search(node.left, data)
    else:
        return node

def inorder(node):
    # In-order traversal of the binary search tree
    if node is not None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def preorder(node):
    # Pre-order traversal of the binary search tree
    if node is not None:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    # Post-order traversal of the binary search tree
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

def main():
    root = None
    while True:
        print("\n### Binary Search Tree Operations ###")
        print("1 - Creation of BST")
        print("2 - Deleting")
        print("3 - Searching")
        print("4 - Traverse in Inorder")
        print("5 - Traverse in Preorder")
        print("6 - Traverse in Postorder")
        print("7 - Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            elt = int(input("Enter element to be inserted: "))
            root = insert(root, elt)
        elif choice == 2:
            elt = int(input("Enter element to be deleted: "))
            delete(root, elt)
        elif choice == 3:
            elt = int(input("Enter element to be searched: "))
            t = search(root, elt)
            if t is None:
                print("Element NOT found")
        elif choice == 4:
            print("\nBST Traversal in INORDER")
            inorder(root)
        elif choice == 5:
            print("\nBST Traversal in PREORDER")
            preorder(root)
        elif choice == 6:
            print("\nBST Traversal in POSTORDER")
            postorder(root)
        elif choice == 7:
            print("\n\nTerminating\n\n")
            break
        else:
            print("\nInvalid Option! Try Again!")

if __name__ == "__main__":
    main()
