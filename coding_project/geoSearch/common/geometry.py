import numpy as np
import pandas as pd

from . import utils 

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

        # Compute radius and angles between basis atom (e.g. Carbon) and center atom (always hydrogen)
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
        # Normalize angles (basis is theta, phi)

        theta_ls = sph_df["theta"]
        phi_ls = sph_df["phi"]

        norm_theta, norm_phi= utils.normalize_angles(theta_ls, phi_ls, theta, phi)
        sph_df["theta"], sph_df["phi"] = norm_theta, norm_phi

        # Filter angles outside of cone
        sph_df = sph_df[(sph_df["theta"])**2 + (sph_df["phi"])**2 < (self.angle/2)]

        # Filter if angles and radius do exceed cone borders

        theta_sinus= np.abs(np.sin(0.5*np.pi*(sph_df["theta"]/(0.5*self.angle))))
        phi_sinus = np.abs(np.sin(0.5*np.pi*(sph_df["phi"]/(0.5*self.angle))))                  

        radius_cutoff = self.length + ((max_distance - self.length) * theta_sinus * phi_sinus)
        sph_df = sph_df[sph_df["r"] < radius_cutoff]


        return sph_df



class mandelbulb(geometries):

    def __init__(self, center, power, resolution):

        super().__init__(center)
        self.max_iter = resolution
        self.power = power

    
    def compute_mandelbulb(self, atomlist):

        # Normalize to center = (0,0,0)
        atomlist = atomlist - self.center

        mandel_coord = atomlist.apply(lambda z : utils.iterate_mandelbulb(self.max_iter, z, self.power, escape_radius=10000000), axis=1)

        mandel_coord = mandel_coord[mandel_coord==True]

        return mandel_coord
