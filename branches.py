class Branch():
    def __init__(self, root=None):
        self.root = root
        self.branches = []

    def addBranch(self):
        self.branches.append(Branch(self))

#getDepth method performs depth first search using recursion to return depth of tree
def getDepth(node):
    #base case, there are no branches from current node
    if len(node.branches) == 0:
        return 1

    return max([getDepth(branch) for branch in node.branches], default=0) + 1

def main():
    #constructing a sample tree with depth of 4
    base_node = Branch()
    base_node.addBranch()
    base_node.addBranch()
    base_node.addBranch()
    base_node.branches[0].addBranch()
    base_node.branches[0].addBranch()
    base_node.branches[1].addBranch()
    base_node.branches[0].branches[0].addBranch()
    base_node.branches[0].branches[0].branches[0].addBranch()
    

    print(getDepth(base_node))




if __name__ == "__main__":
    main()