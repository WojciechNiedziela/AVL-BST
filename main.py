# uruchomienie programu: python program.py --tree BST / AVL

import argparse, time, math

class Node: 
    def __init__(self, key): 
        self.left = None 
        self.right = None
        self.val = key

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


class AVLNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1

    def update_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = max(left_height, right_height) + 1

    def get_balance(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height

    def get_tree_size(self):
        # Poprawiona wersja liczenia rozmiaru drzewa
        if self is None:
            return 0
        left_size = self.left.get_tree_size() if self.left else 0
        right_size = self.right.get_tree_size() if self.right else 0
        return 1 + left_size + right_size
    
    def balance_tree_dsw(self):
        # Tworzenie drzewa w kształcie listwy
        head = self.create_vined_tree(self)
        
        # Obliczenie rozmiaru drzewa
        size = head.get_tree_size()
        
        # Równoważenie drzewa
        root = self.rebalance_vined_tree(head, size)
        return root
    # Operacje rotacji]
    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self.update_height()
        new_root.update_height()
        return new_root

    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self.update_height()
        new_root.update_height()
        return new_root

    # Rotacje lewo-prawo i prawo-lewo
    def rotate_left_right(self):
        self.left = self.left.rotate_left()
        return self.rotate_right()

    def rotate_right_left(self):
        self.right = self.right.rotate_right()
        return self.rotate_left()

    # Operacja wstawiania z zachowaniem równowagi AVL
    def insert(self, key):
        if key < self.val:
            if self.left:
                self.left = self.left.insert(key)
            else:
                self.left = AVLNode(key)
        else:
            if self.right:
                self.right = self.right.insert(key)
            else:
                self.right = AVLNode(key)

        self.update_height()
        return self.balance()

    # Przywracanie równowagi
    def balance(self):
        balance = self.get_balance()

        if balance > 1:
            if self.left and self.left.get_balance() < 0:
                return self.rotate_left_right()
            else:
                return self.rotate_right()

        if balance < -1:
            if self.right and self.right.get_balance() > 0:
                return self.rotate_right_left()
            else:
                return self.rotate_left()

        return self

    # Metody do drukowania węzłów w różnych porządkach
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

    # Metody do eksportu do TikZ
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

    # Metoda do znajdowania najmniejszego elementu w drzewie
    def minValueNode(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    # Usuwanie elementów
    def remove(self, key):
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

            min_right = self.right.minValueNode()
            self.val = min_right.val
            self.right = self.right.remove(min_right.val)
        
        self.update_height()
        return self.balance()

    # Operacja do usuwania całego drzewa
    def delete_all_postorder(self):
        if self.left:
            self.left = self.left.delete_all_postorder()
        if self.right:
            self.right = self.right.delete_all_postorder()
        return None

        
def help():
    print("Help         -   Show this message")
    print("FindMinMax   -   Finding minimum and maximum in the tree")
    print("Print        -   Print the tree using In-order, Pre-order, Post-order")
    print("Remove       -   Remove elements of the tree")
    print("RemoveAll    -   Delete whole tree")
    print("Export       -   Export the tree to tikzpicture")
    print("Rebalance    -   Rebalance the tree")
    print("Exit         -   Exits the program (same as ctrl+D)")

def insert(root, key): 
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def AVLToVine(grand: Node) -> int:
    count = 0
    tmp = grand.right
    while tmp:
 
        if tmp.left:
            oldTmp = tmp
            tmp = tmp.left
            oldTmp.left = tmp.right
            tmp.right = oldTmp
            grand.right = tmp

        else:
            count += 1
            grand = tmp
            tmp = tmp.right
 
    return count
 
def AVLcompress(grand: AVLNode, m: int) -> None:
    tmp = grand.right
    for i in range(m):
        oldTmp = tmp
        tmp = tmp.right
        grand.right = tmp
        oldTmp.right = tmp.left
        tmp.left = oldTmp
        grand = tmp
        tmp = tmp.right
 
def balanceAVL(root: AVLNode) -> Node:
 
    grand = AVLNode(0)
    grand.right = root
    count = AVLToVine(grand)
    h = int(math.log2(count + 1))
    m = pow(2, h) - 1
    AVLcompress(grand, count - m)
    for m in [m // 2**i for i in range(1, h + 1)]:
        AVLcompress(grand, m)

    return grand.right

def bstToVine(grand: Node) -> int: #funkcja tworząca drzewo w kształcie winorośli
    count = 0
    tmp = grand.right
    while tmp:
 
        if tmp.left:
            oldTmp = tmp
            tmp = tmp.left
            oldTmp.left = tmp.right
            tmp.right = oldTmp
            grand.right = tmp

        else:
            count += 1
            grand = tmp
            tmp = tmp.right
 
    return count
 
def compress(grand: Node, m: int) -> None: #funkcja kompresująca drzewo -> obraca w lewo co drugi element
    tmp = grand.right
    for i in range(m):
        oldTmp = tmp
        tmp = tmp.right
        grand.right = tmp
        oldTmp.right = tmp.left
        tmp.left = oldTmp
        grand = tmp
        tmp = tmp.right
 
def balanceBST(root: Node) -> Node:
 
    grand = Node(0)
    grand.right = root
    count = bstToVine(grand)
    h = int(math.log2(count + 1))
    m = pow(2, h) - 1
    compress(grand, count - m)
    for m in [m // 2**i for i in range(1, h + 1)]:
        compress(grand, m)

    return grand.right

    if not head:
        return None
        
        # Liczba pełnych rotacji do zbalansowania
    full_rotations = size // 2

        # Pierwsza seria rotacji w lewo
    current = head
    parent = None
    for _ in range(full_rotations):
        if current and current.right:
            next_node = current.right
            current.right = next_node.right
            next_node.right = current
            current = next_node
        else:
            break  # Uniknięcie błędów
        
        # Druga seria rotacji z mniejszą liczbą rotacji
    m = full_rotations // 2
    while m > 0:
        current = head
        for _ in range(m):
            if current and current.right:
                next_node = current.right
                current.right = next_node.right
                next_node.right = current
                current = next_node
            else:
                break
        m = m // 2
        
    return head
    
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
                action = input().strip().lower()
                if action == "help":
                    help()

                elif action == "findminmax":
                    if root is not None:
                        min_val, max_val = root.find_min_max()
                        print("Minimum value in the BST is: ", min_val)
                        print("Maximum value in the BST is: ", max_val)
                    else:
                        print("Drzewo jest puste")

                elif action == "print":
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

                elif action == "remove":
                    key = int(input("Enter the key to remove: "))
                    if root is not None and root.search(key) is not None:
                        root = root.remove(key)
                        if root is not None:
                            print("Node with key", key, "has been removed.")
                        else:
                            print("The tree is now empty.")
                    else:
                        print("Node with key", key, "does not exist in the tree.")

                elif action == "removeall":
                    if root is not None:
                        root = root.remove_all_post_order()
                        print("\n All nodes have been removed from the tree.")
                    else:
                        print("Drzewo jest puste")

                elif action == "export":
                    if root is not None:
                        with open("tree.tex", "w") as tex_file:
                            tex_file.write("\\documentclass{standalone}\n")
                            tex_file.write("\\usepackage{tikz}\n")
                            tex_file.write("\\begin{document}\n")
                            tex_file.write("\\begin{tikzpicture}\n")
                            tex_file.write("[->,>=stealth,level/.style={sibling distance = 7cm/#1, level distance = 1.5cm}]\n")
                            tex_file.write("\\")
                            root.export(tex_file)
                            tex_file.write(";\n")
                            tex_file.write("\\end{tikzpicture}\n")
                            tex_file.write("\\end{document}\n")
                        print("Export to file tree.tex succeeded")
                    else:
                        print("The tree is empty")

                elif action == "rebalance":
                    if root is not None:
                        root = balanceBST(root)
                        print("Preorder: ", end="")
                        root.print_preorder()
                        print()
                    else:
                        print("The tree is empty")
                
                elif action == "exit":
                    break

        else:
            print("Ilość podanych wierzchołków nie jest równa n")

    elif args.tree == "AVL":
        print("nodes> ", end="")
        n = int(input())
        print("insert> ", end="")
        nums = list(map(int, input().split()))
        nums.sort()
        def construct_avl_from_sorted_list(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = AVLNode(nums[mid])
            node.left = construct_avl_from_sorted_list(nums[:mid])
            node.right = construct_avl_from_sorted_list(nums[mid + 1:])
            node.update_height()  # Aktualizuj wysokość po każdej operacji
            return node
        
        if len(nums) == n:
            print("Sorted:", ",".join(map(str, nums)))
            print("Median:",sorted(nums)[len(sorted(nums))//2])
            root = construct_avl_from_sorted_list(nums)
            while True:
                print("action> ", end="")
                action = input().strip().lower()
                
                if action == "print":
                    if root is not None:
                        print("In-order:", end=" ")
                        root.print_inorder()
                        print("\nPost-order:", end=" ")
                        root.print_postorder()
                        print("\nPre-order:", end=" ")
                        root.print_preorder()
                        print()
                    else:
                        print("Drzewo jest puste")

                elif action == "help":
                    help()
                
                elif action == "findMinMax":
                    if root is not None:
                        min_node = root.minValueNode()
                        current = root
                        while current.right:
                            current = current.right
                        max_node = current
                        print(f"Min: {min_node.val}\nMax: {max_node.val}")
                    else:
                        print("Drzewo jest puste")

                elif action == "export":
                    if root is not None:
                        with open("tree.tex", "w") as tex_file:
                            tex_file.write("\\documentclass{standalone}\n")
                            tex_file.write("\\usepackage{tikz}\n")
                            tex_file.write("\\begin{document}\n")
                            tex_file.write("\\begin{tikzpicture}\n")
                            tex_file.write("[->,>=stealth,level/.style={sibling distance = 7cm/#1, level distance = 1.5cm}]\n")
                            tex_file.write("\\")
                            root.export(tex_file)
                            tex_file.write(";\n")
                            tex_file.write("\\end{tikzpicture}\n")
                            tex_file.write("\\end{document}\n")
                        print("Export to file tree.tex succeeded")
                    else:
                        print("The tree is empty")

                elif action == "remove":
                    if root is not None:
                        print("remove> ", end="")
                        to_remove = list(map(int, input().split()))
                        for val in to_remove:
                            root = root.remove(val)
                        print("Elements removed")
                    else:
                        print("Cannot remove: tree is empty.")

                elif action == "removeall":
                    if root is not None:
                        root.delete_all_postorder()
                        root = None
                        print("Tree deleted")
                    else:
                        print("Cannot delete: tree is empty.")

                elif action == "rebalance":
                    if root is not None:
                        root = balanceAVL(root)
                        print("Tree rebalanced!")
                    else:
                        print("The tree is empty")
                
                elif action == "Exit":
                    break

                elif action == "exit":
                    break
        else:
            print("Ilość podanych wierzchołków nie jest równa n")

if __name__ == "__main__":
    main()