from reportlab.lib.colors import black,salmon,springgreen,lightskyblue,gold

def get_LW(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(39,y-448,8,stroke=0,fill=1)
    pdf.setFillColor(salmon)
    pdf.drawString(33.5,y-450.9,"PE")

def get_RW(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(104.8,y-448,8,stroke=0,fill=1)
    pdf.setFillColor(salmon)
    pdf.drawString(99.5,y-450.9,"PD")


def get_ST(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(71.5,y-439.7,8,stroke=0,fill=1)
    pdf.setFillColor(salmon)
    pdf.drawString(65.8,y-443,"CA")


def get_AM(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(71.5,y-463.7,8,stroke=0,fill=1)
    pdf.setFillColor(springgreen)
    pdf.drawString(65.5,y-466.4,"MA")

def get_MC(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(71.5,y-488.7,8,stroke=0,fill=1)
    pdf.setFillColor(springgreen)
    pdf.drawString(65.5,y-491.4,"MC")

def get_MR(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(104.8,y-488,7.5,stroke=0,fill=1)
    pdf.setFillColor(springgreen)
    pdf.drawString(99,y-490.9,"MD")

def get_ML(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(39,y-488,7.5,stroke=0,fill=1)
    pdf.setFillColor(springgreen)
    pdf.drawString(33.5,y-490.9,"ME")

def get_DM(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(71.5,y-514,8,stroke=0,fill=1)
    pdf.setFillColor(springgreen)
    pdf.drawString(66.7,y-517,"VL")

def get_CB(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(71.5,y-536,8,stroke=0,fill=1)
    pdf.setFillColor(lightskyblue)
    pdf.drawString(66.4,y-539,"ZG")

def get_DR(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(104,y-527,8,stroke=0,fill=1)
    pdf.setFillColor(lightskyblue)
    pdf.drawString(99.3,y-530,"LD")


def get_DL(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(39,y-527,8,stroke=0,fill=1)
    pdf.setFillColor(lightskyblue)
    pdf.drawString(34,y-530,"LE")

def get_GK(pdf,y):
    pdf.setFillColor(black)
    pdf.circle(71.5,y-546,8,stroke=0,fill=1)
    pdf.setFillColor(gold)
    pdf.drawString(65.7,y-549,"GK")