import drawSvg as draw

def work_piece_num(angle='Y', val=0):


    '''
    здесь создаеться заготовка гос номера с регионом на 3 знака
    :return: обьект draw
    '''


    angle = f'skew{angle}({val})'
    base_colour = '#ffffff'
    plate_w = 520  # width
    plate_h = 112  # height
    th = 4  # thickness

    d = draw.Drawing(700, 700, displayInline=False, origin='center')  # создание полотна под номер
    r = draw.Rectangle(-260, -56, plate_w, plate_h, fill='#000000', rx=8, ry=8, transform=angle)  # заполнение черным цветом
    d.append(r)
    r = draw.Rectangle(-260 + th, -56 + th, 360, plate_h - th * 2, fill=base_colour, rx=8, ry=8, transform=angle)  # вставка белая под основной номер
    d.append(r)

    r = draw.Rectangle(107, -56 + th, 150, plate_h - th * 2, fill=base_colour, rx=8, ry=8, transform=angle)  # вставка белая под регион
    d.append(r)

    # Draw circle
    d.append(draw.Circle(-240, 0, 4,
                         fill='gray', stroke_width=1, stroke='black', transform=angle))

    d.append(draw.Circle(240, 0, 4,
                         fill='gray', stroke_width=1, stroke='black', transform=angle))

    # Draw flag
    flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
    r = draw.Rectangle(205, -44, 38, 21, fill='#ffffff', style=flag_style, transform=angle)
    d.append(r)

    flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
    r = draw.Rectangle(205, -37, 38, 7, fill='#00f', transform=angle)
    d.append(r)

    flag_style = "stroke-width:0.4;stroke:rgb(0,0,0)"
    r = draw.Rectangle(205, -44, 38, 7, fill='#f00', transform=angle)
    d.append(r)

    # draw RUS
    font_style = 'font-style:normal;letter-spacing:2px;font-stretch:normal;font-family:Arial'
    d.append(draw.Text('RUS', 28, 140, -44, fill='black', style=font_style, transform=angle))
    return d

def genGosNum(text, angl='Y', val=0):
    '''
    отрисовка гос номера под разними углами
    :param text: str гос номер также используеться в названии сохраняемого файла.
    :param angl: str Y или X
    :param val: int угл до 50%
    :return: None сохраняет в файл
    '''

    angle = f'skew{angl}({val})'
    setgud = set('abekmhopctyxd1234567890')
    assert len(set(text).difference(
        setgud)) == 0, 'Используйте разрешенные символы из англ раскладки "abekmhopctyxd1234567890"'
    name_file = text.upper()
    text = list(name_file)
    d = work_piece_num(angle=angl, val=val)
    pos_text = [-230, -172, -118, -64, 5, 50, 115, 151, 192]
    dict_num = dict(zip(pos_text, text))
    # # Draw text
    font_style = 'font-family:RoadNumbers'
    for key, val in dict_num.items():
        if val.isdigit():
            if key in list(dict_num.keys())[6:]:
                d.append(draw.Text(val, 94, key, -20, fill='black', style=font_style, transform=angle))
                continue
            d.append(draw.Text(val, 119, key, -40, fill='black', style=font_style, transform=angle))  # Text
        else:
            d.append(draw.Text(val, 119, key, -40, fill='black', style=font_style, transform=angle))  # Text
    d.savePng(f'numgos/{name_file}.png')

genGosNum(f'p031be150', angl='Y', val=50)
