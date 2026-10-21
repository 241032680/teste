def tipodano():
    tpd = rand()%6
    match tpd:
        case 0:
            return "íon" # +dano escudo -dano casco
        case 1|2: 
            return "plasma" #-dano escudo +dano casco
        case 3|4|5: 
            return "proton" #sem modificadores

def tipoescudo():
    scd = rand()%8
    match scd:
        case 0:
            return "Deflector" #padrao
        case 1: 
            return "Conversion" #quando o escudo é desativado, desliga todas as armas mas cria uma barreira forte
        case 2: 
            return "Fortificado" #mais forte, regenera mais devagar
        case 3:
            return "Nimble" #mais fraco, regenera mais rapido
        case 4:
            return "Overloaded" #muito mais forte, regenera lento, não regenera se completamente derrubado
        case 5:
            return "Ray" #leva menos dano de torretas e mais dano de torpedos
        case 6:
            return "Resonant" #Mais fraco, aumenta o dano das proprias armas
        case 7:
            return "Scrambler" #Dificulta lock in misseis e torretas quando 100%, demora mais p/ começar a regenerar

def tipomissel():
    msl = rand()%4
    match msl:
        case 0: #misseis
            if inimigos[['tipo']]=="pesado":
                msl1=rand()%4
            else:
                msl1=rand()%3
            match msl1:
                case 0:
                    return "Concussion"
                case 1:
                    return "Ion"
                case 2:
                    return "Multi-Lock"
                case 3:
                    return "Goliath"
        case 1: #torpedos
            pass
        case 2: #bombas
            pass
        case 3: #foguetes
            pass