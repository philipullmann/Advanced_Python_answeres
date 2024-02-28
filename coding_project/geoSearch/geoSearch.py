import argparse
import numpy as np

from .common import utils
from .common import geometry



def parsArgumments() -> argparse.Namespace:
    # Parse Arguments from shell

    EPILOG = "---"

    ndArgs = argparse.ArgumentParser(prog="geoSearch", epilog=EPILOG)


    ndArgs.add_argument("-prot", help="PDB or Mol2 file with protein", type=str, required=True)
    ndArgs.add_argument("-lig", help="PDB or Mol2 file with ligand", type=str, required=True)
    ndArgs.add_argument("-geometry", help="Specify geometry [cube, sphere, cone]", type=str, required=True)
    ndArgs.add_argument("-o", help="Output file", type=str, required=True)

    ndArgs.add_argument("-length", help="Radius of sphere or length of cube/cone", type=float, required=True) 
    ndArgs.add_argument("-angle", help="Angle of cone. Not needed for other geometries", type=float, required=False) 



    args = ndArgs.parse_args()

    return args




def main():

     args = parsArgumments()
     args_dic = vars(args)
 

     # Read Molecules

     print(args_dic["prot"])
     prot = utils.load_molecule(args_dic["prot"])
     lig = utils.load_molecule(args_dic["lig"])

     prot_df = utils.mol2df(prot)
     lig_df = utils.mol2df(lig)

     # Search coordinates
     prot_co_df = prot_df.loc[:, ["X","Y","Z"]]

     # Filter atom type for hydrogens
     lig_h_df = lig_df[lig_df.loc[:,"Element Symbol"].str.contains("H")].reset_index(drop=True)

     # Get DF  of Connected atoms
     connected_atoms = {i: [neighbor.GetIdx() for neighbor in atom.GetNeighbors()] 
                    for i, atom in enumerate(lig.GetAtoms()) if atom.GetSymbol() == 'H'}




     # Select geometry

     hydro_pos = []
     final_out = []
     

     if args_dic["geometry"] == "cube":

          for index, atom in lig_h_df.iterrows():

               # Iterate cube
               coord_ls = np.array([atom.X, atom.Y, atom.Z])
               geoObj = geometry.cube(coord_ls, length=args_dic["length"])
               atom_list = geoObj.compute_cube(prot_co_df)
               selected_df = prot_df[prot_df.index.isin(atom_list.index)]     

               hydro_pos.append(f"Hydrogen at: {atom.X}, {atom.Y}, {atom.Z}")
               final_out.append(selected_df)




     elif args_dic["geometry"] == "sphere":

          for index, atom in lig_h_df.iterrows():

               coord_ls = np.array([atom.X, atom.Y, atom.Z])
               geoObj = geometry.sphere(coord_ls, radius=args_dic["length"])
               atom_list = geoObj.compute_sphere(prot_co_df)
               selected_df = prot_df[prot_df.index.isin(atom_list.index)]

               hydro_pos.append(f"Hydrogen at: {atom.X}, {atom.Y}, {atom.Z}")
               final_out.append(selected_df)   

     elif args_dic["geometry"] == "cone":

          if args_dic["angle"] == None:
               print("ERROR: No angle selected!")
               raise ValueError

          for index, atom in lig_h_df.iterrows():

               base_atom_int = (connected_atoms[atom["Atom Index"]][0])
               bs_coord_ls = np.array(lig_df.loc[:,["X","Y","Z"]][lig_df["Atom Index"] == base_atom_int])[0]

               coord_ls = np.array([atom.X, atom.Y, atom.Z])
               geoObj = geometry.cone(coord_ls, bs_coord_ls, angle=args_dic["angle"], length=args_dic["length"])
               atom_list = geoObj.compute_cone(prot_co_df)
               selected_df = prot_df[prot_df.index.isin(atom_list.index)]

               hydro_pos.append(f"Hydrogen at: {atom.X}, {atom.Y}, {atom.Z}")
               final_out.append(selected_df)

     else:
          raise ValueError
     


     # Print Output file


     utils.writeoutput(args_dic["o"], hydro_pos, final_out)















if __name__ == "__main__":
     main()


