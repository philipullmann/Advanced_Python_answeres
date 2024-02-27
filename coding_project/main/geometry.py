import numpy as np
from scipy.spatial import distance


class geometries:
	
    def __init__(self, form=str, center=list):
        self.form = form
        self.center.x = center[0]
        self.center.y = center[1]
        self.center.z = center[2]

class sphere(geometries):
	
    def __init__(self, radius):
        super(self).__init__()
        self.radius = radius
        
    def compute_sphere(self, atomlist):
        atomlist[distance.euclidean(atomlist[:], np.array(self.center.x, self.center.y
                                                          self.center.z)) < radius]
        return atomlist
        
        
        
class cube(geometries):
    
    def __init__(self, length):
        super(self).__init__()
        self.length = length
        
    def compute_cube(self, atomlist):
        cube_boarders_min = [self.center.x -1/2*length, self.center.y -1/2*length,
                             self.center.z - 1/2*length]        
        
        cube_boarders_max = [self.center.x +1/2*length, self.center.y +1/2*length,
                             self.center.z + 1/2*length]
        
        atomlist = atomlist[atomlist[0] > cube_boarders_min[0] and 
                            atomlist[0] < cube_boarders_max[0]]
        
        atomlist = atomlist[atomlist[1] > cube_boarders_min[1] and 
                            atomlist[1] < cube_boarders_max[1]]
        
        atomlist = atomlist[atomlist[2] > cube_boarders_min[2] and 
                            atomlist[2] < cube_boarders_max[2]]
        
        return atomlist
        
        
    

#class cone(geometries, length, angle):

