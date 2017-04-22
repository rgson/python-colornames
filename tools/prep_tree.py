#!/usr/bin/env python3

"""
Builds the color search tree.

Building the octree takes a few seconds. As the result is always the same,
we generate it ahead of time and hard-code it as a constant instead.
The octree is shrunk by flattening branches with less than two ancestors.
"""

import json


def octree(depth):
    return [octree(depth-1) for i in range(8)] if depth else None

def octree_index(r, g, b, d):
    return ((r >> d & 1) << 2) | ((g >> d & 1) << 1) | (b >> d & 1)

def shrink(node):
    MULTI = 'MULTI'
    if type(node) is not list:
        return node
    res = None
    for i, child in enumerate(node):
        val = shrink(child)
        if val == MULTI:
            res = MULTI
        else:
            node[i] = val
            if val is not None:
                res = val if res is None else MULTI
    return res


colors = json.load(open('colors.json', 'r'))
tree = octree(8)
for name, rgb in colors.items():
    i,j,k,l,m,n,o,p = [octree_index(*rgb, d) for d in reversed(range(8))]
    tree[i][j][k][l][m][n][o][p] = name
shrink(tree)
print(tree)
