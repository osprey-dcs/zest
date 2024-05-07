import os
import pcbnew
def edgecutssegment(board,start,end,width,uuidincref=None):
    c=pcbnew.PCB_SHAPE(board)
    c.SetShape(pcbnew.SHAPE_T_SEGMENT)
    c.SetStart(pcbnew.VECTOR2I(start))
    c.SetEnd(pcbnew.VECTOR2I(end))
    c.SetLayer(pcbnew.Edge_Cuts)
    c.SetWidth(int(round(width,10)))
    board.Add(c)

points=(
(27138120, -46718980), 
(137137900, -46718980), 
(137137900, -186718960),
(116137940, -186718960), 
(116137940, -228479100), 
(27138120, -228479100), 
(27138120, -46718980), 
)
def outline(filename):
    if os.path.isfile(filename):
        b=pcbnew.LoadBoard(filename)
    else:
        b=pcbnew.NewBoard(filename)
    for istart,start in enumerate(points[0:-1]):
        startpoint=pcbnew.VECTOR2I(start[0],start[1])
        endpoint=pcbnew.VECTOR2I(points[istart+1][0],points[istart+1][1])
        edgecutssegment(board=b,start=startpoint,end=endpoint,width=2*25400,uuidincref=None)
    b.Save(filename)

if __name__=="__main__":
    outline('zest.kicad_pcb')
