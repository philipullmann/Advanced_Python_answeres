
## geoSearch

**Author:** &nbsp;&nbsp;Philip Ullmann<br />
**Email:**  &nbsp;&nbsp;&nbsp;philip.ullmann@icm.uu.se <br />
**Place:** &nbsp;&nbsp;&nbsp;Jens Carlsson Lab. Uppsala University <br />
**Date:** &nbsp;&nbsp;  2024 </br >
**Current Version:** &nbsp;&nbsp;  0.0.1


GeoSearch is a program to determine atoms which are close to ligand hydrogens. <br />
Currently supported are three types of geometries: <br />
- Cube
- Sphere
- Cone
- Mandelbulb



# Installation

    pip install -e coding_project


# Usage

    coneSearch -prot [path/to/prot.pdb] -lig [path/to/lig.pdb] -geometry [geometry] -length [length] -o [output]

Special:

-angle (only needed for cone)
-power (only needed for mandelbulb)
-resolution (only needed for mandelbulb)


</br>
</br>
</br>

<tr>
<figure>
    <td> <img src="picture/sketch_draw.png" alt="Drawing"  width="1033" align="center" height="787"> </td>
    <figcaption><b>Figure 1</b>. Sketch of problem </figcaption>
</figure>
</tr> 
