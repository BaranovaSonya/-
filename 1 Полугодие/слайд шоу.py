from Time import sleep
from PIL import Image, ImageDraw, ImageFont

spisok = ['НА СТАРТ', 'ВНИМАНИЕ', 'ОБЕД!!!']

for i in range(len(spisok)):
    im = Image.new('RGB',(200,200), color=('#336699'))
    font = ImageFont.truetype('C:/Windows/Fonts/Book Antiqua/BKANT.TTF', size=22)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100,100),
        spisok[i],
        font = font,
        fill = ('#1C0606')
        )
    time.sleep() 
im.show()

