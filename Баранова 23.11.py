from PIL import Image, ImageDraw, ImageFont
im = Image.new('RGB',(200,200),color=('#336699'))
im.show()
font = ImageFont.truetype('C:\Windows\Fonts\Book Antiqua', size=22)
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (100, 100),
    'Conan Gray',
    font=font,
    fill='#1C0606')
im.show()
