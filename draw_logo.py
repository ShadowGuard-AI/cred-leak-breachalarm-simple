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

im=Image.new("RGB",(900,680),(168,216,222)); d=ImageDraw.Draw(im)
d.ellipse([300,300,470,400],fill=(240,200,120),outline=(150,120,60),width=5)
shell(450,240,130,(198,188,166))
for i in range(7): d.ellipse([400+i*16,215+(i%3)*18,412+i*16,227+(i%3)*18],fill=(244,240,224),outline=(24,52,92))
d.line([(520,150),(580,90)],fill=(24,52,92),width=4); d.ellipse([574,82,592,100],outline=(24,52,92),width=3)
t="cred-leak-breachalarm-simple"; d.text((450,560),t,font=fit(d,t,"BigShouldersInlineDisplay",820,44),fill=(24,52,92),anchor="mm")
im.save("logo.png"); print("logo drawn: rough seeded shell in gloved hand, no pearl")
