# Zest board in KiCAD 8.0
The board is designed in KiCAD 8.0. 
The original Zest board can be found at https://github.com/BerkeleyLab/Zest , which use gEDA and PADS for the schematic and layout design. 
The v1.2 is purposefully use the exact same traces/via/zone as v1.1.

## Except

The simple R/C/L footprint are using the built-in footprint in KiCAD, so the pads size are different from the original gerber.

The other footprints are directly downloaded from different online repos, including the digikey.com and snapeda.com. 

I can not include the footprint files because they are not mine.

## Clone the repo
```
git clone https://gitlab.com/lbl-boards/zest
cd zest
```

### Open the design: 
#### From KiCAD GUI:
File->Open Project...
and nevigate the project file: zest.kicad_pro 
#### From command line
`kicad zest.kicad_pro`

### Generate fabrication package
`make fab`

It will download a script I had in the BIDS repo and use it. I didn't include the whole BIDS as submodule because I don't feel it's necessary, as I am only using this single file here. 

### Generate QR code for SN 
Make sure the gerber.py already exist in the scripts directory, if not, run 

`make gerber.py`

and it will download from the BIDS repo.

`python qrsn.py zest -start 10 -stop 20`

This will generate the gerber file for the 10 different SN. The generated gerbers can be found in the directory 

`ls qrsngbr`

### Generate zip file
`make zip`

This will generate a zip file contains the contents in the fab and the qrsngbr. 

### Generate tarball file
`make tarball`

This will generate a .tar.gz file contains the contents in the fab and the qrsngbr. 