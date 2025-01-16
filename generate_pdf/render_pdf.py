from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black,white,gray,gold,whitesmoke,lightgray
from datetime import datetime
from .get_positions import get_positions
from .position_player import position_convert
import requests
from io import BytesIO



def round_image_with_border(image_path, output_path, radius=None, border_width=10):

    response = requests.get(image_path)
    img = Image.open(BytesIO(response.content))
    # img = Image.open(image_path).convert("RGBA")
    
    width, height = img.size
    if radius is None:
        radius = min(width, height) // 2

    mask_size = (width * 3, height * 3)
    mask = Image.new('L', mask_size, 0)
    draw = ImageDraw.Draw(mask)
    
    draw.ellipse((border_width, border_width, mask_size[0] - border_width, mask_size[1] - border_width), fill=255)
    
    border_draw = ImageDraw.Draw(mask)
    border_draw.ellipse((0, 0) + mask_size, outline=255, width=border_width * 8)
    
    mask = mask.resize((width, height), Image.LANCZOS)

    bordered_img = Image.new("RGBA", (width, height), "black")

    rounded_img = Image.new("RGBA", (width, height))
    rounded_img.paste(bordered_img, (0, 0), mask=mask)
    rounded_img.paste(img, (0, 0), mask=mask)
    
    rounded_img.save(output_path, format="PNG")

def centralizar_texto_area(canvas, texto, x_inicio, largura_area, y, fonte="Helvetica", tamanho_fonte=12):
    canvas.setFont(fonte, tamanho_fonte)

    largura_texto = canvas.stringWidth(texto, fonte, tamanho_fonte)

    x_centralizado = x_inicio + (largura_area - largura_texto) / 2

    return canvas.drawString(x_centralizado, y, texto)


