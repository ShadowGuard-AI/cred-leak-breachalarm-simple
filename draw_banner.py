"""Individually coded drawing program for this repository and this piece only."""
import math, random
from PIL import Image, ImageDraw, ImageFont
FD="/tmp/fonts17"
def F(n,s): return ImageFont.truetype(f"{FD}/{n}.ttf", s)
def fit(d,t,n,mw,st=60):
    s=st
    while s>10:
        f=F(n,s)
        if d.textlength(t,font=f)<=mw: return f
        s-=2
    return F(n,s)

def shell(cx,cy,s,fill=(206,198,178)):
    pts=[]
    for a in range(0,360,28):
        rr=s*(0.82+0.22*math.sin(math.radians(a*3))); pts.append((cx+math.cos(math.radians(a))*rr,cy+math.sin(math.radians(a))*rr*0.78))
    d.polygon(pts,fill=fill,outline=(24,52,92)); d.line([(cx-s*0.7,cy),(cx+s*0.7,cy)],fill=(24,52,92),width=2)

im=Image.new("RGB",(1600,520),(200,225,230)); d=ImageDraw.Draw(im)
for y in range(330):
    t=y/330; c=tuple(int(a+(b-a)*t) for a,b in zip((226,238,240),(168,216,222)))
    d.line([(0,y),(1600,y)],fill=c)
d.rectangle([0,330,1600,520],fill=(24,52,92)); d.rectangle([0,318,1600,336],fill=(74,140,90))
for i in range(5): d.rectangle([80+i*150,215,210+i*150,320],fill=(188,180,164),outline=(110,100,84),width=3)
for i in range(7): shell(900+i*46,360+((i%3)*30),22)
for x in (1240,1480): d.ellipse([x,352,x+44,398],fill=(232,110,150),outline=(170,60,100),width=3)
d.rectangle([240,60,900,140],fill=(232,224,204),outline=(24,52,92),width=4)
t="cred-leak-breachalarm-simple"; d.text((570,100),t,font=fit(d,t,"BigShouldersInlineDisplay",640,42),fill=(24,52,92),anchor="mm")
im.save("banner.png"); print("banner drawn: barge at work, cabin name board")
