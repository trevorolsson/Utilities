# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:06:03 2022

@author: tzo0018
"""
from PIL import Image as I
path = r'<path>'

bg = I.open(path+'sfa.png'); bg = bg.convert("RGBA")
fg = I.open(path+'qo.png'); fg = fg.convert("RGBA"); fg = fg.resize((1642,1589))

res = 100
for i in range(res):
    overlay = I.blend(bg,fg,i/100)
    overlay.save(path+'ani_files//'+"{}.png".format(i))
