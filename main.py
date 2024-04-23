import sys
import argparse

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tree", type=str, help="Type of the tree")
    args = parser.parse_args()

    if args.tree == "BST":
        print("nodes> ", end="")
        n = int(input())
        print("insert> ", end="")
        nums = list(map(int, input().split()))
        print("Inserting: ", end="")
        print(*nums, sep=", ")

        root = None
        for num in nums:
            root = insert(root, num)

        print("Inorder traversal of the BST is: ")
        inorder(root)

if __name__ == "__main__":
    main()
