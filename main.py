import drawSvg as draw

def work_piece_num():
    '''
    здесь создаеться заготовка гос номера с регионом на 3 знака
    :return: обьект draw
    '''
    base_colour = '#ffffff'
    plate_w = 520  # width
    plate_h = 112  # height
    th = 4  # thickness

    d = draw.Drawing(plate_w, plate_h, displayInline=False, )  # создание полотна под номер
    r = draw.Rectangle(0, 0, plate_w, plate_h, fill='#000000', rx=8, ry=8, )  # заполнение черным цветом
    d.append(r)
    r = draw.Rectangle(th, th, 360, plate_h - th * 2, fill=base_colour, rx=8, ry=8)  # вставка белая под основной номер
    d.append(r)

    r = draw.Rectangle(366, th, 150, plate_h - th * 2, fill=base_colour, rx=8, ry=8)  # вставка белая под регион
    d.append(r)

    # Draw circle
    d.append(draw.Circle(20, 56, 4,
                         fill='gray', stroke_width=1, stroke='black'))

    d.append(draw.Circle(500, 56, 4,
                         fill='gray', stroke_width=1, stroke='black'))

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
    return d


def genGosNum(text):
    '''
    здесь наносим буквы и цифры на заготовку гос номера
    :param text: str госномер пример p031be150
    :return: None
    '''
    setgud = set('abekmhopctyxd1234567890')
    assert len(set(text).difference(setgud)) == 0, 'Используйте разрешенные символы из англ раскладки "abekmhopctyxd1234567890"'
    name_file = text.upper()
    text = list(name_file)
    d = work_piece_num()
    pos_text = [30, 88, 142, 196, 255, 310, 372, 411, 452]
    dict_num = dict(zip(pos_text, text))
    # # Draw text
    font_style = 'font-family:RoadNumbers'
    for key, val in dict_num.items():
        if val.isdigit():
            if key in list(dict_num.keys())[6:]:
                d.append(draw.Text(val, 94, key, 36, fill='black', style=font_style))
                continue
            d.append(draw.Text(val, 119, key, 16, fill='black', style=font_style))  # Text
        else:
            d.append(draw.Text(val, 119, key, 16, fill='black', style=font_style))  # Text
    d.savePng(f'numgos/{name_file}.png')

if __name__ == "__main__":

    genGosNum(f'p031be150')

