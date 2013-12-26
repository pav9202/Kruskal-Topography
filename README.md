Kruskal-Topography
==================
Code to map out the topography of an image using Kruskals algorithm. 

We take advantage of the fact that during iterations of Kruskal's minimum spanning tree algorithm you form forests rather than trees as in Prim's. As such you may form a topography of an image by mapping each iteration of Kruskals to a layer on a 3-dimensional mapping.

A result is shown here for an image of a person on a white background. The visualization is a heatmap of the values generated for each pixel. Going from low to high, blue to red.

<img src="/john.png" align="right" width="300px" />
<img src="/john_top.png" align="right" width="300px" />
