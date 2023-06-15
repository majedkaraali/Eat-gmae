import subprocess
import sys
import time
########################################################################################## Libaries

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])



print("-Code By Majed")

def reload(metin,tekrar):
    for i in range(tekrar):
        print(metin,"/ ",end="\r")
        time.sleep(0.1)
        print(metin,"- ",end="\r")
        time.sleep(0.1)
        print(metin,"\ ",end="\r")
        time.sleep(0.1)
        print(metin,"| ",end="\r")
        time.sleep(0.1) 
        
reload("-Please wait",4)

time.sleep(1)
print("Welcome to the game / Oyuna hoş geldiniz")
time.sleep(1)
print("Checking required libraries / Gerekli kütüphaneler kontrol ediliyor")
time.sleep(1)
print("Required libraries are [tkinter,Pillow,playsound] / gerekli kütüphaneler [tkinter,Pillow,playsound]")
time.sleep(1)

try:
    print("[GAME] Trying to import tkinter ")
    from tkinter import *
except:
    print("[EXCEPTION] tkinter not installed")
    try:
        print("[GAME] Trying to install tkinter via pip")
        import pip
        install("tk")
        print("[GAME] tkinter has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")

try:
    print("[GAME] Trying to import Pillow")
    import PIL
except:
    print("[EXCEPTION] Pillow not installed")
    try:
        print("[GAME] Trying to install Pillow via pip")
        import pip
        install("Pillow")
        print("[GAME] Pillow has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")

try:
    print("[GAME] Trying to import playsound")
    import playsound
