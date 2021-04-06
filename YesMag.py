from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

identifiant = ""
mdp = ""
temps = ""
driver = webdriver.Chrome(executable_path="chromedriver.exe")
FirstPass = True
def BTretour():
    try:
        retour = driver.find_element_by_xpath(
            "/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reader/ion-header/ion-navbar/button")
        retour.click()
        print("[RETOUR]")
    except:
        try:
            retour = driver.find_element_by_xpath(
                "/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-video/ion-header/ion-navbar/button")
            retour.click()
            print("[RETOUR]")
        except:
            pass
        pass



def BTLu():
    target = driver.find_element_by_xpath(
        "/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reader/ion-content/div[2]/div/div/button[1]")
    target.click()
    print("[LU]")

def connexion(pidentifiant, pmdp):
    sleep(3)
    login = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-login/ion-content/div[2]/div[1]/ion-list/ion-item[1]/div[1]/div/ion-input/input")
    login.send_keys(pidentifiant)
    print("[ID]")
    mdp = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-login/ion-content/div[2]/div[1]/ion-list/ion-item[2]/div[1]/div/ion-input/input")
    mdp.send_keys(pmdp)
    print("[MDP]")
    sleep(1)
    submit = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-login/ion-content/div[2]/div[1]/button[1]")
    submit.click()
    print("[CONNEXION]")
    sleep(1)

def choisirarticle():
    global FirstPass
    col = driver.find_elements_by_class_name("col")
    cards = []
    for i in col:
        cards.append(i)
    #print(cards)
    #print(len(cards))
    toread = cards[random.randint(1, 39)]
    toread.click()
    print("[ARTICLE CHOISI]")
    sleep(4)
    try:
        jaicompris = driver.find_element_by_xpath(
            "/html/body/ion-app/ion-modal/div/page-article-help/ion-header/ion-navbar/div[2]/ion-buttons/button")
        jaicompris.click()
    except:
        #print("error")
        if FirstPass == True:
            BTretour()
        pass
    try:
        jaicompris = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-video-help/ion-header/ion-navbar/div[2]/ion-buttons/button")
        jaicompris.click()
    except:
        pass

    sleep(5)

def lecture():
    n = 0
    print("Lecture en cours...")
    while True:
        n = n + 1
        try:
            texts = "/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reader/ion-content/div[2]/div/div/p/span[" + str(
                n) + "]"
            target = driver.find_element_by_xpath(texts)
            target.location_once_scrolled_into_view
            if random.randint(1, 16) == 3:
                try:
                    target.click()
                    print("[VERIFICATION VOC]")
                    sleep(5)
                    target.click()#test
                except:
                    pass
                try:
                    ok = driver.find_element_by_xpath("/html/body/ion-app/ion-toast/div/div/button")
                    ok.click()
                except:
                    pass
            sleep(15)
        except:
            try:
                texts = "/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-reader/ion-content/div[2]/div/div/p/span[" + str(
                    n - 3) + "]"
                target = driver.find_element_by_xpath(texts)
                target.click()
                sleep(5)
                target.click()
            except:
                pass
            break
    sleep(1)
    #BTLu()
    sleep(1)
    BTretour()
    sleep(1)

def ChangePage():
    home = driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-menu/div/ion-content/div[2]/ion-list/button[1]")
    home.click()
    print("[RETOUR ACCEUIL]")
    sleep(1)
    try:
        page = driver.find_element_by_xpath(
            "/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-header/ion-navbar/ion-buttons/button")
        page.click()
    except:
        pass
    for i in range(random.randint(1, 45)):
        page = driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-home/ion-header/ion-navbar/ion-buttons/button[2]")
        page.click()
        sleep(0.5)
    sleep(1)

def Statistiques():
    try:
        buttonStat = driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-menu/div/ion-content/div[2]/ion-list/button[4]")
        buttonStat.click()
    except:
        driver.refresh()
        buttonStat = driver.find_element_by_xpath(
            "/html/body/ion-app/ng-component/ion-split-pane/ion-menu/div/ion-content/div[2]/ion-list/button[4]")
        buttonStat.click()
    print("[CHECK STATISTIQUES]")
    sleep(1)
    Avriltime = driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-stats/ion-content/div[2]/ion-list[2]/ion-item[1]/div[1]/div/ion-label/strong")
    Avriltime = Avriltime.text
    print("Temps actualisé: ", Avriltime)
    return Avriltime

def main():
    global FirstPass
    global identifiant
    global mdp
    global temps
    window.destroy()
    driver.get("https://yesmag.fr/webapp/")
    connexion(identifiant, mdp)
    vTime = ""
    while str(temps) not in str(vTime):
        vTime = Statistiques()
        ChangePage()
        choisirarticle()
        lecture()
        FirstPass = False
    print("FIN: Vous avez passé ", vTime, " sur Yesmag.")
    driver.close()


window = Tk()

window.title("YesMag Counter :)")

window.geometry('370x150')

lbl1 = Label(window, text="Identifiant: ")

lbl1.grid(column=0, row=0)

txt1 = Entry(window, width=30)

txt1.grid(column=1, row=0)

lbl2 = Label(window, text="Mot de passe: ")

lbl2.grid(column=0, row=2)

txt2 = Entry(window, width=30)

txt2.grid(column=1, row=2)

lbl3 = Label(window, text="Temps ? (h/min)")

lbl3.grid(column=0, row=3)

s1 = Spinbox(window, from_=0, to=10, width=3)
s1.grid(column=1, row=3)

s2 = Spinbox(window, from_=0, to=9, width=3)
s2.grid(column=1, row=4)

lbl3 = Label(window, text="")

lbl3.grid(column=1, row=5)

lbl4 = Label(window, text="")

lbl4.grid(column=3, row=6)

def clickedID():
    global identifiant
    identifiant = str(txt1.get())
    print("identifiant: ", identifiant)

def clickedMP():
    global mdp
    mdp = str(txt2.get())
    print("mot de passe: ", mdp)

def setHeure():
    global temps
    minute = str(s2.get())
    if minute == "0":
       minute = ""
    temps = str(s1.get())+"h"+minute
    #print(s1.get())
    #print(minute)
    print("temps désiré: ", temps)

btn1 = Button(window, text="Valider", command=clickedID)

btn1.grid(column=2, row=0)

btn2 = Button(window, text="Valider", command=clickedMP)

btn2.grid(column=2, row=2)

btn3 = Button(window, text="LIRE YESMAG !", command=main)#main

btn3.grid(column=1, row=6)

btn4 = Button(window, text="Valider temps", command=setHeure)

btn4.grid(column=2, row=4)

window.mainloop()
