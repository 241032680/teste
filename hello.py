print("Hello world!")

import array 
import struct

def atirar(bar):
    pass
def ajustar_util(foo):
    pass    

buffer = array.array('H')
def add_buffer(ação, custo, alvo, cargo, prox):
    #2 bytes por pacote:
    #--
    #Byte 1: Ação
    #6 bits: ação (0-63; 1-64)
    #2 bits: custo de ações (0-3; 1-4)
    #--
    #Byte 2: Interagíveis
    #4 bits: alvo (0-15; 1-16)
    #3 bits: cargo (0-7; 1-8)
    #1 bit: booleano "continuar próxima rodada" (0-1)
    
    pacote = ação<<10 | custo<<8 | alvo<<4 | cargo<<1 | prox
    action_queue = array.array('H', [pacote])
    buffer.extend(action_queue)
    return buffer

def listar_pacotes():
    a = max((pac.bit_length() for pac in buffer), default=0)
    for x, pac in enumerate(buffer):
        print(f'{x}: {pac:0{a}b}')

def read_buffer(pos):
        pacote = buffer[pos]
        packbytes = struct.pack('<H', pacote)
        unpack = struct.unpack('<H', packbytes)[0]
        Ação = (unpack >> 10) & 0x3F #0011 1111
        Custo = (unpack >> 8) & 0x03 #0000 0011
        Alvo = (unpack >>  4) & 0x0F #0000 1111
        Cargo = (unpack >> 1) & 0x07 #0000 0111
        Prox = (unpack)       & 0x01 #0000 0001
        return [Ação, Custo, Alvo, Cargo, Prox]


def confirmar_acoes(cargo):
    if cargo not in ("piloto", "copiloto", "engenheiro", "atirador", "aae"): return "Cargo Invalido"
    for x in range(0, len(buffer)+1):
        args = read_buffer(x)
        if args[0] == 0:
            return atirar(args[3], args[4])
        elif args[0] ==1:
            return ajustar_util(args[3])
        max(ações_cargo[Cargo] - int(Custo), 0)

add_buffer(1, 2, 2, 1, 1)
add_buffer(12, 3, 2, 1, 1)
add_buffer(11, 1, 5, 3, 0)
listar_pacotes()
print(read_buffer(2))
confirmar_acoes("piloto")