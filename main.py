# uruchomienie programu: python program.py --tree BST
#
#
#

import sys
import argparse

class Node: #klasa tworząca nowy typ danych - wierzchołek
    def __init__(self, key): # konstruktor pozwalający stworzyc nowy obiekt klasy
        self.left = None # jego lewe dziecko
        self.right = None # jego prawe dziecko
        self.val = key # warttosc wierzcholka
        
        
def help():
    print("Help Show this message")
    print("Print Print the tree using In-order, Pre-order, Post-order")
    print("Remove Remove elements of the tree")
    print("Delete Delete whole tree")
    print("Export Export the tree to tikzpicture")
    print("Rebalance Rebalance the tree")
    print("Exit Exits the program (same as ctrl+D)")


def insert(root, key): #funkcja czytajaca wierzcholek BST i ustawiająca go w odpowiednim miejscu w zaleznosci od jego wartosci
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
    parser = argparse.ArgumentParser() #odpalenie programu przy pomocy komendy
    parser.add_argument("--tree", type=str, help="Type of the tree")
    args = parser.parse_args() #

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

        print("action> ", end="")
        action = input().strip()
        if action == "Help":
            help()
        
        
        # print("Inorder traversal of the BST is: ")
        # inorder(root)

if __name__ == "__main__":
    main()
