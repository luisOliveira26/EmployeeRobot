#importar bibliotecas 
import vlc 
import tkinter as tk 
import RPi.GPIO as GPIO 
import time 
#chamamento dos videos 
video1 = "videos/b3.mp4" 
player1 = vlc.MediaPlayer(video1) 
video2 ="videos/b4.mp4" 
player2 = vlc.MediaPlayer(video2) 
video3 ="videos/b5.mp4" 
player3 = vlc.MediaPlayer(video3) 
video4 ="videos/b6.mp4" 
player4 = vlc.MediaPlayer(video3) 
#definir pinos 
OUTPin1 = 11    
BtnPin1 = 3    
BtnPin2 = 5    
BtnPin3 = 7    
# pin11 --- out1 
# pin3 --- button1 
# pin5 --- button2 
# pin7 --- button3 
# definir pinos como entrada ou saidas 
print ('Program is starting...') 
GPIO.setmode(GPIO.BOARD)       
GPIO.setup(OUTPin1, GPIO.OUT)   
# Numbers GPIOs by physical location 
# Set OUTPin's mode is output 
GPIO.setup(BtnPin1, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)#, pull_up_down=GPIO.PUD_UP)    # 
Set buttonPin's mode is input, and pull up to high level(3.3V) 
GPIO.setup(BtnPin2, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)    # Set buttonPin's mode is 
input, and pull up to high level(3.3V) 
GPIO.setup(BtnPin3, GPIO.IN)#, pull_up_down=GPIO.PUD_UP) 
# criação da janela  
def createjanauto(previouswindow): 
GPIO.output(OUTPin1, GPIO.LOW) #envio de sinal para o robo parar 
janauto = tk.Tk() 
janauto.attributes('-fullscreen', True) #meter ecra cheio 
labelsala = tk.Label(janauto, text = "Pretende começar a visita?",font=("Arial", 25)) 
# criar legenda 
labelsala.place(x=550, y=100) #posicionar legenda 
buttonB3 = tk.Button(janauto, text ="Sim",height=2,width=15,bg = 
"green",font=("Arial", 15), command= lambda: createjanb3(janauto)) #criar botão 
buttonB3.place(x=630, y=300) #posicionar botão 
buttonB4 = tk.Button(janauto, text="Voltar",height=2,width=15,bg = 
"red",font=("Arial", 15), command= lambda: createjanmov(janauto)) 
buttonB4.place(x=630, y=500) 
previouswindow.destroy() #fechar a janela anterior 
def createjanclose(previouswindow): 
GPIO.output(OUTPin1, GPIO.LOW) 
janclose = tk.Tk() 
janclose.attributes('-fullscreen', True) 
label10 = tk.Label(janclose, text="Pretende continuar?",font=("Arial",  
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 82 
PAP 
SchoolBot 
25)) 
label10.place(x=560, y=100) 
buttonsim = tk.Button(janclose,width = 20, text = "Sim",font=("Arial", 15),command = 
lambda: createjanb3(janclose)) 
buttonsim.place(x=600, y=400) 
buttonnao = tk.Button(janclose, width=20, text="Não",font=("Arial", 
15),command=lambda: createjanfechar(janclose)) 
buttonnao.place(x=600, y=600) 
previouswindow.destroy() 
def createjanmov(previouswindow): 
GPIO.output(OUTPin1, GPIO.LOW) 
janmov = tk.Tk() 
janmov.attributes('-fullscreen', True) 
buttonauto = tk.Button(janmov,text="Automático", bg = "blue", height=3,width=15,fg = 
"white",font=("Arial", 15),command= lambda: createjanauto(janmov)) 
buttonauto.place(x=650, y=250) 
buttonmanu = tk.Button(janmov,text="Manual",bg = "blue", height=3,width=15,fg= 
"white",font=("Arial", 15),command= lambda: createjanmanu(janmov)) 
buttonmanu.place(x=650, y=400) 
buttonquit = tk.Button(janmov, text="Sair",activebackground="red",bg = "blue", 
height=3,width=15, fg="white",font=("Arial", 15),command= lambda: createjanfechar(janmov)) 
#https://www.educba.com/python-tkinter-button/ 
buttonquit.place(x=650, y=550) #1500.800 
labelmov = tk.Label(janmov, text = "Selecione o tipo de controlo",font=("Arial", 25)) 
labelmov.place(x=550, y=100) 
previouswindow.destroy() #tem que fechar no final do def para que este não feche a 
janela sem criar uma nova  
def createjanfechar(previouswindow): 
GPIO.output(OUTPin1, GPIO.LOW) 
janfechar = tk.Tk() 
janfechar.attributes('-fullscreen', True) 
label10 = tk.Label(janfechar, text="Pretende sair?",font=("Arial", 25)) 
label10.place(x=610, y=100) 
buttonsim = tk.Button(janfechar,width = 20, text = "Sim",font=("Arial", 15),command = 
lambda: janfechar.destroy()) 
buttonsim.place(x=600, y=300) 
buttonnao = tk.Button(janfechar, width=20, text="Não",font=("Arial", 
15),command=lambda: createjanmov(janfechar)) 
buttonnao.place(x=600, y=500) 
previouswindow.destroy() 
#criação da janela quando o robo chega á sala 
def createjanb3(previouswindow): 
GPIO.output(OUTPin1, GPIO.HIGH) # Mandar o robo se mover 
jan = 3 
janb3 = tk.Tk() 
janb3.attributes('-fullscreen', True) 
label5 = tk.Label(janb3, text="Movendo se para sala B3",font=("Arial", 25),bg = 
"blue") 
label5.place(x=550, y=100) 
label6 = tk.Label(janb3, text="Segue-me, Obrigado",font=("Arial", 15)) 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 83 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 84 
 
