import array
import struct


#checklist:
#adicionar ação no buffer (seleção)
#remover ultima ação (undo)
#poder ler e interpretar o buffer (transformar encoding em função)

def buffer():
    pass

ação, alvo, cargo = 5,6,7
pacote = (ação << 9) | (alvo << 4) | cargo
action_queue = array.array('H', [pacote])

buffbytes = struct.pack('<H', pacote) #rep binaria pra salvar

recovered_val = struct.unpack('<H', buffbytes)[0]

#shift: ponteiro do bloco; mascara: valor maximo do bloco
ação = (recovered_val >> 9) & 0x7F
alvo = (recovered_val >> 4) & 0x1F
cargo  = recovered_val & 0x0F
