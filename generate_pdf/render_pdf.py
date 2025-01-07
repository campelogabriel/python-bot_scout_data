from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black,white,gray,yellow


def round_image_with_border(image_path, output_path, radius=None, border_width=10):
    # Abrir a imagem
    img = Image.open(image_path).convert("RGBA")
    
    # Definir o tamanho da imagem
    width, height = img.size
    if radius is None:
        radius = min(width, height) // 2

    # Criar uma máscara maior para antialiasing e borda
    mask_size = (width * 3, height * 3)
    mask = Image.new('L', mask_size, 0)
    draw = ImageDraw.Draw(mask)
    
    # Desenhar o círculo para a máscara
    draw.ellipse((border_width, border_width, mask_size[0] - border_width, mask_size[1] - border_width), fill=255)
    
    # Desenhar o contorno preto (aumenta o tamanho da máscara para incluir a borda)
    border_draw = ImageDraw.Draw(mask)
    border_draw.ellipse((0, 0) + mask_size, outline=255, width=border_width * 8)
    
    # Redimensionar a máscara para o tamanho original
    mask = mask.resize((width, height), Image.LANCZOS)

    # Criar imagem para borda preta
    bordered_img = Image.new("RGBA", (width, height), "black")

    # Aplicar a máscara à imagem original e à borda preta
    rounded_img = Image.new("RGBA", (width, height))
    rounded_img.paste(bordered_img, (0, 0), mask=mask)
    rounded_img.paste(img, (0, 0), mask=mask)
    
    # Salvar a imagem resultante
    rounded_img.save(output_path, format="PNG")

def centralizar_texto_area(canvas, texto, x_inicio, largura_area, y, fonte="Helvetica", tamanho_fonte=12):
    # Definir a fonte e o tamanho
    canvas.setFont(fonte, tamanho_fonte)

    # Obter a largura do texto
    largura_texto = canvas.stringWidth(texto, fonte, tamanho_fonte)

    # Calcular a posição X para centralizar o texto dentro da largura da área
    x_centralizado = x_inicio + (largura_area - largura_texto) / 2

    # Desenhar o texto na posição centralizada
    return canvas.drawString(x_centralizado, y, texto)

x,y = A4
pdf = canvas.Canvas("scout.pdf")
pdf.setFillColor(black)
pdf.rect(x=0,y= 0,height=y,width= x/4,stroke=0, fill=1)

pdf.drawImage(image="imagem_arredondada.png",width=70,height=70,x=40,y=y - 100)


pdf.setFillColor(yellow)
pdf.setFontSize(12)
centralizar_texto_area(pdf,"Paulinho Paula",fonte="Helvetica-Bold",x_inicio=45,largura_area=60, y= y-130)

pdf.setFont("Helvetica",10)
pdf.setFillColor(white)
pdf.drawString(x=38,y= y - 150,text="Meio Campo")


pdf.setFontSize(9)

pdf.setFillColor(gray)
pdf.drawString(x=10,y= y - 190,text="Data Nasc")
pdf.setFillColor(white)
pdf.setFont("Helvetica",9)
pdf.drawString(x=9,y= y - 205,text="08/01/1997")

pdf.setFillColor(gray)
pdf.drawString(x=80,y= y - 190,text="Pé Dominante")
pdf.setFillColor(white)
centralizar_texto_area(pdf,"Esquerdo",60,95,y - 205,tamanho_fonte=9,fonte="Helvetica")


pdf.setFillColor(gray)
pdf.drawString(x=17,y= y - 230,text="Altura")
pdf.setFillColor(white)
pdf.drawString(x=14,y= y - 245,text="178 cm")

pdf.setFillColor(gray)
pdf.drawString(x=80,y= y - 230,text="Nacionalidade")
pdf.setFillColor(white)
pdf.drawString(x=98,y= y - 245,text="BRA")


centralizar_texto_area(pdf,"Última Partida",36,67,y - 280,tamanho_fonte=10,fonte="Helvetica-Bold")







pdf.save()