# Zest board in KiCAD 8.0
The board is designed in KiCAD 8.0. 
The original Zest board can be found at https://github.com/BerkeleyLab/Zest , which use gEDA and PADS for the schematic and layout design. 
The history and credit of the board can be found in the [boardhistoryandcredit](./boardhistoryandcredit)

The v1.2 is purposefully use the exact same traces/via/zone as v1.1,
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

It will download a script I had in the BIDS repo and use it to generate the gerber, drill, bom and xyposition files. I didn't include the whole BIDS as submodule because I don't feel it's necessary, as I am only using this single file here. 

### Generate QR code for SN 

`make qrsn SNSTART=10 SNSTOP=20`

This will generate the gerber file for the 10 different SN. The generated gerbers can be found in the directory 

`ls qrsngbr`

### Generate zip file
`make zip SNSTART=10 SNSTOP=20`

This will generate a zip file contains the contents in the fab and the qrsngbr. 

### Generate tarball file
`make tarball SNSTART=10 SNSTOP=20`

This will generate a .tar.gz file contains the contents in the fab and the qrsngbr. 