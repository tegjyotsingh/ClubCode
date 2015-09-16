"""
Basic Binary Tree Library

"""
import random

# Node class for tree node
class node:

    def __init__(self):
        self.data=None
        self.left=None
        self.right=None

# Binary Tree class
class BinaryTree:

    def __init__(self):
        self.root=None

    # inserts data randomly by deciding whether to go left or  right at each point
    def insert(self,data):
        if self.root==None:
            self.root=node()
            self.root.data=data
        else:
            temp=self.root
            temp_node=node()
            temp_node.data=data
            temp_prev=temp
            flag=1
            while temp!=None:
                temp_prev=temp
                if random.random()>=0.5:
                    temp=temp.right
                    flag=1
                else:
                    temp=temp.left
                    flag=0
            if flag==1:
                temp_prev.right=temp_node
            else:
                temp_prev.left=temp_node

    def traverse(self,current_root,order):
        temp=current_root
        if current_root==self.root:
            print "\n"+order
        if order=="inorder":
            #print LNR
            if temp!=None:
                self.traverse(temp.left,"inorder")
                print temp.data,
                self.traverse(temp.right,"inorder")
        elif order=="preorder":
            #print NLR
            if temp!=None:
                print temp.data,
                self.traverse(temp.left,"preorder")
                self.traverse(temp.right,"preorder")
        elif order=="postorder":
            #print LRN
            if temp!=None:
                self.traverse(temp.left,"postorder")
                self.traverse(temp.right,"postorder")
                print temp.data,

    def create_from_list(self,list):
        for i in list:
            self.insert(i)

    def count_nodes(self,current_root,count):
        #similar to traversal
        if current_root!=None:
            count=self.count_nodes(current_root.left,count)+1+self.count_nodes(current_root.right,count)
        return count
    def create_from_traversal(self,inorder,start,end,preorder,index):
        #take first preorder element make node
        if start>end:
            return [index,None]
        temp_node=node()
        temp_node.data=preorder[index]
        index=index+1
        if start==end:
            return [index,temp_node]
        else:
            #find element in inorder
            temp=preorder[index-1]
            count=0
            for i in range(start,end+1):
                if inorder[i]== temp:
                    count=i
            [index,temp_node.left]=self.create_from_traversal(inorder,start,count-1,preorder,index)
            [index,temp_node.right]=self.create_from_traversal(inorder,count+1,end,preorder,index)
        return [index,temp_node]


    def height(self,current_node="root", current_height=0):
        if current_node is "root":
            current_node=self.root
        if current_node is None:
            return 0
        return max(self.height(current_node.left), self.height(current_node.right))+1

    def count_max_leaves(self, height):
        return  pow(2,(height-1))

    def print_tree(self):
        height=self.height()
        number_leafs=self.count_max_leaves(height)
        print_list=[[' ' for i in range(number_leafs+number_leafs/2)] for j in range(height)]
        self.print_tree_matrix(self.root, print_list, start=0, end=len(print_list[0]), level=0)
        for row in print_list:
            for element in row:
                print element,
            print

    def print_tree_matrix(self, root, print_list, start, end, level):
        if root is None:
            return
        else:
            middle=int(((start+end)/2.0))
            print_list[level][middle]=root.data
            self.print_tree_matrix(root.left, print_list, start=start, end=middle, level=level+1)
            self.print_tree_matrix(root.right, print_list, start=middle, end=end, level=level+1)

def Test_print():
    list1=[1,2,3, 4, 5, 6, 7, 8]
    b1=BinaryTree()
    b1.create_from_list(list1)
    print b1.height()
    b1.print_tree()
    b1.traverse(b1.root,"inorder")
    b1.traverse(b1.root,"preorder")
    b1.traverse(b1.root,"postorder")

def Test():
    #testcases
    list1=[1,2,3,4,5,6,7,8]
    b1=BinaryTree()
    b1.create_from_list(list1)
    b1.traverse(b1.root,"inorder")
    b1.traverse(b1.root,"preorder")
    b1.traverse(b1.root,"postorder")
    #function Calls

    print "count="+str(b1.count_nodes(b1.root,0))
    inorder1=[6,5,7,3,4,1,2,8]
    preorder1=[1,3,5,6,7,4,2,8]
    postorder1=[6,7,5,4,3,8,2,1]
    b2=BinaryTree()
    [index,b2.root]=b2.create_from_traversal(inorder1,0,len(inorder1)-1,preorder1,0)
    b2.traverse(b2.root,"inorder")
    b2.traverse(b2.root,"preorder")
    b2.traverse(b2.root,"postorder")
if __name__=="__main__":
    #Test()
    Test_print()

