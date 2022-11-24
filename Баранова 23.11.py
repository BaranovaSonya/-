a=int(3)
b=int(1)
spisok=['НА СТАРТ','ВНИМАНИЕ','ОБЕД!!!']
for i in range:
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new('RGB',(200,200),color=('#336699'))
    font = ImageFont.truetype('C:/Windows/Fonts/Book Antiqua/BKANT.TTF', size=22)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100,100),
        '1',
        font=font,
        fill=('#1C0606')
        )
im.show()

