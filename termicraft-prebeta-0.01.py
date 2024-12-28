#23rd character???
#wait no hold on
#21st character
#20 in 0 based index
import os
import time
class text:
    def __init__(self,xpos,ypos,color,text):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.text = text
class block:
    def __init__(self,col1,col2,col3,col4,chr1,chr2,chr3,chr4,bname):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.col4 = col4
        self.chr1 = chr1
        self.chr2 = chr2
        self.chr3 = chr3
        self.chr4 = chr4
        self.bname = bname
blox=[]
blocks=[block(32,32,33,33,"V","V","*","*","Grass")]
def addblock(x,y,block):
    blox.append(text(x,y,block.col1,block.chr1))
    blox.append(text(x+1,y,block.col2,block.chr2))
    blox.append(text(x,y+1,block.col3,block.chr3))
    blox.append(text(x+1,y+1,block.col4,block.chr4))
addblock(1,2,blocks[0])
screen=[]
skrien=""
camx=0
camy=0
if True:
    screen=[]
    for suffer in range(0,29*21):
        screen.append("\033[94m\033[07m ")
    os.system('cls' if os.name == 'nt' else 'clear')
    for bloq in range(0,len(blox)):
        if camx-1<blox[bloq].xpos and camy-1<blox[bloq].ypos:
            screen[(blox[bloq].xpos-camx)+(((blox[bloq].ypos-camy))*28)]="\033["+str(blox[bloq].color)+"m\033[07m"+str(blox[bloq].text)
            #print(blox[bloq].xpos-camx,blox[bloq].ypos-camy)
    skrien=""
    for run2 in range(0,21):
        for run in range(0,28):
            skrien=skrien+screen[run+((run2)*28)]
            print(run+((run2)*28))
        skrien=skrien+"\n"
    print(skrien)
    time.sleep(0.2)
#print("\033["+str(blox[0].color)+"m\033[07m"+str(blox[0].text)+"")
#print(skrien.count('\n'))