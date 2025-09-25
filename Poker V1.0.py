#######################################################################
# Nombre: Iker García Caba
# Fecha: 25/09/2025
# Programa: AceMaster
# Objetivo: Simular una partida de poker, con un jugador guiado por AceMaster, que se enfrentará
# a otros 5 jugadores en una partida de texas hold'em clásica
#
########################################################################
import random as rand
rand.seed(7)
class Card:
    def __init__(self, valor: int, palo: str):
        if valor in ('A','Q','K','J'):
            self.valor:str= valor
        else:
            self.valor:int=valor
        self.palo=palo


class Player:
    def __init__(self, card1,card2, position: int=1,chips: int=0, bet:bool=False):
        '''
        Recuerda que si card1 y card2 son objetos tienes que alimentarles por separado, ya que en deck.deal aparecerán como una lista de dos elementos
        '''
        if card1.valor>card2.valor:
            self.card1=card1
            self.card2=card2
        else:
            self.card1=card2
            self.card2=card1
        self.position=position
        self.chips= chips
        self.bet=bet

class Deck:
    def __init__(self, mazo:list):
        self.mazo=mazo
    def shuffle():
        self.mazo=rand.shuffle(self.mazo)
        return self.mazo
    def deal(self,n: int):
        cartas=[]
        for x in range(n):
            card=self.mazo.pop()
            cartas.append(card)
        return cartas
            
            


    


def CrearMazo():
    mazo: list =[]
    palos: list[str,str,str,str]=['clubs','spades','hearts','diamonds']
    letras: dict={'A':14,'Q':12,'J':11,'K':13}
    for x in range(10):
        for p in palos:
            card=Card(valor=x+1,palo=p)
            mazo.append(card)
    for x in letras:
        for p in palos:
            card=Card(valor=letras[x],palo=p)
            mazo.append(card)

    return mazo


        


