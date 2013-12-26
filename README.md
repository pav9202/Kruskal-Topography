Kruskal-Topography
==================
Code to map out the topography of an image using Kruskals algorithm. 

We take advantage of the fact that during iterations of Kruskal's minimum spanning tree algorithm you form forests rather than trees as in Prim's. As such you may form a topography of an image by mapping each iteration of Kruskals to a layer on a 3-dimensional mapping.

A result is shown here for an image of a person on a white background. The visualization is a heatmap of the values generated for each pixel. Going from low to high, blue to red.

<img src="/john.png" align="center" width="300px" />
<img src="/john_top.png" align="center" width="450px" />

Another test image: 
<img src="/personInFocus.png" align="center" width="300px" />

Heatmap: <img src="/personInFocus_top.png" align="center" width="450px" />

And with a little thresholding: <img src="/personInFocus_top_thresholded.png" align="center" width="450px" />


The image is not mine and was taken from: http://www.nashvilleinjuryattorneysblog.com/Jonathan%20white%20background.JPG
