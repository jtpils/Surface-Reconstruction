# Surface Reconstruction
Repo of code written for surface reconstruction from point clouds  
## Pipeline
1. Input: unoriented point clouds (xyz values, and optionally RGB values in .ply format)
2. Optionally, chunk ply and use the smaller chunks of ply to run step 3 and 4 on different nodes on a computing cluster. Use ```ChunkPLY``` provided by KBH06.  
```./ChunkPLY --in input-filename.ply --out output-filename.chunks --width 200``` 
3. Normal estimation: Needed because unless the point cloud has very high sampling density and is noise-free, which Delaunay-based reconstruction methods would work fine, reliable normals and oriented normals especially at each point are crucial for surface reconstruction. Use ```ComputeNormals.py``` to add normals information to .ply file if it does not contain normals.
4. Use Poisson Reconstruction algorithm [KBH06](http://hhoppe.com/poissonrecon.pdf) at depth => 10 (14 preferred).   
```./PoissonRecon --in input-filename.ply --out output-filename.ply --depth 14 ```
5. Evaluate the resulting mesh model in MeshLab or MeshMixer
 
