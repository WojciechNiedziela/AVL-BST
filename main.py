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

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.val, end=' ')
        if self.right:
            self.right.print_inorder()

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.val, end=' ')

    def print_preorder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def find_min_max(self):
        min_val = self.val
        max_val = self.val

        if self.left:
            min_val = self.left.find_min_max()[0]
        if self.right:
            max_val = self.right.find_min_max()[1]

        return min_val, max_val


        
        
def help():
    print("Help         -   Show this message")
    print("FindMinMax   -   Finding minimum and maximum in the tree")
    print("Print        -   Print the tree using In-order, Pre-order, Post-order")
    print("Remove       -   Remove elements of the tree")
    print("RemoveAll    -   Delete whole tree")
    print("Export       -   Export the tree to tikzpicture")
    print("Rebalance    -    Rebalance the tree")
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

def RemoveAll(root):
    root = None
    return root



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

        while True:
            print("action> ", end="")
            action = input().strip()
            if action == "Help":
                help()
            elif action == "FindMinMax":
                if root is not None:
                    min_val, max_val = root.find_min_max()
                    print("Minimum value in the BST is: ", min_val)
                    print("Maximum value in the BST is: ", max_val)
                else:
                    print("Drzewo jest puste")
            elif action == "Print":
                if root is not None:
                    print("Inorder: ", end="")
                    root.print_inorder()
                    print("\nPostorder: ", end="")
                    root.print_postorder()
                    print("\nPreorder: ", end="")
                    root.print_preorder()
                    print()
                else:
                    print("Drzewo jest puste")
            elif action == "RemoveAll":
                root = RemoveAll(root)
                print("All nodes have been removed from the tree.")
            elif action == "Exit":
                break


if __name__ == "__main__":
    main()

