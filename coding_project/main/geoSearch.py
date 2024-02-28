from pathlib import Path
import argparse


import numpy as np

import utils
import geometry





def parsArgumments() -> argparse.Namespace:
    # Parse Arguments from shell

    EPILOG = "---"

    ndArgs = argparse.ArgumentParser(prog="geoSearch", epilog=EPILOG)


    ndArgs.add_argument("-prot", help="PDB or Mol2 file with protein", type=str, required=True)
    ndArgs.add_argument("-lig", help="PDB or Mol2 file with ligand", type=str, required=True)

    ndArgs.add_argument("-geometry", help="Specify geometry [cube, sphere, cone]", type=str, required=True)

    ndArgs.add_argument("-length", help="Radius of sphere or length of cube/cone", type=float, required=True) 
    ndArgs.add_argument("-angle", help="Angle of cone. Not needed for other geometries", type=float, required=False) 



    args = ndArgs.parse_args()

    return args




def main():

     prot = utils.load_molecule("../example/protein.pdb")
     lig = utils.load_molecule("../example/ligand.pdb")

     prot_df = utils.mol2df(prot)
     lig_df = utils.mol2df(lig)

     print(len(prot_df))
     print(prot_df)

     # Search coordinates
     prot_co_df = prot_df.loc[:, ["X","Y","Z"]]

     # Filter atom type for hydrogens
     lig_h_df = lig_df[lig_df.loc[:,"Element Symbol"].str.contains("H")].reset_index(drop=True)

     # Get DF  of Connected atoms
     connected_atoms = {i: [neighbor.GetIdx() for neighbor in atom.GetNeighbors()] 
                    for i, atom in enumerate(lig.GetAtoms()) if atom.GetSymbol() == 'H'}



     for index, atom in lig_h_df.iterrows():

          # Iterate cube
          coord_ls = np.array([atom.X, atom.Y, atom.Z])
          geoObj = geometry.cube(coord_ls, length=5)
          atom_list = geoObj.compute_cube(prot_co_df)
          selected_df = prot_df[prot_df.index.isin(atom_list.index)]

          del geoObj

          # Iterate sphere

          coord_ls = np.array([atom.X, atom.Y, atom.Z])
          geoObj = geometry.sphere(coord_ls, radius=5)
          atom_list = geoObj.compute_sphere(prot_co_df)
          selected_df = prot_df[prot_df.index.isin(atom_list.index)]


          # Iterate Cone

          coord_ls = np.array([atom.X, atom.Y, atom.Z])
          base_atom_int = (connected_atoms[atom["Atom Index"]][0])

          bs_coord_ls = np.array(lig_df.loc[:,["X","Y","Z"]][lig_df["Atom Index"] == base_atom_int])[0]

          geoObj = geometry.cone(coord_ls, bs_coord_ls, angle=45, length=10)
          atom_list = geoObj.compute_cone(prot_co_df)


          selected_df = prot_df[prot_df.index.isin(atom_list.index)]









if __name__ == "__main__":
     main()