except:
    print("[EXCEPTION] playsound not installed")
    try:
        print("[GAME] Trying to install playsound via pip")
        import pip
        install("playsound")
        install("playsound==1.2.2")
        print("[GAME] playsound has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
##########################################################################################
# MaJeDo



from tkinter import *
from PIL import ImageTk, Image
import random
import threading
from playsound import playsound

root=Tk()
root.title("Eat!")
root.configure(bg='#8FBC8F')
root.iconbitmap("jpg/favicon.ico")

################### Varibales
score=0
hit=False
dead=False
health=95
dil="EN"
in_how_frame=False
first_open=True
qut=False
bandge_part=0
bleed=False
star_bleed=False
virus_count=0
food_count=0

Timer=0.8
###################



##########################################################   images
how_en=ImageTk.PhotoImage(Image.open("jpg/HOW2.png"))
how_tr=ImageTk.PhotoImage(Image.open("jpg/HOWTR.png"))
how_ar=ImageTk.PhotoImage(Image.open("jpg/HOWAR.png"))

bag=ImageTk.PhotoImage(Image.open("jpg/bag.jpg"))
en=ImageTk.PhotoImage(Image.open("jpg/EN.jpg"))
tr=ImageTk.PhotoImage(Image.open("jpg/TR.jpg"))    
ar=ImageTk.PhotoImage(Image.open("jpg/AR.jpg"))

hp=ImageTk.PhotoImage(Image.open("jpg/hp.jpg"))
imga=ImageTk.PhotoImage(Image.open("jpg/noclip.jpg"))
img=ImageTk.PhotoImage(Image.open("jpg/food.jpg"))      #   3 xp
img1=ImageTk.PhotoImage(Image.open("jpg/food1.jpg"))    #   5 xp
img2=ImageTk.PhotoImage(Image.open("jpg/food2.jpg"))    #   6 xp  
img3=ImageTk.PhotoImage(Image.open("jpg/food3.jpg"))    #   5 xp
img4=ImageTk.PhotoImage(Image.open("jpg/food4.jpg"))    #   4 xp
img5=ImageTk.PhotoImage(Image.open("jpg/food5.jpg"))    #   2 xp
img6=ImageTk.PhotoImage(Image.open("jpg/food6.jpg"))    #   5 xp
img7=ImageTk.PhotoImage(Image.open("jpg/food7.jpg"))    #   8 xp
img8=ImageTk.PhotoImage(Image.open("jpg/food8.jpg"))    #   5 xp
img9=ImageTk.PhotoImage(Image.open("jpg/food9.jpg"))    #   6 xp
img10=ImageTk.PhotoImage(Image.open("jpg/food10.jpg"))  #   9 xp
img11=ImageTk.PhotoImage(Image.open("jpg/food11.jpg"))  #   3 xp
img12=ImageTk.PhotoImage(Image.open("jpg/food12.jpg"))  #   5 xp
img13=ImageTk.PhotoImage(Image.open("jpg/food13.jpg"))  #   4 xp
img14=ImageTk.PhotoImage(Image.open("jpg/food14.jpg"))  #   8 xp
img15=ImageTk.PhotoImage(Image.open("jpg/food15.jpg"))  #   3 xp
img16=ImageTk.PhotoImage(Image.open("jpg/food16.jpg"))  #   6 xp
img17=ImageTk.PhotoImage(Image.open("jpg/food17.jpg"))  #   8 xp
#img18=ImageTk.PhotoImage(Image.open("jpg/food18.jpg"))- - - - - - - - - - -# not used :D
img19=ImageTk.PhotoImage(Image.open("jpg/virus1.jpg"))  #   -3 xp   
#img20=ImageTk.PhotoImage(Image.open("jpg/virus2.jpg"))- - - - - - - - - - -# not used :D
img21=ImageTk.PhotoImage(Image.open("jpg/virus3.jpg"))  #   -3 xp 
#img22=ImageTk.PhotoImage(Image.open("jpg/virus4.jpg"))- - - - - - - - - - -# not used :D
img23=ImageTk.PhotoImage(Image.open("jpg/virus6.jpg"))  #   -7 xp  
img24=ImageTk.PhotoImage(Image.open("jpg/virus7.jpg"))  #   -7 xp
img25=ImageTk.PhotoImage(Image.open("jpg/virus8.jpg"))  #   -2 xp
img26=ImageTk.PhotoImage(Image.open("jpg/virus.jpg"))   #   -5 xp
img27=ImageTk.PhotoImage(Image.open("jpg/virus5.jpg"))  #   -4 xp
##########################################################





#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
def play():
    threading.Thread(target=start_s).start() # Game Start 
    homescrene.destroy()       
    star_new()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#




##################################################################   Func

def main_menu():
    threading.Thread(target=ui_click2).start()
    def oke():
        global qut
        qut=True
        global score,health
        score=0
        health=100
        threading.Thread(target=menu_s).start()
        postions.destroy()
        static.destroy()
        home_s()
    def noo():
        frame.destroy()
        mainmenu.config(state="normal")
        threading.Thread(target=ui_click3).start()
    
    frame=LabelFrame(postions,bg="#528B8B",height=150,width=320)
    frame.place(x=184,y=200)
    mainmenu.config(state="disabled")
    sure=Label(frame,text="You will lose your score, Are you sure?",bg="#528B8B")
    sure.place(x=50,y=30)
    ok_button=Button(frame,text=" Ok ",bg="#8B795E",command=oke)
    ok_button.place(x=50,y=100)
    no_button=Button(frame,text="Cancel",bg="#8B795E",command=noo)
    no_button.place(x=220,y=100)

    if dil =="TR":
        ok_button.config(text="Tamam")
        no_button.config(text="Kapat")
        sure.config(text="Puanlarını kaybedeceksin, emin misin?")
    if dil =="AR":
        ok_button.config(text="حسنا")
        no_button.config(text="اغلاق")
        sure.config(text="ستخسر نقاطك ، هل أنت متأكد؟")
        sure.place(x=70,y=30)

def home_s():
    global homescrene,ply,info,exitt,how,bag,lang_button,flag,first_open
    homescrene=Label(root,image=bag)
    homescrene.pack()

    buttonsframe=Frame(homescrene,width=725,height=220,bg="#202529")
    buttonsframe.place(x=2,y=190)
    ply=Button(buttonsframe,text="Play",command=play,bg="#202529",borderwidth=0,activebackground="#78d6ff",font=("Times" ,18),fg="white")
    ply.place(x=335,y=0)
    how=Button(buttonsframe,text="How To Play",command=howto,bg="#202529",borderwidth=0,activebackground="#78d6ff",font=("Times" ,16),fg="white")
    how.place(x=305,y=50)
    info=Button(buttonsframe,text="Info",command=infoo,bg="#202529",borderwidth=0,activebackground="#78d6ff",font=("Times" ,16),fg="white")
    info.place(x=5,y=188)
    exitt=Button(buttonsframe,text="Exit",command=exit,bg="#202529",borderwidth=0,activebackground="#78d6ff",font=("Times" ,16),fg="white")
    exitt.place(x=675,y=188)

    lang_frame=Frame(homescrene,width=80,height=50,bg="#202529")
    lang_frame.place(x=0,y=0)
    lang_button=Button(lang_frame,text="EN",command=set_lang ,bg="#202529",
    borderwidth=0,activebackground="#78d6ff",font=("Times" ,10),fg="white")
    lang_button.place(x=5,y=5)
    flag=Button(lang_frame,image=en,borderwidth=0,bg="#202529",command=set_lang)
    flag.place(x=28,y=8)
    save_lang()




def close_how():
    global in_how_frame
    threading.Thread(target=ui_click3).start()
    in_how_frame=False
    how_frame.destroy()
    hw.destroy()
    clos.destroy()

def howto():
    global how_frame,hw,clos,in_how_frame,flag2,lang_button2,fi
    threading.Thread(target=ui_click2).start()
    how_frame=Label(homescrene,image=how_en,borderwidth=0)
    how_frame.place(x=0,y=0)
    hw=Label(root,width=104,height=2,bg="#202529",borderwidth=0)
    hw.pack()
    clos=Button(hw,text="Close",command=close_how,bg="#202529",borderwidth=0,activebackground="#78d6ff",font=("Times" ,16),fg="white")
    clos.place(x=330,y=1)

    langs_frame=Frame(hw,width=80,height=50,bg="#202529")
    langs_frame.place(x=0,y=0)

    lang_button2=Button(langs_frame,text="EN",command=set_lang ,bg="#202529",borderwidth=0,activebackground="#78d6ff",font=("Times" ,10),fg="white")
    lang_button2.place(x=5,y=5)
    flag2=Button(langs_frame,image=en,borderwidth=0,bg="#202529",command=set_lang)
    flag2.place(x=28,y=8)  

    in_how_frame=True
    if dil=="TR":
        how_frame.config(image=how_tr)
        flag2.config(image=tr)
        lang_button2.config(text=dil)

    elif dil =="AR":
        how_frame.config(image=how_ar)
        lang_button2.config(text=dil)
        flag2.config(image=ar)


def xi():
        sup.destroy()
        info.config(state="normal")
        threading.Thread(target=ui_click3).start()

def exit():
    threading.Thread(target=exit_s).start()
    root.destroy()

def infoo():
    global sup,homescrene
    sup=Frame(root,width=728,heigh=160,bg="#8E8E8E")
    threading.Thread(target=ui_click2).start()
    sup.pack()
    info.config(state="disabled")
    my_text=Label(sup,text="Eat Game By Majed",bg="#8E8E8E",fg="#EEE8AA",font=("Times" ,14))
    my_text.place(x=290,y=42)
    my_text=Label(sup,text="Discord",bg="#8E8E8E",fg="#EEE8AA",font=("Times" ,14))
    my_text.place(x=330,y=80)
    my_text=Label(sup,text="majed#5222",bg="#8E8E8E",fg="#EEE8AA",font=("Times" ,14))
    my_text.place(x=318,y=115)
    cls=Button(sup,text="Close",command=xi,bg="#8DB6CD")
    cls.place(x=0,y=0)



def set_lang():
    global homescrene,ply,info,exitt,how,bag,lang_button,dil
    threading.Thread(target=ui_click).start()
    if dil =="EN":
        dil="TR"
        ply.config(text="Oyna")
        ply.place(x=330,y=0)
        how.config(text="Nasıl Oynanır")
        how.place(x=302,y=50)

        info.config(text="Bilgi")
        exitt.config(text="Çık")

        lang_button.config(text=dil)
        flag.config(image=tr)

        if in_how_frame==True:
            how_frame.config(image=how_tr)
            flag2.config(image=tr)
            lang_button2.config(text=dil)

    elif dil=="TR":
        dil="AR"
        ply.config(text="العب",font=("Times" ,18),fg="white")
        ply.place(x=333,y=0)
        how.config(text="كيفية اللعب",font=("Times" ,18),fg="white")
        how.place(x=307,y=50)
        info.config(text="معلومات")
        exitt.config(text="خروج")
        exitt.place(x=670,y=188)
        lang_button.config(text=dil)
        flag.config(image=ar)
        if in_how_frame==True:
            how_frame.config(image=how_ar)
            flag2.config(image=ar)
            lang_button2.config(text=dil)

    elif dil=="AR":
        dil="EN"
        ply.config(text="Play",font=("Times" ,18),fg="white")
        ply.place(x=335,y=0)
        how.config(text="How To Play",font=("Times" ,16),fg="white")
        how.place(x=305,y=50)
        info.config(text="Info",font=("Times" ,16),fg="white")
        exitt.config(text="Exit",font=("Times" ,16),fg="white")
        lang_button.config(text=dil)
        flag.config(image=en)
        if in_how_frame==True:
            how_frame.config(image=how_en)
            flag2.config(image=en)
            lang_button2.config(text=dil)







def save_lang():
    global homescrene,ply,info,exitt,how,bag,lang_button,dil
    if dil =="TR":
        ply.config(text="Oyna")
        ply.place(x=330,y=0)
        how.config(text="Nasıl Oynanır")
        how.place(x=302,y=50)
        info.config(text="Bilgi")
        exitt.config(text="Çık")
        lang_button.config(text=dil)
        flag.config(image=tr)
        if in_how_frame==True:
            how_frame.config(image=how_tr)
            flag2.config(image=tr)
            lang_button2.config(text=dil)

    elif dil=="AR":
        ply.config(text="العب",font=("Times" ,18),fg="white")
        ply.place(x=333,y=0)
        how.config(text="كيفية اللعب",font=("Times" ,18),fg="white")
        how.place(x=307,y=50)
        info.config(text="معلومات")
        exitt.config(text="خروج")
        exitt.place(x=670,y=188)
        lang_button.config(text=dil)
        flag.config(image=ar)
        if in_how_frame==True:
            how_frame.config(image=how_ar)
            flag2.config(image=ar)
            lang_button2.config(text=dil)

home_s()
##################################################################   




#######################################      Sound 

def eat_sound():
    s=random.randint(1,5)
    if s==1:
        playsound('sound/eat1.mp3')
    elif s==2:
        playsound('sound/eat2.mp3')
    elif s==3:
        playsound('sound/eat3.mp3')
    elif s==4:
        playsound('sound/eat4.mp3')
    elif s==5:
        playsound('sound/eat5.mp3')

def Count_down():
    playsound('sound/cc.wav')
def die():
    playsound('sound/die.wav')
def Virus():
    playsound('sound/viruseat.mp3')
def ui_click():
    playsound('sound/click.wav')
def ui_click2():
    playsound('sound/click2.wav')
def ui_click3():
    playsound('sound/click3.mp3')
def start_s():
    playsound('sound/start.mp3')
def exit_s():
    playsound('sound/exit.mp3')
def menu_s():
    playsound('sound/menu.wav')
#######################################

liste=[img,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,
img14,img15,img16,img17,img19,img23,img24,img25,img26,img27,img21]

foodlist=[img,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,
img14,img15,img16,img17]

viruslist=[img19,img23,img24,img25,img26,img27,img21]

############################################################################ Game logic

def set_timer(rand):
    global Timer
    if score>=200:
        Timer=0.7
    if score>=500:
        Timer=0.6
    if score>=900:
        Timer=0.5
    if score>=1300:
        Timer=0.4

    
def dmage():  
    global health,h_bar,dead,start_bleed,bleed
    star_bleed=True
    
    if bleed==True:
        star_bleed=False
    
    if (star_bleed==True):
        bleed=True
        print("bledding")
        while (health != 0):
            if bleed==False:
                break
            h_bar.destroy()
            health-=1
            h_bar=Label(static,bg="green",width=health,height=1,text="Health")
            if health<50:
                h_bar.config(bg="gold")
            if health<25:
                h_bar.config(bg="red")
            h_bar.place(x=10,y=60)
            time.sleep(0.2)
   
        
    
        
    if dil=="TR":
        h_bar.config(text="Sağlık")
        
    elif dil=="AR":
         h_bar.config(text="صحة")
         
   
    if health <1:
        dead=True
        static.destroy()
        fl=open("scoredata.txt","a")
        fl.write(f"{score}\n")
        fl.close()
        from  scores import max_sc

        threading.Thread(target=die).start()
        h_bar.destroy()
        deathnote=LabelFrame(postions,borderwidth=0,bg="#DEB887",width=685,height=505)
        deathnote.place(x=0,y=0)
        tex=Label(deathnote,text="GAME OVER",font=("BLOD",22),bg="#DEB887")
        tex.place(x=270,y=150)
        tex1=Label(deathnote,text="Score:"+str(score),font=("BLOD",22),bg="#DEB887")
        tex1.place(x=185,y=255)
        tex2=Label(deathnote,text="High Score:"+str(max_sc),font=("BLOD",22),bg="#DEB887")
        tex2.place(x=385,y=255)

def command_passer():
    pass



def bandge(coll):
    
    global static,bandge_lab,bandge_part,bleed
    if  coll=="Virus":
        bandge_lab.destroy()
        if bandge_part>15:
            bandge_part-=20
    if coll=="Food":
        bandge_lab.destroy()
        bandge_part+=20
    if coll=="Start":
        bandge_part+=15

    if bandge_part>=95:
        bandge_part=0
        bleed=False

    bandge_lab=Label(static,text="Bandge parts",width=bandge_part,height=1,bg='Darkgreen')
    bandge_lab.place(x=10,y=37)
   


def add_score():
    global score,hit,health
    if rmg in viruslist:
        if (bleed):
            bandge("Virus")
        threading.Thread(target=Virus).start()
        threading.Thread(target=dmage).start()
       
    elif rmg in foodlist:
        threading.Thread(target=eat_sound).start()
        if rmg ==img:
            if (bleed):
                health+=10
                bandge("Food")
            score+=30
        elif rmg==img1:
            if (bleed):
                health+=10
                bandge("Food")
            score+=50
        elif rmg==img2:
            if (bleed):
                health+=10
                bandge("Food")
            score+=60
        elif rmg==img3:
            if (bleed):
                health+=10
                bandge("Food")
            score+=50
        elif rmg==img4:
            if (bleed):
                health+=10
                bandge("Food")
            score+=40
        elif rmg==img5:
            if (bleed):
                health+=10
                bandge("Food")
            score+=20
        elif rmg==img6:
            if (bleed):
                health+=10
                bandge("Food")
            score+=50
        elif rmg==img7:
            if (bleed):
                health+=10
                bandge("Food")
            score+=80
        elif rmg==img8:
            if (bleed):
                health+=10
                bandge("Food")
            score+=50
        elif rmg==img9:
            if (bleed):
                health+=10
                bandge("Food")
            score+=60
        elif rmg==img10:
            if (bleed):
                health+=10
                bandge("Food")
            score+=90
        elif rmg==img11:
            if (bleed):
                health+=10
                bandge("Food")
            score+=30
        elif rmg==img12:
            if (bleed):
                health+=10
                bandge("Food")
            score+=50
        elif rmg==img13:
            if (bleed):
                health+=10
                bandge("Food")
            score+=40
        elif rmg==img14:
            if (bleed):
                health+=10
                bandge("Food")
            score+=80
        elif rmg==img15:
            if (bleed):
                health+=10
                bandge("Food")
            score+=30
        elif rmg==img16:
            if (bleed):
                health+=10
                bandge("Food")
            score+=60
        elif rmg==img17:
            if (bleed):
                health+=10
                bandge("Food")
            score+=80
        
    hit=True
    if dead !=True: 
        scc=Label(static,text="Score:"+str(score),bg="#A9A9A9",font=("BLOD",12))
        scc.place(x=10,y=5)
    if dil=="TR":
        scc.config(text="Puan:"+str(score))
    elif dil=="AR":
        scc.config(text="نقاط:"+str(score))   
    if x==1:
        pos1.config(bg="#4A4A4A",command=command_passer)
    elif x==2:
        pos2.config(bg="#4A4A4A",command=command_passer)
    elif x==3:
        pos3.config(bg="#4A4A4A",command=command_passer)
    elif x==4:
        pos4.config(bg="#4A4A4A",command=command_passer)
    elif x==5:
        pos5.config(bg="#4A4A4A",command=command_passer)
    elif x==6:
        pos6.config(bg="#4A4A4A",command=command_passer)     
    elif x==7:
        pos7.config(bg="#4A4A4A",command=command_passer)
    elif x==8:
        pos8.config(bg="#4A4A4A",command=command_passer)
    elif x==9:
        pos9.config(bg="#4A4A4A",command=command_passer)
    elif x==10:
        pos10.config(bg="#4A4A4A",command=command_passer)
    elif x==11:
        pos11.config(bg="#4A4A4A",command=command_passer)
    elif x==12:
        pos12.config(bg="#4A4A4A",command=command_passer)
    
    
def star_new():
    global pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11,pos12,test,scc,h_bar,static,postions,mainmenu,qut
    qut=False
    postions=LabelFrame(root,width=690,height=510,bg="#A9A9A9")
    postions.pack()
    static=LabelFrame(root,width=690,height=100,bg="#A9A9A9")
    static.pack()
    pos1=Button(postions,bg="#4A4A4A",image=imga)
    pos1.place(x=25,y=20)
    pos2=Button(postions,bg="#4A4A4A",image=imga)
    pos2.place(x=185,y=20)
    pos3=Button(postions,bg="#4A4A4A",image=imga)
    pos3.place(x=345,y=20)
    pos4=Button(postions,bg="#4A4A4A",image=imga)
    pos4.place(x=505,y=20)

    pos5=Button(postions,bg="#4A4A4A",image=imga)
    pos5.place(x=25,y=180)
    pos6=Button(postions,bg="#4A4A4A",image=imga)
    pos6.place(x=185,y=180)
    pos7=Button(postions,bg="#4A4A4A",image=imga)
    pos7.place(x=345,y=180)
    pos8=Button(postions,bg="#4A4A4A",image=imga)
    pos8.place(x=505,y=180)

    pos9=Button(postions,bg="#4A4A4A",image=imga)
    pos9.place(x=25,y=340)
    pos10=Button(postions,bg="#4A4A4A",image=imga)
    pos10.place(x=185,y=340)
    pos11=Button(postions,bg="#4A4A4A",image=imga)
    pos11.place(x=345,y=340)
    pos12=Button(postions,bg="#4A4A4A",image=imga)
    pos12.place(x=505,y=340)

    test=Button(static,text="Start",command=lambda:threading.Thread(target=counddown).start(),bg="#458B74",font=("BLOD",12))
    test.place(x=315,y=5)
    scc=Label(static,text="Score:"+str(score),bg="#A9A9A9",font=("BLOD",12))
    scc.place(x=10,y=5)
    h_bar=Label(static,bg="green",width=health,height=1,text="Health")
    h_bar.place(x=10,y=60)
    mainmenu=Button(static,text="Menu",command=lambda:threading.Thread(target=main_menu).start(),bg="#458B74",font=("BLOD",10))
    mainmenu.place(x=635,y=8)
    bandge("Start")
    if dil=="TR":
        test.config(text="Başla")
        scc.config(text="Puan:"+str(score))
        h_bar.config(text="Sağlık")
        mainmenu.config(text="Menü")
    elif dil=="AR":
        test.config(text="أبـدا",font=("BLOD",12))
        scc.config(text="نقاط:"+str(score),font=("BLOD",12))
        h_bar.config(text="صحة",font=("BLOD",9))
        mainmenu.config(text="القائمة",font=("BLOD",10))

        
    



def counddown():
    threading.Thread(target=Count_down).start()
    test.destroy()

    tre=Label(static,text=" 3",fg="black",bg="#A9A9A9",font=("BLOD",16))
    tre.place(x=326,y=8)
    time.sleep(1)
    tre.destroy()

    to=Label(static,text=" 2",fg="black",bg="#A9A9A9",font=("BLOD",16))
    to.place(x=326,y=8)
    time.sleep(1)
    to.destroy()

    one=Label(static,text=" 1",fg="black",bg="#A9A9A9",font=("BLOD",16))
    one.place(x=326,y=8)
    time.sleep(1)
    one.destroy()

    go=Label(static,text="Go",fg="green",bg="#A9A9A9",font=("BLOD",16))
    go.place(x=326,y=8)
    time.sleep(1)
    go.destroy()

    threading.Thread(target=random_chi).start()

    
def random_chi():
    global x ,rmg,virus_count,food_count
    
    rmg=random.choice(liste)
    x=random.randint(1,12)
    
    if rmg in foodlist:
        print('food')
        food_count+=1

    elif rmg in viruslist:
        print('virus')
        virus_count+=1
    
   # print("Virus",virus_count,"Food",food_count)

    if food_count>=4:
      #  print("exuceted")
        rmg=random.choice(viruslist)
        food_count=0

    if virus_count>=2:
       # print("exuceted")
        rmg=random.choice(foodlist)
        food_count=0
        virus_count=0

    if qut!=True:
        open_chi(x)

def open_chi(x):

    global hit
    hit=False
    print(Timer)
    if x==1:
        pos1.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos1.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==2 and qut==False:
        pos2.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos2.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==3 and qut==False:
        pos3.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos3.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==4 and qut==False:
        pos4.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos4.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==5 and qut==False:
        pos5.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos5.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==6 and qut==False:
        pos6.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos6.config(bg="#4A4A4A",image=imga,command=command_passer)     
    elif  x==7 and qut==False:
        pos7.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos7.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==8 and qut==False:
        pos8.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos8.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==9 and qut==False:
        pos9.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos9.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==10 and qut==False:
        pos10.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos10.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==11 and qut==False:
        pos11.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos11.config(bg="#4A4A4A",image=imga,command=command_passer)
    elif  x==12 and qut==False:
        pos12.config(bg="#4A4A4A",state="normal",command=lambda:add_score(),image=rmg)
        time.sleep(Timer)
        pos12.config(bg="#4A4A4A",image=imga,command=command_passer)



    time.sleep(2)
    if dead!=True:
        threading.Thread(target=random_chi).start()




root.mainloop()
