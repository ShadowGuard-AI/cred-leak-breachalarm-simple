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

im=Image.new("RGB",(1600,900),(190,220,226)); d=ImageDraw.Draw(im)
for y in range(560):
    t=y/560; c=tuple(int(a+(b-a)*t) for a,b in zip((214,232,236),(168,216,222)))
    d.line([(0,y),(1600,y)],fill=c)
d.rectangle([0,560,1600,900],fill=(24,52,92))
for x in (180,560,1050,1420): d.ellipse([x,600,x+54,654],fill=(232,110,150),outline=(170,60,100),width=3)
d.rectangle([0,120,1600,300],fill=(120,104,84)); d.rectangle([0,120,1600,148],fill=(84,72,56))
for i in range(9): shell(300+i*55,420+((i%3)*36),26)
d.rectangle([620,180,980,290],fill=(188,180,164),outline=(110,100,84),width=4)
d.ellipse([700,205,790,262],fill=(240,200,120),outline=(150,120,60),width=4); d.ellipse([820,205,910,262],fill=(240,200,120),outline=(150,120,60),width=4)
im.save("intro-banner.png"); print("intro drawn: rail, gloves, falling fan, buoys, no readable lettering")
