COMMITNUM = $(shell git log --pretty=oneline --abbrev-commit --abbrev=8|head -1 | awk '{print $$1}')
DATETIME = $(shell date  +'%Y%m%d%H%M%S')
GITTIME=$(shell git log -1 --date=iso-strict --pretty=%cd)
PROJECT=zest

pdf:
	kicad-cli sch export pdf $(PROJECT).kicad_sch

fab: gerber.py
	mkdir -p fab
	python scripts/gerber.py zest.kicad_pcb fab -gerber -drill -bom -xypos
gerber.py:
	mkdir -p scripts
	wget https://gitlab.com/lbl-bids/kicad_library/-/raw/master/scripts/gerber.py -O scripts/gerber.py

tarball: fab qrsn
	echo $(GITTIME)
	tar --sort=name --mtime=$(GITTIME)  --owner=0 --group=0 --numeric-owner -czf $(PROJECT)_$(DATETIME)_$(COMMITNUM).tar.gz fab qrsngbr
	md5sum $(PROJECT)_$(DATETIME)_$(COMMITNUM).tar.gz
zip: fab qrsn
	touch -d $(GITTIME) fab/* qrsngbr/*
	zip -X -o $(PROJECT)_$(DATETIME)_$(COMMITNUM).zip fab/* qrsngbr/*
	md5sum $(PROJECT)_$(DATETIME)_$(COMMITNUM).zip
SNSTART=1
SNSTOP=2
qrsn: gerber.py
	python qrsn.py -proj $(PROJECT)_qrsn -start $(SNSTART) -stop $(SNSTOP) -outputdir qrsngbr

.PHONY: gerber.py fab
