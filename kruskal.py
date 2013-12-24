from PIL import Image, ImageFilter

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

graph = {
        'vertices': [],
        'edges': set([])
        }

#print(kruskal(graph) == minimum_spanning_tree)

try:
    original = Image.open("Lenna.png")
except:
    print "Unable to load image"

width,height = original.size
for i in range(0,width):
    for j in range(0,height):
        r, g, b = original.getpixel((i, j))
        n = r*(pow(256,2)) + g*256 + b # Convert RGB to an integer representation
        graph['vertices'].append(str(n)) #str((i*width)+j) # Add RBG integer value of pixel to the graph as a vertex
        #add Edges to the graph that represent differences between pixels
        if(i>0):
            v = graph['vertex'][((i-1)*width)+j]
            graph['edges'].add((abs(n-int(v)),str(n),v))
        if(i<width-1):
            v = graph['vertex'][((i+1)*width)+j]
            graph['edges'].add((abs(n-int(v)),str(n),v))
        if(j>0):
            v = graph['vertex'][(i*width)+(j-1)]
            graph['edges'].add((abs(n-int(v)),str(n),v))
        if(j<height-1):
            v = graph['vertex'][(i*width)+(j+1)]
            graph['edges'].add((abs(n-int(v)),str(n),v))
        




