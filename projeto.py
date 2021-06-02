GlowScript 3.1 VPython
def parAndar(): # faz a simulação parar e andar
    global inic,anda,om
    if inic==False: # se a simulação não foi iniciada
        om=sqrt(g/(l*cos(radians(ang)))) # cálculo da frequencia angular
        inic=True # agora, está iniciada
    anda=not anda # mudar andamento
    rad_andar.checked=anda

def reiniciar(): # reiniciar a simulação
    global inic,anda,t
    if not inic: # se não foi iniciada
        return   # nada faz
    inic,anda=False,False
    rad_andar.checked=anda # colocar o botão de simulação na posição "parada"
    t=0 # restaurar o tempo

def ajustAng(): # ajustar o angulo de inclinação do pendulo
    global ang
    if inic==False: # se a simulação não estiver iniciada
        ang=angSlid.value # ler o valor indicado pelo cursor
        angLb.text=angStr.format(ang) # informar novo valor do Angulo
        configurar() # chamar a função de configurara
    else: # caso contrario (a simulação foi iniciada)
        angSlid.value=ang # apenas confirmar o valor vigente/atualizado
        
def ajustVel(): # ajustar Velocidade
    global vel
    if inic==False: # se a simulação ñ estiver iniciada
        vel=VelSlid.value # ler o valor indicado pelo cursor
        VelLb.text=VelStr.format(vel) # informar novo valor da Velocidade
        configurar() # chamar a função de configurar
    else: # caso contrario (a simulação foi iniciada)
        VelSlid.value=vel # apenas confirmar o valor vigente
        
def ajustMC(): # ajustar Massa Carrinho
    global mc
    if inic==False: # se a simulação ñ estiver iniciada
        mc=MCSlid.value # ler o valor indicado pelo cursor
        MCLb.text=MCStr.format(mc) # informar novo valor da Massa
        configurar() # chamar a função de configurar
    else: # caso contrario (a simulação foi iniciada)
        MCSlid.value=mc # apenas confirmar o valor vigente

def ajustMP(): # ajustar Massa Carrinho
    global mp
    if inic==False: # se a simulação ñ estiver iniciada
        mp=MPSlid.value # ler o valor indicado pelo cursor
        MPLb.text=MPStr.format(mp) # informar novo valor da Massa
        configurar() # chamar a função de configurar
    else: # caso contrario (a simulação foi iniciada)
        MPSlid.value=mp # apenas confirmar o valor vigente
        
def configurar(): # configura a posição do pendulo (bolinha e do fio)
    global r
    r=l*sin(radians(ang)) # raio da trajetoria
    x,y,z=r*cos(fi),-l*cos(radians(ang)),r*sin(fi) # coordenadas da bolinha
    fio.axis=vector(l*sin(fi),-l*cos(fi),0)  # eixo do fio
    bob.pos=Mass.pos+vector(l*sin(fi),pivot.y-l*cos(radians(ang)),0)
    bob.mass=mp
    bob.radius=mp
    Mass.mass=mc        

def mover(): # mover a bolinha e o fio
    global fi,t
    fi+=om*dt+vel # incrementar o Angulo de rotação
    x,z=r*cos(fi),r*sin(fi) # novos valores de x e z
    fio.axis.x,fio.axis.z=x,z # girar eixo do fio
    acc=(eq-Mass.pos)*(spring.constant/Mass.mass)
    Mass.velocity+=acc*dt
    Mass.pos+=Mass.velocity*dt
    spring.axis=Mass.pos-spring.pos
    fio.pos=Mass.pos
    bob.pos=Mass.pos+vector(l*sin(fi),pivot.y-l*cos(radians(ang)),0) 
    fio.axis=bob.pos-fio.pos #calcular eixo
    t+=dt # incrementar o tempo