def create_pdf(obj):

    x,y = A4
    pdf = canvas.Canvas("scout.pdf")
    pdf.setFillColor(black)
    pdf.rect(x=0,y= 0,height=y,width= x/4,stroke=0, fill=1)
    pdf.setFillColor(whitesmoke)
    pdf.rect(x=x/4,y=0,width= x - x/4 ,height=y,stroke=0,fill=1)
    
    
    try:
        pdf.drawImage(obj['img_team'],119,y - 74,60,60, mask="auto")
    except Exception:
        ...

    round_image_with_border(obj['profile'],"imagem_arredondada.png",60,0) 


    pdf.drawImage(image="imagem_arredondada.png",width=70,height=70,x=40,y=y - 100,mask="auto")


    pdf.setFillColor(gold)
    centralizar_texto_area(pdf,obj['Name'],fonte="Helvetica-Bold",x_inicio=44,largura_area=60, y= y-130)

    pdf.setFillColor(white)
    centralizar_texto_area(pdf,position_convert(obj['pos']),fonte="Helvetica",x_inicio=44.8,largura_area=60, y= y - 150,tamanho_fonte=10)
    


    pdf.setFont("Helvetica-Bold",9)
    pdf.setFillColor(gray)
    pdf.drawString(x=10,y= y - 190,text="Data Nasc")
    pdf.setFillColor(white)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(x=9,y= y - 205,text=datetime.strptime(obj['nascimento'], "%d %b %Y").strftime("%d/%m/%Y"))

    pdf.setFont("Helvetica-Bold",9)
    pdf.setFillColor(gray)
    pdf.drawString(x=80,y= y - 190,text="Pé Dominante")
    pdf.setFillColor(white)
    centralizar_texto_area(pdf,"Direito" if obj['pé'] == "Right" else "Esquerdo",62,95,y - 205,tamanho_fonte=9,fonte="Helvetica-Bold")


    pdf.setFont("Helvetica-Bold",9)
    pdf.setFillColor(gray)
    pdf.drawString(x=17,y= y - 230,text="Altura")
    pdf.setFillColor(white)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(x=15,y= y - 245,text=f"{obj['altura']} cm")
    

    pdf.drawImage(obj['bandeira'],90,y - 246,10,10,mask='auto')
    pdf.setFont("Helvetica-Bold",9)
    pdf.setFillColor(gray)
    pdf.drawString(x=80,y= y - 230,text="Nacionalidade")
    pdf.setFillColor(white)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(x=105,y= y - 245,text=obj['nacionalidade'])

    pdf.setStrokeColor(white)
    pdf.line(0,y - 260,x/4,y - 260)

    if 'placar_mandante' in obj:
        centralizar_texto_area(pdf,"Próxima Partida" if "Tomorrow" in obj['data'] else "Última Partida",40,67,y - 280,tamanho_fonte=10,fonte="Helvetica-Bold")
        centralizar_texto_area(pdf,obj['data'] if obj['data'] and ":" not in obj['data'] else "Em Andamento",39,67,y - 295,tamanho_fonte=8,fonte="Helvetica")
    else:
        centralizar_texto_area(pdf,obj['data'],40,67,y - 280,tamanho_fonte=10,fonte="Helvetica-Bold")



    pdf.drawImage(obj['escudo_mandante'],26,y - 335,20,20, mask="auto")
    centralizar_texto_area(pdf,obj['nome_mandante'],15,40,y - 350,tamanho_fonte=8,fonte="Helvetica")

    
    if 'placar_mandante' in obj:
        centralizar_texto_area(pdf,obj['placar_mandante'] if obj['placar_mandante'] != "N/A" else "",40,50,y - 333,tamanho_fonte=20,fonte="Helvetica-Bold")
        centralizar_texto_area(pdf,"-",47.6,55,y - 332,tamanho_fonte=14,fonte="Helvetica-Bold")
        centralizar_texto_area(pdf,obj['placar_visitante'] if obj['placar_visitante'] != "N/A" else "",55,60,y - 333,tamanho_fonte=20,fonte="Helvetica-Bold")
    else:
        centralizar_texto_area(pdf,obj['data'].split(" ")[0],40,67,y - 295,tamanho_fonte=9,fonte="Helvetica")
        centralizar_texto_area(pdf,obj['data'].split(" ")[1],44,55,y - 330,tamanho_fonte=12,fonte="Helvetica-Bold")


    pdf.drawImage(obj['escudo_visitante'],x / 4 - 45,y - 335,20,20, mask="auto")
    centralizar_texto_area(pdf,obj['nome_visitante'],x_inicio=x / 4 - 50,largura_area=x / 4 - 120,y=y - 350,tamanho_fonte=8,fonte="Helvetica")

        

    pdf.setStrokeColor(white)
    pdf.line(0,y - 380,x/4,y - 380)
    pdf.setFont("Helvetica-Bold",10)
    pdf.drawString(53,y-405,"Posição")
    pdf.drawImage("images/field.png",1.5,y - 560,140,140, mask="auto")

    # POSICOES
    pdf.setFont("Helvetica-Bold",8)
    for pos in obj['positions']:
        get_positions(pos,pdf,y)
   
    pdf.drawImage("images/x_logo.png",25,y - 660,15,15,mask='auto')
    pdf.drawImage("images/logo.png",55,y - 640,35,35,mask='auto')
    pdf.setFont("Helvetica-Bold",8)
    pdf.setFillColor(white)
    pdf.drawString(44,y - 655,"@datascoutme")
    #PARTE DO SCOUT

    #TITULO

    pdf.setFillColor(black)
    centralizar_texto_area(pdf,f"{obj['liga']} {obj['temp']}",240,300,y - 40,"Courier-Bold",22)

    # PARTIDAS
    pdf.setFillColor(lightgray)
    pdf.roundRect(183,y-243,169.5,140,8,stroke=0,fill=1)
    pdf.setFillColor(white)
    pdf.roundRect(180,y-240,170,140,5,stroke=1,fill=1)
  

    pdf.drawImage("images/partidas.png",335,y-115,30,30,mask='auto')

    pdf.setFillColor(black)
    pdf.setFont("Courier-Bold",12)
    pdf.drawString(190, y - 120,"Partidas")
    pdf.setFont("Courier-Bold",24)
    pdf.drawString(190, y - 150,f"{obj['Total_played']} ")

    # DADOS PARTIDAS
    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 175,"Titular:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(221, y - 175,obj['Started'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 188,"Mins por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(249, y - 188,obj['Minutes_per_game'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 201,"Total de minutos:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(260, y - 201,obj['Total_minutes_played'])

    # Gols
    pdf.setFillColor(lightgray)
    pdf.roundRect(408,y-243,169.5,140,8,stroke=0,fill=1)
    pdf.setFillColor(white)
    pdf.roundRect(405,y-240,170,140,5,stroke=1,fill=1)


    pdf.drawImage("images/gols.png",560,y-113,25,25,mask='auto')



    pdf.setFillColor(black)
    pdf.setFont("Courier-Bold",12)
    pdf.drawString(415, y - 120,"Gols")
    pdf.setFont("Courier-Bold",24)
    pdf.drawString(415, y - 150,obj['Goals'])

    # DADOS Gols
    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 175,"xG:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(432, y - 175,obj['Expected_Goals_(xG)'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 188,"Gols por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(473, y - 188,obj['Goals_per_game'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 201,"Gols Com Pé Esquerdo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(515, y - 201,obj['Left_foot_goals'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 214,"Gols Com Pé Direito:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(502, y - 214,obj['Right_foot_goals'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 227,"Gols de Cabeça:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(485, y - 227,obj['Headed_goals'])

    # Passe
    pdf.setFillColor(lightgray)
    pdf.roundRect(183,y-413,169.5,140,8,stroke=0,fill=1)
    pdf.setFillColor(white)
    pdf.roundRect(180,y-410,170,140,5,stroke=1,fill=1)


    pdf.drawImage("images/assistencias.png",337,y-283,30,30,mask='auto')

    pdf.setFillColor(black)
    pdf.setFont("Courier-Bold",12)
    pdf.drawString(190, y - 290,"Assistências")
    pdf.setFont("Courier-Bold",24)
    pdf.drawString(190, y - 320,obj['Assists'])

    # Dados Passe

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 345,"xA:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(205, y - 345,obj['Expected_Assists_(xA)'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 358,"Grande Chances Criadas:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(298, y - 358,obj['Big_chances_created'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 371,"Acerto em Passes:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(268, y - 371,obj['Accurate_per_game'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 384,"Acerto em Lançamentos:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(293, y - 384,obj['Acc._long_balls'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 397,"Acerto em Cruzamentos:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(293, y - 397,obj['Acc._crosses'])

    # defesa
    pdf.setFillColor(lightgray)
    pdf.roundRect(408,y-413,169.5,140,8,stroke=0,fill=1)
    pdf.setFillColor(white)
    pdf.roundRect(405,y - 410,170,140,5,stroke=1,fill=1)


    pdf.drawImage("images/desarmes.png",560,y-283,30,30,mask='auto')


    pdf.setFillColor(black)
    pdf.setFont("Courier-Bold",12)
    pdf.drawString(415, y - 290,"Desarmes por Jogo")
    pdf.setFont("Courier-Bold",24)
    pdf.drawString(415, y - 320,obj['Tackles_per_game'])


    # DADOS defesa

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 345,"Interceptação por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(509, y - 345,obj['Interceptions_per_game'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 358,"Bolas Recuperadas por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(534, y - 358,obj['Balls_recovered_per_game'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 371,"Dribles Sofridos por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(519, y - 371,obj['Dribbled_past_per_game'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 384,"Duelos Vencidos no Chão:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(524, y - 384,obj['Ground_duels_won'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 397,"Duelos Aéreos Vencidos:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(518, y - 397,obj['Aerial_duels_won'])

    # Outros
    pdf.setFillColor(lightgray)
    pdf.roundRect(183,y-583,169.5,140,8,stroke=0,fill=1)
    pdf.setFillColor(white)
    pdf.roundRect(180,y-580,170,140,5,stroke=1,fill=1)

  
    pdf.drawImage("images/outros.png",337,y-450,20,20,mask='auto')


    pdf.setFillColor(black)
    pdf.setFont("Courier-Bold",12)
    pdf.drawString(190, y - 460,"Outros I")

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 485,"Dribles Completos por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(304, y - 485,obj['Succ._dribbles'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 498,"Perda da bola por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(285, y - 498,obj['Possession_lost'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 511,"Faltas Sofridas por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(291, y - 511,obj['Was_fouled'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 524,"Faltas Cometidas por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(300, y - 524,obj['Fouls'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 537,"Impedimentos por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(286, y - 537,obj['Offsides'])


    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 549,"Erros que levaram ao chute:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(305, y - 549,obj['Error_led_to_shot'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(190, y - 561,"Erros que levaram ao gol:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(296, y - 561,obj['Error_led_to_goal'])


    # outros II
    pdf.setFillColor(lightgray)
    pdf.roundRect(408,y-583,169.5,140,8,stroke=0,fill=1)
    pdf.setFillColor(white)
    pdf.roundRect(405,y-580,170,140,5,stroke=1,fill=1)


    pdf.drawImage("images/outros.png",563,y-452,20,20,mask='auto')


    pdf.setFillColor(black)
    pdf.setFont("Courier-Bold",12)
    pdf.drawString(415, y - 460,"Outros II")

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 485,"Passes Chaves por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(518, y - 485,obj['Key_passes'])

    
    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y -498,"Grande Chances Perdidas:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(526, y -498,obj['Big_chances_missed'])

    
    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)   
    pdf.drawString(415, y - 511,"Ações com a bola por jogo:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(526, y - 511,obj['Touches'])


    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 524,"Cartões Amarelos:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(492, y - 524,obj['Yellow'])


    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 537,"Amarelo + Vermelho:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(501, y - 537,obj['Yellow-Red'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica",9)
    pdf.drawString(415, y - 550,"Cartões Vermelhos:")
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(497, y - 550,obj['Red_cards'])

    pdf.setFillColor(gray)
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawString(x - 150,22,"*N/A: Sem Dados")
    pdf.drawString(x - 150,10,"*Dados obtidos no Sofascore")
    pdf.save()