# uruchomienie programu: python program.py --tree BST / AVL
#
#ToDO:
#
#Pomiar czasu - do sprawozdania
#
#AVL
#Implementacja
#Rebalance
#

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

    def find_min_max(self): #zwraca wartosc wierzcholkow
        min_val = self.val
        max_val = self.val

        if self.left:
            min_val = self.left.find_min_max()[0]
        if self.right:
            max_val = self.right.find_min_max()[1]

        return min_val, max_val
    
    def search(self, key): #funkcja pomocnicza sprawdzający czy dany wierzchołek istnieje w drzewie
        if self is None or self.val == key:
            return self

        if self.val < key:
            return self.right.search(key) if self.right else None

        return self.left.search(key) if self.left else None
    
    def minValueNode(self): #zwraca najmniejszy wierzcholek
        current = self

        while(current.left is not None):
            current = current.left

        return current
    
    
    def remove(self, key):
        if self is None:
            return self
        if key < self.val:
            if self.left:
                self.left = self.left.remove(key)
        elif key > self.val:
            if self.right:
                self.right = self.right.remove(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            temp = self.right.minValueNode()
            self.val = temp.val
            self.right = self.right.remove(temp.val)
        return self
    
    def remove_all_post_order(self, first=True):
        if first:
            print("Deleting: ", end="")
        if self.left:
            self.left = self.left.remove_all_post_order(False)
        if self.right:
            self.right = self.right.remove_all_post_order(False)
        print(self.val, end=' ')
        return None
    
    
    def export(self, tex_file):
        if not self.left and not self.right:
            tex_file.write(f"node {{{self.val}}}")
        else:
            tex_file.write(f"node {{{self.val}}}\n")
            if self.left:
                tex_file.write("    child { ")
                self.left.export(tex_file)
                tex_file.write(" } ")
            else:
                tex_file.write("    child[missing] ")
        
            if self.right:
                tex_file.write("    child { ")
                self.right.export(tex_file)
                tex_file.write(" } ")
            else:
                tex_file.write("    child [missing] ")


        
        
def help():
    print("Help         -   Show this message")
    print("FindMinMax   -   Finding minimum and maximum in the tree")
    print("Print        -   Print the tree using In-order, Pre-order, Post-order")
    print("Remove       -   Remove elements of the tree")
    print("RemoveAll    -   Delete whole tree")
    print("Export       -   Export the tree to tikzpicture")
    print("Rebalance    -   Rebalance the tree - only AVL")
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



def main():
    parser = argparse.ArgumentParser() #odpalenie programu przy pomocy komendy
    parser.add_argument("--tree", type=str, help="Type of the tree")
    args = parser.parse_args() #

    if args.tree == "BST":
        print("nodes> ", end="")
        n = int(input())
        print("insert> ", end="")
        nums = list(map(int, input().split()))

        if len(nums) == n:
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

                elif action == "Remove":
                    key = int(input("Enter the key to remove: "))
                    if root is not None and root.search(key) is not None:
                        root = root.remove(key)
                        if root is not None:
                            print("Node with key", key, "has been removed.")
                        else:
                            print("The tree is now empty.")
                    else:
                        print("Node with key", key, "does not exist in the tree.")

                elif action == "RemoveAll":
                    if root is not None:
                        root = root.remove_all_post_order()
                        print("\n All nodes have been removed from the tree.")
                    else:
                        print("Drzewo jest puste")

                elif action == "Export":
                    if root is not None:
                        with open("tree.tex", "w") as tex_file:
                            tex_file.write("\\documentclass{standalone}\n")
                            tex_file.write("\\usepackage{tikz}\n")
                            tex_file.write("\\begin{document}\n")
                            tex_file.write("\\begin{tikzpicture}\n")
                            tex_file.write("[->,>=stealth',level/.style={sibling distance = 7cm/#1, level distance = 1.5cm}]\n")
                            tex_file.write("\\")
                            root.export(tex_file)
                            tex_file.write(";\n")
                            tex_file.write("\\end{tikzpicture}\n")
                            tex_file.write("\\end{document}\n")
                        print("Export to file tree.tex succeeded")
                    else:
                        print("The tree is empty")
                
                elif action == "Exit":
                    break

        else:
            print("Ilość podanych wierzchołków nie jest równa n")

        
        

    if args.tree == "AVL":
        print("nodes> ", end="")
        n = int(input())
        print("insert> ", end="")
        nums = list(map(int, input().split()))
        if len(nums) == n:
            print("TODO")
        else:
            print("Ilość podanych wierzchołków nie jest równa n")

if __name__ == "__main__":
    main()

