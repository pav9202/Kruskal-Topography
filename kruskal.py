from PIL import Image, ImageFilter
import copy

parent = dict()
rank = dict()

MST_atEachStage=[]

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
    print len(edges)
    for edge in edges:
        weight, vertice1, vertice2, vertice1Loc, vertice2Loc = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
            location = (vertice1Loc, vertice2Loc)
            MST_atEachStage.append(location)
    return minimum_spanning_tree

graph = {
        'vertices': [],
        'edges': set([])
        }
# minimum_spanning_tree = set([
#             (1, 'A', 'B'),
#             (2, 'B', 'D'),
#             (1, 'C', 'D'),
#             ])

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
        graph['vertices'].append(str(n)) # Add RBG integer value of pixel to the graph as a vertex


for i in range(0,width):
    for j in range(0,height):
        #add Edges to the graph that represent differences between pixels
        if(i>0):
            v = graph['vertices'][((i-1)*width)+j]
            n =int(graph['vertices'][(i*width)+j])
            graph['edges'].add((abs(n-int(v)),str(n),v,str(i)+','+str(j),str((i-1))+','+str(j)))
        if(i<(width-1)):
            v = graph['vertices'][((i+1)*width)+j]
            n =int(graph['vertices'][(i*width)+j])
            graph['edges'].add((abs(n-int(v)),str(n),v,str(i)+','+str(j),str((i+1))+','+str(j)))
        if(j>0):
            v = graph['vertices'][(i*width)+(j-1)]
            n =int(graph['vertices'][(i*width)+j])
            graph['edges'].add((abs(n-int(v)),str(n),v,str(i)+','+str(j),str(i)+','+str((j-1))))
        if(j<height-1):
            v = graph['vertices'][(i*width)+(j+1)]
            n =int(graph['vertices'][(i*width)+j])
            graph['edges'].add((abs(n-int(v)),str(n),v,str(i)+','+str(j),str(i)+','+str((j+1))))
      
kruskal(graph)

print len(graph['edges'])
print MST_atEachStage 

pixelValues = [[None for x in range(width)] for y in range(height)] #[height][width]
pixelsCovered = set()
count = 0
for t in MST_atEachStage:
    pixelsCovered.add(t[0])
    pixelsCovered.add(t[1])
    a,b = t[0].split(',')
    # print t
    # print str(a) +','+str(b)
    # print len(pixelsCovered)
    # raw_input()
    if(pixelValues[int(a)][int(b)]==None):
        pixelValues[int(a)][int(b)] = count
    a,b = t[1].split(',')
    if(pixelValues[int(a)][int(b)]==None):
        pixelValues[int(a)][int(b)] = count

    count+=1
    if(len(pixelsCovered)==(width*height)):
        break

print '\n'
print count
print (width*height)
raw_input()
saved = open('topography.txt','w')
print '\n\n\n\n'
print pixelValues

saved.write(pixelValues)