# ******* configuração **********
mp=1
mc=5
scene=canvas(title='Pendulo + Carrinho',width=1200,height=800,background=color.white)
bob=sphere(pos=vector(10,0,10),mass=mp,radius=mp,color=vector(0.121, 0.527, 0.813))
wall=box(pos=vector(0,1,0),size=vector(0.2,3,2),color=color.black) 
floor=box(pos=vector(6,-0.6,0),size=vector(60,0.1,5),color=color.black)
Mass=box(pos=vector(10,0,10),velocity=vector(0,0,0),size=vector(2,2,2),mass=mc,color=color.blue)
pivot=vector(0,0,0)
spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.4,constant=0.5,thickness=0.1,coils=20,color=color.red)
eq=vector(9,0,0)
pivot=vector(0,10,0)
fio=cylinder(pos=Mass.pos,radius=0.1,color=color.black)
l=mag(bob.pos-pivot)
fi=pi/4
g=9.8 #gravitacão 
ang=0
vel=0.01
configurar() # chamar função para configurar
angStr='Angulo={0:.3g} graus.' # cadeia a ser formatada
angLb=label(pos=vector(1,17,0),text=angStr.format(ang),opacity=0, box=0, line=0) # rotulo
VelStr='Velocidade={0:.3g}' # cadeia a ser formatada
VelLb=label(pos=vector(1,15,0),text=VelStr.format(vel),opacity=0, box=0, line=0) 
MPStr='Massa do Pendulo={0:.3g}' # cadeia a ser formatada
MPLb=label(pos=vector(1,19,0),text=MPStr.format(mp),opacity=0, box=0, line=0)
MCStr='Massa do Carro={0:.3g}' # cadeia a ser formatada
MCLb=label(pos=vector(1,20,0),text=MCStr.format(mc),opacity=0, box=0, line=0)
# ********** montagem dos controles ****************************
wtext(text="<span style='color:MediumSeaGreen;'>Ajuste o valor da Massa Pendulo:</span>")
scene.append_to_caption("\n\n") # proxima linha
MPSlid=slider(width=10,length=200, min=1, max=25,left=100,top=4,bottom=0,bind=ajustMP)
MPSlid.value=mp # ajuste da posição inicial do cursor
scene.append_to_caption("\n")
wtext(text="<span style='color:MediumSeaGreen;'>Ajuste o valor da Massa Carrinho:</span>")
scene.append_to_caption("\n\n") # proxima linha
MCSlid=slider(width=10,length=200, min=1, max=100,left=100,top=4,bottom=0,bind=ajustMC)
MCSlid.value=mc # ajuste da posição inicial do cursor
scene.append_to_caption("\n")
# Criar uma barra para modificar a Velocidade
wtext(text="<span style='color:MediumSeaGreen;'>Ajuste o valor da Velocidade:</span>")
scene.append_to_caption("\n\n") # proxima linha
VelSlid=slider(width=10,length=200, min=0, max=1,left=100,top=4,bottom=0,bind=ajustVel)
VelSlid.value=vel # ajuste da posição inicial do cursor
scene.append_to_caption("\n\n") # espaçamento vertical 
# Criar uma barra para modificar o Angulo
wtext(text="<span style='color:MediumSeaGreen;'>Ajuste o valor do Angulo:</span>")
scene.append_to_caption("\n\n")
angSlid=slider(width=10,length=200, min=0, max=60,left=100,top=5,bottom=0,bind=ajustAng)
angSlid.value=ang # ajuste da posição inicial do cursor
scene.append_to_caption("\n\n") #espaçamento vertical 
# Criar um interruptor de animação na janela de controle
rad_andar=radio(text="<span>Andar</span>",bind=parAndar,checked=False)
scene.append_to_caption("\t\t")
# Criar um botão "reiniciar" na janela de controle
button(text="Reiniciar",background=vector(0.9,0.9,1),bind=reiniciar)
inic,anda=False,False # controles da simulação
dt=0.01 # intervalo de tempo
t=0 # tempo mas foi assim que fiz parte a parte, o problema mantem se depois mesmo com esta aletração que ele falou
while True: #principal
    rate(60) # ñ mais de 60 passos/segundo 
    if anda: # se a simulação estiver em andamento
        mover()