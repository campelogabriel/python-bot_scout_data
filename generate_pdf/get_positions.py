from .positions_field import get_AM,get_CB,get_DL,get_DM,get_DR,get_GK,get_LW,get_MC,get_ML,get_MR,get_RW,get_ST

def get_positions(pos,pdf,y):
    if pos == 'AM':
        return get_AM(pdf,y)
    if pos == 'CB':
        return get_CB(pdf,y)
    if pos == 'DL':
        return get_DL(pdf,y)
    if pos == 'DM':
        return get_DM(pdf,y)
    if pos == 'DR':
        return get_DR(pdf,y)
    if pos == 'ML':
        return get_ML(pdf,y)
    if pos == 'GK':
        return get_GK(pdf,y)
    if pos == 'LW':
        return get_LW(pdf,y)
    if pos == 'MC':
        return get_MC(pdf,y)
    if pos == 'RW':
        return get_RW(pdf,y)
    if pos == 'ST':
        return get_ST(pdf,y)
    if pos == 'MR':
        return get_MR(pdf,y)


