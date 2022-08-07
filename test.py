import drawSvg as draw

def work_piece_num(skewX=0, skewY=0, rotate=0, scale=1,regcount=True):

    angle = f'skewX({skewX}) skewY({skewY}) rotate({rotate} 0 0) scale({scale})'
    base_colour = '#ffffff'
    plate_w = 520  # width
    plate_h = 112  # height
    th = 8  # thickness

    d = draw.Drawing(800, 800, displayInline=False)  # создание полотна под номер
    r = draw.Rectangle(0, 0, 800, 800, fill='	#282828', rx=8, ry=8,
                       # transform=angle
                       )  # заполнение черным цветом
    d.append(r)
    r = draw.Rectangle(140, 344, plate_w, plate_h, fill='#000000', rx=8, ry=8, transform=angle)  # заполнение черным цветом
    d.append(r)
    if regcount:
        r = draw.Rectangle(148,
                          352,
                          384,
                          96,
                          fill=base_colour,
                          rx=8,
                          ry=8,
                          transform=angle)  # вставка белая под основной номер
        d.append(r)

        r = draw.Rectangle(534,
                          352,
                          119,
                          96,
                          fill=base_colour,
                          rx=8,
                          ry=8,
                          transform=angle)  # вставка белая под регион
        d.append(r)
    else:
        r = draw.Rectangle(148,
                           352,
                           356,
                           96,
                           fill=base_colour,
                           rx=8, ry=8,
                           transform=angle)  # вставка белая под основной номер
        d.append(r)

        r = draw.Rectangle(507,
                           352,
                           145,
                           96,
                           fill=base_colour,
                           rx=8,
                           ry=8,
                           transform=angle)  # вставка белая под регион
        d.append(r)
        # Draw circle
    d.append(draw.Circle(160, 400, 4,
                         fill='gray',
                         stroke_width=1,
                         stroke='black',
                         transform=angle))

    d.append(draw.Circle(640,
                         400,
                         4,
                         fill='gray',
                         stroke_width=1,
                         stroke='black',
                         transform=angle))

    # Draw flag
    flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
    r = draw.Rectangle(608,
                       358,
                       38,
                       21,
                       fill='#ffffff',
                       style=flag_style,
                       transform=angle)
    d.append(r)

    flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
    r = draw.Rectangle(608,
                       365,
                       38,
                       7,
                       fill='#00f',
                       transform=angle)
    d.append(r)

    flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
    r = draw.Rectangle(608,
                       358,
                       38,
                       7,
                       fill='#f00',
                       transform=angle)
    d.append(r)

    # draw RUS
    font_style = 'font-style:normal;letter-spacing:2px;font-stretch:normal;font-family:Arial'
    d.append(draw.Text('RUS',
                       28,
                       542,
                       358,
                       fill='black',
                       style=font_style,
                       transform=angle))
    return d

def genGosNum(text='p031be150', skewX=0, skewY=0, rotate=0, scale=0, blackout=0,regcount=True):

    plate_w = 520  # width  1120
    plate_h = 112  # height
    th = 4  # thickness
    angle = f'skewX({skewX}) skewY({skewY}) rotate({rotate} 0 0) scale({scale})'
    setgud = set('abekmhopctyxd1234567890')
    assert len(set(text).difference(
        setgud)) == 0, 'Используйте разрешенные символы из англ раскладки "abekmhopctyxd1234567890"'
    name_file = text.upper()
    text = list(name_file)
    d = work_piece_num(skewX=skewX,
                       skewY=skewY,
                       rotate=rotate,
                       scale=scale,
                       regcount=regcount)
    pos_text = [170, 228, 280, 332, 388, 444, 512, 553, 594]
    dict_num = dict(zip(pos_text, text))
    pos_text1 = [174, 236, 292, 348, 408, 464, 547, 591]
    dict_num1 = dict(zip(pos_text1, text))
    # # Draw text
    font_style = 'font-family:RoadNumbers'
    if regcount:
        for key, val in dict_num1.items():
            if val.isdigit():
                if key in list(dict_num1.keys())[6:]:
                    d.append(draw.Text(val,
                                       90,
                                       key,
                                       384,
                                       fill='black',
                                       style=font_style,
                                       transform=angle))  #  цифры регион
                    continue
                d.append(draw.Text(val,
                                   119,
                                   key,
                                   361,
                                   fill='black',
                                   style=font_style,
                                   transform=angle))  # Text
            else:
                d.append(draw.Text(val,
                                   119,
                                   key,
                                   361,
                                   fill='black',
                                   style=font_style,
                                   transform=angle))  # Text
        r = draw.Rectangle(140,
                           344,
                           plate_w,
                           plate_h,
                           fill='#000000',
                           rx=8,
                           ry=8,
                           transform=angle,
                           stroke='black',
                           fill_opacity=blackout)  # заполнение черным цветом
        d.append(r)

    else:
        for key, val in dict_num.items():
            if val.isdigit():
                if key in list(dict_num.keys())[6:]:
                    d.append(draw.Text(val,
                                       90,
                                       key,
                                       384,
                                       fill='black',
                                       style=font_style,
                                       transform=angle))
                    continue
                d.append(draw.Text(val,
                                   119,
                                   key,
                                   361,
                                   fill='black',
                                   style=font_style,
                                   transform=angle))  # Text
            else:
                d.append(draw.Text(val,
                                   119,
                                   key,
                                   361,
                                   fill='black',
                                   style=font_style,
                                   transform=angle))  # Text
        r = draw.Rectangle(140,
                           344,
                           plate_w,
                           plate_h,
                           fill='#000000',
                           rx=8,
                           ry=8,
                           transform=angle,
                           stroke='black',
                           fill_opacity=blackout)  # заполнение черным цветом
        d.append(r)
    d.savePng('example.png')
    return d

genGosNum(f'h031be150', skewX=0, skewY=0, rotate=0, scale=0.5, blackout=0.5, regcount=False)