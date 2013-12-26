from PIL import Image, ImageFilter
import copy
from operator import itemgetter

# parent = dict()
# rank = dict()

# def make_set(vertice):
#     parent[vertice] = vertice
#     rank[vertice] = 0

# def find(vertice):
#     if parent[vertice] != vertice:
#         parent[vertice] = find(parent[vertice])
#     return parent[vertice]

# def union(vertice1, vertice2):
#     root1 = find(vertice1)
#     root2 = find(vertice2)
#     if root1 != root2:
#         if rank[root1] > rank[root2]:
#             parent[root2] = root1
#         else:
#             parent[root1] = root2
#             if rank[root1] == rank[root2]: rank[root2] += 1

# def kruskal(graph):
#     for vertice in graph['vertices']:
#         make_set(vertice)

#     minimum_spanning_tree = set()
#     edges = list(graph['edges'])
#     edges.sort()
#     print len(edges)
#     for edge in edges:
#         weight, vertice1, vertice2, vertice1Loc, vertice2Loc = edge
#         if find(vertice1) != find(vertice2):
#             union(vertice1, vertice2)
#             minimum_spanning_tree.add(edge)
            
#     return minimum_spanning_tree

# graph = {
#         'vertices': [],
#         'edges': set([])
#         }
# # minimum_spanning_tree = set([
# #             (1, 'A', 'B'),
# #             (2, 'B', 'D'),
# #             (1, 'C', 'D'),
# #             ])

# #print(kruskal(graph) == minimum_spanning_tree)

# for i in range(0,width):
#     for j in range(0,height):
#         r, g, b = original.getpixel((i, j))
#         n = r*(pow(256,2)) + g*256 + b # Convert RGB to an integer representation
#         graph['vertices'].append(str(n)) # Add RBG integer value of pixel to the graph as a vertex
# print len(graph['vertices'])
# raw_input()

# for i in range(0,width):
#     for j in range(0,height):
#         #add Edges to the graph that represent differences between pixels
#         if(i>0):
#             v = graph['vertices'][((i-1)*width)+j]
#             n =int(graph['vertices'][(i*width)+j])
#             graph['edges'].add((abs(n-int(v)),str(n),v,str(i)+','+str(j),str((i-1))+','+str(j)))
#         if(i<(width-1)):
#             v = graph['vertices'][((i+1)*width)+j]
#             n =int(graph['vertices'][(i*width)+j])
#             graph['edges'].add((abs(n-int(v)),str(n),v,str(i)+','+str(j),str((i+1))+','+str(j)))
#         if(j>0):
#             v = graph['vertices'][(i*width)+(j-1)]
#             n =int(graph['vertices'][(i*width)+j])
#             graph['edges'].add((abs(n-int(v)),str(n),v,str(i)+','+str(j),str(i)+','+str((j-1))))
#         if(j<height-1):
#             v = graph['vertices'][(i*width)+(j+1)]
#             n =int(graph['vertices'][(i*width)+j])
#             graph['edges'].add((abs(n-int(v)),str(n),v,str(i)+','+str(j),str(i)+','+str((j+1))))

class DisjointSet(dict):
    def add(self, item):
        self[item] = item
 
    def find(self, item):
        parent = self[item]
 
        while self[parent] != parent:
            parent = self[parent]
 
        self[item] = parent
        return parent
 
    def union(self, item1, item2):
        self[item2] = self[item1]

def kruskal( nodes, edges ):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add( n )
 
    sz = len(nodes) - 1
 
    for e in sorted( edges, key=itemgetter( 2 ) ):
        n1, n2, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            if sz == 0:
                return mst
            forest.union(t1, t2)
 
 
#test   
 
nodes = []
#list( "ABCDEFG" )
edges = [] 
# ("A", "B", 7), ("A", "D", 5),
#           ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
#       ("C", "E", 5),
#       ("D", "E", 15), ("D", "F", 6),
#       ("E", "F", 8), ("E", "G", 9),
#       ("F", "G", 11)]
verticesValues = []

try:
    original = Image.open("john.png")
except:
    print "Unable to load image"

width,height = original.size
for i in range(0,width):
    for j in range(0,height):
        r, g, b,a = original.getpixel((i, j))
        n = r*(pow(256,2)) + g*256 + b # Convert RGB to an integer representation
        verticesValues.append(str(n)) # Add RBG integer value of pixel to the graph as a vertex
print 'Length of verticesValues:'
print len(verticesValues)
print '(press enter)'
raw_input()

for i in range(0,width):
    for j in range(0,height):
        #add Edges to the graph that represent differences between pixels
        nodes.append(str(i)+','+str(j))
        if(i>0):
            v = verticesValues[((i-1)*height)+j]
            n =int(verticesValues[(i*height)+j])
            edges.append((str(i)+','+str(j),str((i-1))+','+str(j),abs(n-int(v))))
        if(i<(width-1)):
            v = verticesValues[((i+1)*height)+j]
            n =int(verticesValues[(i*height)+j])
            edges.append((str(i)+','+str(j),str((i+1))+','+str(j),abs(n-int(v))))
        if(j>0):
            v = verticesValues[(i*height)+(j-1)]
            n =int(verticesValues[(i*height)+j])
            edges.append((str(i)+','+str(j),str(i)+','+str((j-1)),abs(n-int(v))))
        if(j<height-1):
            v = verticesValues[(i*height)+(j+1)]
            n =int(verticesValues[(i*height)+j])
            edges.append((str(i)+','+str(j),str(i)+','+str((j+1)),abs(n-int(v))))

print 'Length of nodes:'
print len(nodes)
print '481,0' in nodes
print '(press enter)'
raw_input()

MST = kruskal(nodes,edges)

print MST 

pixelValues = [[None for x in range(height)] for y in range(width)] #[height][width]
pixelsCovered = set()
count = 0
for t in MST:
    pixelsCovered.add(t[0])
    pixelsCovered.add(t[1])
    a,b = t[0].split(',')
    if(pixelValues[int(a)][int(b)]==None):
        pixelValues[int(a)][int(b)] = count
    a,b = t[1].split(',')
    if(pixelValues[int(a)][int(b)]==None):
        pixelValues[int(a)][int(b)] = count
    count+=1

print '\n'
print count
print len(pixelsCovered)
print (width*height)
print '(press enter)'
raw_input()


saved = open('topography.txt','w')
for i in range(0,width):
    for j in range(0,height):
        saved.write(str(pixelValues[i][j])+',')
    saved.write('\n')
saved.close()





