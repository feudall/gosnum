import drawSvg as draw
import string as st
plate_text = 'K627PO190'

plate_w = 520  # width
plate_h = 112  # height
th = 4  # thickness

plate_pos, plate_reg_w = ([59, 88, 142, 196, 275, 329, 372, 2], 160)
k_offset = {'K': 36, 'P': 252, 'O': 302}

d = draw.Drawing(plate_w, plate_h, displayInline=False)  # создание полотна под номер

r = draw.Rectangle(0, 0, plate_w, plate_h, fill='#000000', rx=8, ry=8)  # заполнение черным цветом
d.append(r)

base_colour = '#ffffff'
reg_colour = '#ffffff'

r = draw.Rectangle(th, th, 360, plate_h - th * 2, fill=base_colour, rx=8, ry=8)  # вставка белая под основной номер
d.append(r)

r = draw.Rectangle(366, th, 150, plate_h - th * 2, fill=base_colour, rx=8, ry=8)  # вставка белая под регион
d.append(r)
# How many simbols
plate_len = 6

# Draw text
font_style = 'font-family:RoadNumbers'
for i, s in enumerate(plate_text[:plate_len]):
    if s.isdigit():
        d.append(draw.Text(s, 119, plate_pos[i], 16, fill='black', style=font_style))  # Text
    else:
        d.append(draw.Text(s, 119, k_offset[s], 16, fill='black', style=font_style))  # Text

# Text region
font_style = f'letter-spacing:{plate_pos[plate_len + 1]}px;font-family:RoadNumbers'
d.append(draw.Text(plate_text[plate_len:], 94, plate_pos[plate_len], 36, fill='black', style=font_style))

# Draw flag
flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
r = draw.Rectangle(465, 12, 38, 21, fill='#ffffff', style=flag_style)
d.append(r)

flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
r = draw.Rectangle(465, 19, 38, 7, fill='#00f')
d.append(r)

flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
r = draw.Rectangle(465, 12, 38, 7, fill='#f00')
d.append(r)

# draw RUS
font_style = 'font-style:normal;letter-spacing:2px;font-stretch:normal;font-family:Arial'
d.append(draw.Text('RUS', 28, 400, 12, fill='black', style=font_style))

# Draw circle
d.append(draw.Circle(20, 56, 4,
                     fill='gray', stroke_width=1, stroke='black'))

d.append(draw.Circle(500, 56, 4,
                     fill='gray', stroke_width=1, stroke='black'))

d.savePng('example1.png')