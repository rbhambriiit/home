
class Node(object):
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def build_tree(lines):
    total_nodes = int(lines[0].strip())
    # print total_nodes

    # build tree as list
    tree = [-1 for _ in xrange(total_nodes)]
    tree[0] = 1
    # print tree

    for index,l in enumerate(lines[1:total_nodes+1]):
        left,right = [int(s) for s in l.strip().split()]
        # print index,left,right

        if left > 0:
            tree[2*index+1] = left

        if right > 0:
            tree[2*index+2] = right

        # print tree

    return tree



with open('input_tree') as f:
    lines = f.readlines()
    # print lines

    tree = build_tree(lines)
    print 'Built tree:',tree
