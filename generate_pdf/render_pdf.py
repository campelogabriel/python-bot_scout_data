from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black,white,gray,yellow,gold,gainsboro,whitesmoke,salmon


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
    canvas.setFont(fonte, tamanho_fonte)

    largura_texto = canvas.stringWidth(texto, fonte, tamanho_fonte)

    x_centralizado = x_inicio + (largura_area - largura_texto) / 2

    return canvas.drawString(x_centralizado, y, texto)




x,y = A4
pdf = canvas.Canvas("scout.pdf")
pdf.setFillColor(black)
pdf.rect(x=0,y= 0,height=y,width= x/4,stroke=0, fill=1)
pdf.setFillColor(whitesmoke)
pdf.rect(x=x/4,y=0,width= x - x/4 ,height=y,stroke=0,fill=1)
pdf.drawImage("team.png",120,y - 74,60,60, mask="auto")




pdf.drawImage(image="imagem_arredondada.png",width=70,height=70,x=40,y=y - 100,mask="auto")


pdf.setFillColor(gold)
centralizar_texto_area(pdf,"Paulinho Paula",fonte="Helvetica-Bold",x_inicio=45,largura_area=60, y= y-130)

pdf.setFillColor(white)
centralizar_texto_area(pdf,"Meio-Campo",fonte="Helvetica",x_inicio=45,largura_area=60, y= y - 150,tamanho_fonte=10)



pdf.setFont("Helvetica",9)
pdf.setFillColor(gray)
pdf.drawString(x=10,y= y - 190,text="Data Nasc")
pdf.setFillColor(white)
pdf.setFont("Helvetica",9)
pdf.drawString(x=9,y= y - 205,text="08/01/1997")

pdf.setFillColor(gray)
pdf.drawString(x=80,y= y - 190,text="Pé Dominante")
pdf.setFillColor(white)
centralizar_texto_area(pdf,"Direito",60,95,y - 205,tamanho_fonte=9,fonte="Helvetica")


pdf.setFillColor(gray)
pdf.drawString(x=17,y= y - 230,text="Altura")
pdf.setFillColor(white)
pdf.drawString(x=14,y= y - 245,text="178 cm")

pdf.setFillColor(gray)
pdf.drawString(x=80,y= y - 230,text="Nacionalidade")
pdf.setFillColor(white)
pdf.drawString(x=98,y= y - 245,text="BRA")

pdf.setStrokeColor(white)
pdf.line(0,y - 260,x/4,y - 260)

centralizar_texto_area(pdf,"Última Partida",40,67,y - 280,tamanho_fonte=10,fonte="Helvetica-Bold")
centralizar_texto_area(pdf,"08/12/2024",40,67,y - 295,tamanho_fonte=8,fonte="Helvetica")


name_mandante = "Cuiabá"
name_visitante = "Vasco"
placar_mandante = "1"
placar_visitante = "2"



pdf.drawImage("cuiaba.png",18,y - 335,20,20, mask="auto")
centralizar_texto_area(pdf,name_mandante,8,40,y - 350,tamanho_fonte=8,fonte="Helvetica")

centralizar_texto_area(pdf,placar_mandante,36,50,y - 333,tamanho_fonte=20,fonte="Helvetica-Bold")
centralizar_texto_area(pdf,"-",44,55,y - 332,tamanho_fonte=14,fonte="Helvetica-Bold")
centralizar_texto_area(pdf,placar_visitante,54,60,y - 333,tamanho_fonte=20,fonte="Helvetica-Bold")


pdf.drawImage("team.png",x / 4 - 45,y - 335,20,20, mask="auto")
centralizar_texto_area(pdf,name_visitante,x_inicio=x / 4 - 50,largura_area=x / 4 - 120,y=y - 350,tamanho_fonte=8,fonte="Helvetica")

    
pdf.setStrokeColor(white)
pdf.line(0,y - 380,x/4,y - 380)
pdf.setFont("Helvetica-Bold",10)
pdf.drawString(53,y-400,"Posição")
pdf.drawImage("soccer-field.png",13,y - 540,120,120, mask="auto")

