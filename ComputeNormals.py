########################
## ComputeNormals.py 
## load a point cloud, estimate normals using knn, and write the new point cloud to file
## uses pyntcloud library
## Ty Feng | June 10, 2019
########################

from pyntcloud import PyntCloud

in_file = input("What is the input file name? ===>")
k_input = input("What is the number of nearest neighbors used to compute normals? (e.g. 6) ===>")
k = int(k_input)
if (in_file != ""):
	try:
		point_cloud = PyntCloud.from_file(in_file)
		print ("loaded " + in_file + " as a point cloud")
		k_neighbors = point_cloud.get_neighbors(k)
		print ("Using " + k_input + " nearest neighbors to estimate normals...")
		normals = point_cloud.add_scalar_field("normals", k_neighbors=k_neighbors)
		print ("Normals estimated for each point")
		print ("Writing ply with normals to file...")
		point_cloud.to_file(in_file+"-pyntcloud_"+k_input+"NN.ply")
		print ("Successfully written ply with normals to file: " + in_file+"-pyntcloud_"+k_input+"NN.ply")
	except:
		print ("ERROR: input file " + in_file + " not correct OR k NN not correct!")
else: 
	print ("Goodbye!")
