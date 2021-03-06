Kruskal-Topography
==================
Noticed this property of Kruskal's algorithm a while back and decided to code it up. 

Code to map out the topography of an image using Kruskals algorithm. 

We take advantage of the fact that during iterations of Kruskal's minimum spanning tree algorithm you form forests rather than trees as in Prim's. As such you may form a topography of an image by mapping each iteration of Kruskals to a layer on a 3-dimensional mapping.

A result is shown here for an image of a person on a white background. The visualization is a heatmap of the values generated for each pixel. Going from low to high, blue to red.

<img src="/john.png" align="center" width="300px" />
<img src="/john_top.png" align="center" width="450px" />

Another test image: 
<img src="/personInFocus.png" align="center" width="300px" />

Heatmap: <img src="/personInFocus_top.png" align="center" width="450px" />

And with a little thresholding: <img src="/personInFocus_top_thresholded.png" align="center" width="450px" />

Now those were the results of using the different of pixel values as the edge weights. When using values of one of the pixels on the edge we get the resultant image.

<img src="/personInFocus_top2.png" align="center" width="450px" />
<img src="/personInFocus_top2_thresholded.png" align="center" width="450px" />
<img src="/john_top2_thresholded.png" align="center" width="450px" />



The images are not mine and was taken from: 
http://cpn.canon-europe.com/files/education/infobank/focus_points/a_single_focusing_point/fp_Focus_points3.jpg
http://www.nashvilleinjuryattorneysblog.com/Jonathan%20white%20background.JPG