PAP 
SchoolBot 
 
 
    label6.place(x=650, y=200) 
    labelcara = tk.Label(janb3, text="^_^",font=("Arial", 200)) 
    labelcara.place(x=550, y=250) 
    janb3.destroy() 
     
previouswindow.destroy() 
     
    #esperar que o robo detete uma sala 
    while True: 
        
        if GPIO.input(BtnPin1)==GPIO.HIGH and GPIO.input(BtnPin2)==GPIO.HIGH: and 
GPIO.input(BtnPin3)==GPIO.LOW: 
            GPIO.output(OUTPin1, GPIO.LOW) 
            player1 = vlc.MediaPlayer(video1) 
            player1.play() 
            player1.set_fullscreen(True) 
            time.sleep (56) 
            player1.stop() 
            createjanclose(previouswindow)     
            print ('stop ...') 
 
        if GPIO.input(BtnPin1) == GPIO.HIGH and GPIO.input(BtnPin2) == GPIO.LOW: and 
GPIO.input(BtnPin3) == GPIO.HIGH: 
            GPIO.output(OUTPin1, GPIO.LOW) 
            player1 = vlc.MediaPlayer(video2) 
            player1.play() 
            player1.set_fullscreen(True) 
            time.sleep (59) 
            player1.stop() 
            createjanclose(previouswindow)     
            print ('stop ...') 
             
        if GPIO.input(BtnPin1)==GPIO.HIGH and GPIO.input(BtnPin2)==GPIO.HIGH: and 
GPIO.input(BtnPin3)==GPIO.LOW: 
            GPIO.output(OUTPin1, GPIO.LOW) 
            player1 = vlc.MediaPlayer(video3) 
            player1.play() 
            player1.set_fullscreen(True) 
            time.sleep (48) 
            player1.stop() 
            createjanclose(previouswindow)     
            print ('stop ...') 
 
        if GPIO.input(BtnPin1) == GPIO.HIGH and GPIO.input(BtnPin2) == GPIO.HIGH: and 
            GPIO.input(BtnPin3) == GPIO.HIGH: 
            GPIO.output(OUTPin1, GPIO.LOW) 
            player1 = vlc.MediaPlayer(video4) 
            player1.play() 
            player1.set_fullscreen(True) 
            time.sleep(53) 
            player1.stop() 
            createjanclose(previouswindow) 
            print('stop ...') 
             
 
 
def createjanmanu(previouswindow): 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 85 
 
PAP 
SchoolBot 
    GPIO.output(OUTPin1, GPIO.LOW) 
    janmanu = tk.Tk() 
 
 
    janmanu.attributes('-fullscreen', True) 
    label5 = tk.Label(janmanu, text="Controlo manual ativado",font=("Arial", 25)) 
    label5.place(x=600, y=100) 
    label6 = tk.Label(janmanu, text="Use a App",font=("Arial", 15)) 
    label6.place(x=740, y=200) 
    buttonfim = tk.Button(janmanu,text="Fim",font=("Arial", 15),height=3,width=15,bg = 
"grey",command= lambda: createjanfechar(janmanu))#command= 
combine_funcs(createNewWindow3)) 
    buttonfim.place(x=700, y=400) 
    previouswindow.destroy() 
 
 
 
 
 
    previouswindow.destroy() 
def createjaninicio(): 
    GPIO.output(OUTPin1, GPIO.LOW) 
    print ('play ...') 
    inicio = tk.Tk() 
    inicio.attributes('-fullscreen', True) 
    labelbv = tk.Label(inicio, text="Seja bem-vindo ao Bloco B", font=("Arial", 15)) 
    labelbv.place(x=600, y=200) 
    buttoncomecar = tk.Button(inicio,text="Começar", font=("Arial", 25),command= lambda: 
createjanmov(inicio)) 
    buttoncomecar.place(x=650, y=400) 
     
             
 
    inicio.mainloop() 
     
 
  
     
# criar a janela inicial 
createjaninicio() 
