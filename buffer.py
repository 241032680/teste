import array
import struct

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
    #mascara pq a bosta do python fica cortando os zeros frontais
    pacote = array.array('H', [((ação&0x4f)<<2 |(custo&0x3))<<8 | ((alvo&0xf)<<4 |(cargo&0x7)<<1 |(prox&0x1))])
    buffer.extend(pacote)
    return buffer

def listar_pacotes():
    a = max((pac.bit_length() for pac in buffer), default=0)
    for x, pac in enumerate(buffer):
        print(f'{x}: {pac:0{a}b}')

def read_buffer(pos):
        packbytes = struct.pack('<H', buffer[pos])
        unpack = struct.unpack('<H', packbytes)[0]
        Ação = (unpack >> 10) & 0x3F #0011 1111
        Custo = (unpack >> 8) & 0x03 #0000 0011
        Alvo = (unpack >>  4) & 0x0F #0000 1111
        Cargo = (unpack >> 1) & 0x07 #0000 0111
        Prox = (unpack)       & 0x01 #0000 0001
        return (Ação, Custo, Alvo, Cargo, Prox)

def confirmar_acoes(cargo):
    if cargo not in ("piloto", "copiloto", "engenheiro", "atirador", "aae"): return print("Cargo Invalido")
    for x in range(0, len(buffer)):
        args = read_buffer(x)
        if args[0] == 0:
            atirar(args[2], args[3])
        elif args[0] ==1:
            ajustar_util(args[2])
        max(ações_cargo[args[3]] - int(args[1]), 0)
