# Zest board in KiCad 8.0
The board is designed in [KiCad](https://www.kicad.org/) 8.0.
The original Zest board can be found at [https://github.com/BerkeleyLab/Zest](https://github.com/BerkeleyLab/Zest),
which use [gEDA](https://en.wikipedia.org/wiki/GEDA) and [PADS](https://en.wikipedia.org/wiki/PADS_(CAD_software)) for the schematic and layout design.
The history and credit of the board can be found in the [boardhistoryandcredit](./boardhistoryandcredit) file.

This v1.2 is purposefully uses the exact same traces/via/zone as v1.1,
## Except

The simple R/C/L footprints use the built-in footprints from KiCad, so those pad sizes are slightly different from the original Gerber.

The other footprints are directly downloaded from different online repos, including digikey.com and snapeda.com.

I can not include the footprint files because they are not licensed
for redistribution.

## Reference ID mapping

The reference ID for each component has changed because the KiCad and gEDA manage the hierarchical sheets / subcircuit differently. 
A mapping of the v1.2 and v1.1 part reference ID can be found in the partsub.json.

## Clone the repo
```
git clone https://gitlab.com/lbl-boards/zest
cd zest
```

### Open the design:
#### From KiCAD GUI:
File->Open Project...
and navigate to the project file: zest.kicad_pro
#### From command line
`kicad zest.kicad_pro`

### Generate fabrication package
`make fab`

It will download the Gerber.py script from the [BIDS repo](https://gitlab.com/lbl-bids/kicad_library) and use it to generate the Gerber, drill, bom and xyposition files. I didn't include the whole BIDS as submodule because I don't feel it's necessary, as I am only using this single file here.

### Generate QR code for SN

`make qrsn SNSTART=10 SNSTOP=20`

This will generate the Gerber file for 10 different serial numbers. The generated Gerbers can be found in the directory

`ls qrsngbr`

### Generate zip file
`make zip SNSTART=10 SNSTOP=20`

This will generate a zip file containing files from the fab and the qrsngbr directories.

### Generate tarball file
`make tarball SNSTART=10 SNSTOP=20`

This will generate a .tar.gz file containing files from the fab and the qrsngbr directories.
