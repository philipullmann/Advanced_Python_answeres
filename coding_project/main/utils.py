def load_molecule(file_path_mol: str):
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

    if file_extension == '.mol2':
        return Chem.MolFromMol2File(file_path_mol, removeHs=False)
    elif file_extension == '.pdb':
        return Chem.MolFromPDBFile(file_path_mol, removeHs=False)
    else:
        raise ValueError("Unsupported file type")

