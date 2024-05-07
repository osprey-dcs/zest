fab: gerber.py
	mkdir -p fab
	python scripts/gerber.py zest.kicad_pcb fab -gerber -drill -bom -xypos
gerber.py:
	mkdir -p scripts
	wget https://gitlab.com/lbl-bids/kicad_library/-/raw/master/scripts/gerber.py -O scripts/gerber.py
.PHONY: gerber.py fab
