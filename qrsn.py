import pcbnew
import pyqrcode

def pcbtext(board,x,y,text,size=pcbnew.VECTOR2I(1000000,2000000),layer=None,hjustify=pcbnew.GR_TEXT_H_ALIGN_CENTER):
    c=pcbnew.PCB_TEXT(board)
    c.SetPos(pcbnew.VECTOR2I(int(round(x,10)),int(round(y,10))))
    c.SetHorizJustify(hjustify)
    if layer is not None:
        c.SetLayer(board.GetLayerID(layer))
    c.SetText(text)
    c.SetTextSize(size)
    board.Add(c)


def qrpoint(center,step):
    xys=[]
    xys.append((center.real,center.imag))
    xys.append((center.real,center.imag+step))
    xys.append((center.real+step,center.imag+step))
    xys.append((center.real+step,center.imag))
    xys.append((center.real,center.imag))
    return xys


def pcbfilledrect(board,xys,layer='F.Silkscreen'):
    c=pcbnew.PCB_SHAPE(board)
    c.SetShape(pcbnew.SHAPE_T_POLY)
    polyset=pcbnew.SHAPE_POLY_SET()
    linechain=pcbnew.SHAPE_LINE_CHAIN()
    for x,y in xys:
        linechain.Append(int(round(x,10)),int(round(y,10)))
    linechain.SetClosed(True)
    polyset.AddOutline(linechain)
    c.SetPolyShape(polyset)
    c.SetFilled(True)
    c.SetWidth(0)
    c.SetLayer(board.GetLayerID(layer))
    board.Add(c)
    return c


def qrgen(stringin,quiet_zone=0):
    t=pyqrcode.create(stringin)
    text=[i for i in t.text(quiet_zone).split('\n') if i]
    return text
def qrpcb(board,stringin,x0,y0,quiet_zone=0,stepnm=10*25400,layer='F.Silkscreen'):
    text=qrgen(stringin,quiet_zone)
    cs=[]
    for il,l in enumerate(text):
        for iw,w in enumerate(l):
            center=x0+1j*y0+(iw-1j*il)*stepnm
            xys=qrpoint(center,stepnm)
            if w=='1':
                p=pcbfilledrect(board,xys,layer=layer)
                cs.append(p)
#                print(iw,il,xys)
    v=pcbnew.PCB_GROUP(board)
    for i in cs:
        v.AddItem(i)
    board.Add(v)


if __name__=="__main__":
    import argparse
    import outline
    import git
    import sys
    import os
    sys.path.append('./scripts/')
    import gerber
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(dest='project', help='project name (used in saved gerber file name)')
    parser.add_argument('-start', dest='start',type=int, default=1,help='serial number start')
    parser.add_argument('-stop', dest='stop',type=int, default=0,help='serial number stop')
    clargs = parser.parse_args()
    
    projname='_qrsn'
    boardfilename='%s.kicad_pcb'%projname
    for sn in range(clargs.start,clargs.stop):
        outline.outline(boardfilename)
        gitcommit8=git.Repo('.').head.commit.hexsha[0:8]
        board=pcbnew.LoadBoard(boardfilename)
#        qrpcb(board=board,stringin='https://gitlab.com/lbl-boards/zest commit:%s SN:%03d'%(gitcommit8,sn),x0=80000000,y0=-158000000,stepnm=15*25400,layer='B.Silkscreen')
        qrpcb(board=board,stringin='commit:%s SN:%03d'%(gitcommit8,sn),x0=89500000,y0=-203000000,stepnm=15*25400,layer='F.Silkscreen')
        pcbtext(board=board,x=101000000,y=-211000000,text="Commit:\n%s\nSN:"%(gitcommit8),size=pcbnew.VECTOR2I(1500000,1500000),layer='F.Silkscreen',hjustify=pcbnew.GR_TEXT_H_ALIGN_LEFT)
        pcbtext(board=board,x=101000000,y=-204000000,text="%03d"%(sn),size=pcbnew.VECTOR2I(5000000,5000000),layer='F.Silkscreen',hjustify=pcbnew.GR_TEXT_H_ALIGN_LEFT)
        pcbnew.Refresh()
        board.Save(boardfilename)
        outputdir='qrsngbr'
        gerber.fab(pcbfile=boardfilename,outputdir=outputdir,gerber=True,drill=False,bom=False,xypos=False,keepdateveretc=False,debug=False,layers=['F.Silkscreen'])
        gerbername='%s/%s-%s.gbr'%(outputdir,projname,'F_Silkscreen')
        gerbersnname='%s/%s%s-%s_%03d.gbr'%(outputdir,clargs.project,projname,'F_Silkscreen',sn)
        os.rename(gerbername,gerbersnname)
        for ext in ['pcb','pro']:
            os.remove('%s.kicad_%s'%(projname,ext))
    