# PARTIDAS
   
pdf.setFillColor(white)
pdf.roundRect(180,y-240,160,140,5,stroke=0,fill=1)

pdf.setFillColor(black)
pdf.setFont("Courier-Bold",12)
pdf.drawString(190, y - 120,"Partidas")
pdf.setFont("Courier-Bold",24)
pdf.drawString(190, y - 150,"20")

# DADOS PARTIDAS
pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 175,"Titular:")
pdf.setFillColor(black)
pdf.drawString(228, y - 175,"2")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 188,"Mins por jogo:")
pdf.setFillColor(black)
pdf.drawString(263, y - 188,"75")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 201,"Total de minutos:")
pdf.setFillColor(black)
pdf.drawString(278, y - 201,"1230")

# Gols

pdf.setFillColor(white)
pdf.roundRect(405,y-240,155,140,5,stroke=0,fill=1)


pdf.setFillColor(black)
pdf.setFont("Courier-Bold",12)
pdf.drawString(415, y - 120,"Gols")
pdf.setFont("Courier-Bold",24)
pdf.drawString(415, y - 150,"2")

# DADOS Gols
pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 175,"xG:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(432, y - 175,"0.21")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 188,"Gols por jogo:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(473, y - 188,"0.4")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 201,"Gols Com Pé Esquerdo:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(515, y - 201,"0")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 214,"Gols Com Pé Direito:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(502, y - 214,"1")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 227,"Gols de Cabeça:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(485, y - 227,"0")

# Passe

pdf.setFillColor(white)
pdf.roundRect(180,y-410,160,140,5,stroke=0,fill=1)

pdf.setFillColor(black)
pdf.setFont("Courier-Bold",12)
pdf.drawString(190, y - 290,"Assistências")
pdf.setFont("Courier-Bold",24)
pdf.drawString(190, y - 320,"0")

# Dados Passe

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 345,"xA:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(205, y - 345,"0.02")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 358,"Grande Chances Criadas:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(298, y - 358,"8")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 371,"Acerto em Passes:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(268, y - 371,"94%")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 384,"Acerto em Lançamentos:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(293, y - 384,"87%")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 397,"Acerto em Cruzamentos:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(293, y - 397,"27%")

# defesa

pdf.setFillColor(white)
pdf.roundRect(405,y - 410,155,140,5,stroke=0,fill=1)


pdf.setFillColor(black)
pdf.setFont("Courier-Bold",12)
pdf.drawString(415, y - 290,"Desarmes")
pdf.setFont("Courier-Bold",24)
pdf.drawString(415, y - 320,"38")


# DADOS defesa

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 345,"Interceptação por jogo:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(509, y - 345,"5.4")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 358,"Bolas Recuperadas por jogo:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(534, y - 358,"3.2")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 371,"Dribles Sofridos por jogo:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(519, y - 371,"0.9")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 384,"Duelos Vencidos no Chão:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(524, y - 384,"40%")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(415, y - 397,"Duelos Aereos Vencidos:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(518, y - 397,"90%")

# Outros

pdf.setFillColor(white)
pdf.roundRect(180,y-580,160,140,5,stroke=0,fill=1)

pdf.setFillColor(black)
pdf.setFont("Courier-Bold",12)
pdf.drawString(190, y - 460,"Outros")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 485,"Dribles Completos:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(268, y - 485,"3.2 (68%)")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 498,"Perda da bola por jogo:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(288, y - 498,"4.3")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 511,"Faltas Sofridas:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(255, y - 511,"2")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 524,"Faltas Cometidas:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(265, y - 524,"5")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 537,"Impedimentos:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(251, y - 537,"5")


pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 549,"Erros que levaram ao chute:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(306, y - 549,"3")

pdf.setFillColor(gray)
pdf.setFont("Helvetica",9)
pdf.drawString(190, y - 562,"Erros que levaram ao gol:")
pdf.setFillColor(black)
pdf.setFont("Helvetica-Bold",9)
pdf.drawString(296, y - 562,"0")






pdf.save()