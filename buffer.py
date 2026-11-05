import array
import struct


#checklist:
#adicionar ação no buffer (seleção)
#remover ultima ação (undo)
#poder ler e interpretar o buffer (transformar encoding em função)

def buffer():
    pass

#2 bytes por pacote:

#Byte 1: Ação
#6 bits: ação (0-63; 1-64)
#2 bits: custo de ações (0-3; 1-4)

#Byte 2: Interagíveis
#4 bits: alvo (0-15; 1-16)
#3 bits: cargo (0-7; 1-8)
#1 bit: booleano "continuar próxima rodada" (0-1)


ação, custo, alvo, cargo, prox = 60, 2, 13, 6, 0

pacote = ação<<10 | custo<<8 | alvo<<4 | cargo<<1 | prox
action_queue = array.array('H', [pacote])
print(f'{pacote:b}')

ação = 111100 #max 11 1111
custo = 10 #max 11
alvo = 1101 #max 1111
cargo = 110 #max 111
prox = 0 #max 1

#1111 00-- ---- ----
#**** **10 ---- ----
#**** **** 1101 ----
#**** **** **** 110-
#**** **** **** ***0
#=
#1111 0010 1101 1100
#
#1111 00-- ---- ----
#**** **** **11 1111
#
#---- ---- --11 1100 #pacote <<10
#**** **** **11 1111 #mascara
#0000 0000 0011 1100
#
#1111 0010 1101 1100
#
#---- ---- 1111 0010 #pacote <<8
#**** **** 0000 0011 #mascara
#0000 0000 0000 0010

buffbytes = struct.pack('<H', pacote) #rep binaria pra salvar

recovered_val = struct.unpack('<H', buffbytes)[0]
print(f'{recovered_val:b}')
#shift: posição do bloco no pacote; mascara: numero de bits
ação = (recovered_val >> 10) & 0x3F #0011 1111
custo = (recovered_val >> 8)  & 0x03 #0000 0011
alvo = (recovered_val >>  4) & 0x0F #0000 1111
cargo  = (recovered_val >> 1) & 0x07      #0000 0111
prox = (recovered_val & 0x01) #0000 0001
print(f'{ação:0{ação.bit_length()}b} {custo:0{custo.bit_length()}b} {alvo:0{alvo.bit_length()}b} {cargo:0{cargo.bit_length()}b} {prox:0{prox.bit_length()}b} ')
print(f'{ação} {custo} {alvo} {cargo} {prox}')