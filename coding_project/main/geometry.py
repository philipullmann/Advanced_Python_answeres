import numpy as np
import utils
import pandas as pd


class geometries:
	
    def __init__(self, center):
        self.x, self.y, self.z = center
        self.center = center

class sphere(geometries):
	
    def __init__(self, center, radius):

        super().__init__(center)
        self.radius = radius
        
    def compute_sphere(self, atomlist):

        distances = atomlist.apply(lambda row: utils.euclidean_distance(row, np.array([self.x, self.y, self.z])), axis=1)

        filter_atomlist = atomlist[distances < self.radius]

        return filter_atomlist
        
        
        
class cube(geometries):
    
    def __init__(self, center, length: float):

        super().__init__(center)
        self.length = length
        
    def compute_cube(self, atomlist):
        """Compute cube with ligand atom as center and search for protein atoms inside this cube

        Args:
            atomlist (pd.DataFrame): Protein atoms to iterate through

        Returns:
            pd.DataFrame: Coordinates of atoms in cube boarders defined by length
        """


        cube_boarders_min = [self.x -1/2*self.length, self.y -1/2*self.length,
                             self.z - 1/2*self.length]        
        

        cube_boarders_max = [self.x +1/2*self.length, self.y +1/2*self.length,
                             self.z + 1/2*self.length]
        
        atomlist = atomlist[(atomlist["X"] > cube_boarders_min[0]) & 
                            (atomlist["X"] < cube_boarders_max[0])]

        atomlist = atomlist[(atomlist["Y"] > cube_boarders_min[1]) & 
                            (atomlist["Y"] < cube_boarders_max[1])]
        
        atomlist = atomlist[(atomlist["Z"] > cube_boarders_min[2]) & 
                            (atomlist["Z"] < cube_boarders_max[2])]

        return atomlist
        
    

class cone(geometries):

    def __init__(self, center, bs_center, length, angle):

        super().__init__(center)
        self.length = length
        self.angle = angle
        self.bs_center = bs_center

    def compute_cone(self, atomlist):

        radius, theta, phi = utils.euclid2spherical(self.center, self.bs_center)

        # First check if atom is even possibly part of cone (distance < surface line!
        # Reduce Computational time
        max_distance = self.length/np.cos(np.deg2rad(self.angle))
        distances = atomlist.apply(lambda row: utils.euclidean_distance(row, np.array([self.x, self.y, self.z])), axis=1)
        filter_atomlist = atomlist[distances < max_distance]

        # Compute spherical coordinates between center atom and all protein atoms 
        sph_coord = filter_atomlist.apply(lambda row: utils.euclid2spherical(row, np.array([self.x, self.y, self.z])), axis=1)
        sph_df = pd.DataFrame(sph_coord.tolist(), columns=['r', 'theta', 'phi'], index=sph_coord.index)

        # Filter cone
        
        # Defines angle boundares. Modulo to account for 179->180->-179

        print(sph_df)

        theta_bound_lower = (theta - self.angle/2) % 360
        theta_bound_upper = (theta + self.angle/2) % 360


        phi_bound_lower = (phi - self.angle/2) % 360
        phi_bound_upper = (phi + self.angle/2) % 360




        #print(sph_df)