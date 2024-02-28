from pathlib import Path
import pandas as pd
import numpy as np

from scipy.spatial import distance
from rdkit import Chem



def load_molecule(file_path_mol: str) -> Chem.rdchem.Mol:
    """
    Load a molecule from a file with automatic format detection based on the file extension.
    
    Supported formats: MOL2, PDB supported by RDKit.
    
    Parameters:
    - file_path_mol: str or Path, path to the molecule file.
    
    Returns:
    - mol: RDKit Mol object, or None if the format is unsupported or loading fails.
    """

    # Extract the file extension
    # Convert file_path to a Path object if it's not already one

    file_path = Path(file_path_mol)
    file_extension = file_path.suffix.lower()

    file_path_res = file_path.resolve()
    print("Input: ", file_path_res)

    if file_extension == '.mol2':
        return Chem.MolFromMol2File(file_path_mol, removeHs=False)
    elif file_extension == '.pdb':
        return Chem.MolFromPDBFile(file_path_mol, removeHs=False)
    else:
        raise ValueError("Unsupported file type")


def writeoutput(outputpath, hydro_list, final_output):

    with open(Path(outputpath), 'w') as f:

        for hydro, df in zip(hydro_list, final_output):

                    f.write(hydro)
                    f.write('\n')
                    df.to_csv(f, sep='\t', index=False, header=None)  # Write DataFrame to file with tab separator
                    f.write('\n')
                    f.write('\n')



def mol2df(mol) -> pd.DataFrame:
    num_atoms = mol.GetNumAtoms()

    # Initialize lists to store atom data
    atom_index = []
    element_symbol = []
    x_coords = []
    y_coords = []
    z_coords = []

    # Loop over each atom in the molecule
    for i in range(num_atoms):
        atom = mol.GetAtomWithIdx(i)
        pos = mol.GetConformer().GetAtomPosition(i)
        atom_index.append(i)
        element_symbol.append(atom.GetSymbol())
        x_coords.append(pos.x)
        y_coords.append(pos.y)
        z_coords.append(pos.z)

    atom_df = pd.DataFrame({
        'Atom Index': atom_index,
        'Element Symbol': element_symbol,
        'X': x_coords,
        'Y': y_coords,
        'Z': z_coords
    })


    return atom_df



def euclidean_distance(coord1, coord2):

    return distance.euclidean(coord1, coord2)



def euclid2spherical(coord1, coord2=None):

    if coord2 is None:

        x, y, z = coord1


        r = np.linalg.norm([x, y, z])

        # Calculate azimuthal/horizontal angle
        theta = np.arctan2(y, x)

        # Calculate inclination/vertical angle
        phi = np.arctan2(np.sqrt(x**2 + y**2), z)

        spherical_coord = np.array([r, np.degrees(theta), np.degrees(phi)])

        return spherical_coord
    
    
    else:

        # Calculate spherical vector from coord2 to coord1
        x1, y1, z1 = coord1
        x2, y2, z2 = coord2


        diff_vec = np.array([x1 - x2, y1 - y2, z1 - z2])


        return euclid2spherical(diff_vec)


def normalize_angle(angle):

    if angle <= -180:
        angle += 360
    if angle > 180:
        angle -= 360
    return angle


def normalize_angles(theta_ls :pd.Series, phi_ls: pd.Series, basis_theta, basis_phi):

    theta_norm = theta_ls - basis_theta
    phi_norm = phi_ls - basis_phi

    theta_norm = theta_norm.apply(normalize_angle)
    phi_norm = phi_norm.apply(normalize_angle)

    return theta_norm, phi_norm


