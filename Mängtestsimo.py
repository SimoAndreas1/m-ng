#Mäng
#Simo ja Aksel
#28.04.2022

import random

#Mängus vajalikud muutujad


#MENÜÜ#

print()
print("Kalev")
print()
print()
print("Mängu loojad: Simo ja Aksel")
print()
print()
algus = int(input("[1] Mängi [2] Välju Mängust"))
print()
if algus == 2:
    exit()
    
elif algus == 1:
    save_name = input("Nimetage enda save-i")
elif algus == 2:
    exit()
#Loo kontekst
print()
print(f"Sa alustad põllumaal peale suurt pidupäeva. \nSa mõistad midagi on mäda, kõik mis su ümber on tundub veider. \nIgal pool on maha lagunenud või lagunemas majad, maha jäätud vagunid. \nLiikudes edasi sa näed grupp inimesi võitlemas trollide ja mutantidega. \nSa näed kuidas kõik inimese surevad igalpool, sa otsustad asja enda kätte võtta, et mõista mis sinu kodumaaga juhtus.")
print()
#Lugu jätkab.
print("Osa I.")
print("Sa kõndisid kohalikku külla, sa nägid kuidas seinad olid igalepoole ümber ehitatud. Sinuga hakkas rääkima valvur.")
print("Valvur: Kes sa oled? Mis põhjusega sa siia tulid? Kellega sa oled?")
print("Mängija: Ma olen talunik. Ma tulin vastuseid otsima, et mis siin toimub. Igal pool on rüüstatud majad ja surnud inimesed. Mis siin toimub?")
print("Valvur: Metsa koobas avati ja välja jooksid trollid ja mutandid. Kas sa nägid neid?")
print("Mängija: Jah. Ründasid kamp kohalikke külast väljaspool. Tapsid nad ära nagu metslased.")
print("Valvur: Selge. Mis su nimi on?")
print("Mängija: Minu nimi on Kalev.")
print("Valvur: Olgu. Ma lasen su sisse. Sa pead küla sõduriks hakkama.")
print("Kalev: Sobib.")
print("Sulle anti relv ja kaitse: Mõõk ja Kilp")
print("Avatud Kalevil: statistika")

#Stats#
health = 100 #Elud
XP = 10 #XP on skoor kasutatud mängus. Mängu lõpus näed palju said.
attack = 1 
defense = 0
protsent = 30
level = 0

#Lugu jätkab.
print("Osa II:")
print("Kalev: Kus see koobas üldse on?")
print("Valvur: külast ida poole. Parem on sinna minna öösel, kui kõik trollid ja need teised olevused on kohal. Lihtsam nad kõik kohe maha võtta.")
print("Kalev: Selge. Lähme siis öösel.")
print("Öö ootamine...")
print("Valvur: nonii suur mees, aja end ülesse. Meie sõdurid on valmis minema.")
print("Kalev: Olgu. Lähme")
print()
print("Koopa otsimine...")
print()
print("Valvur: Noh, näed midagi?")
print("Kalev: Jah, näen küll. Seal pool.")
print()
print("Te sisenesite koopasse.")
print()
print("Suvaline Troll: MIDA TE INIMESED MEIE KOOPAS TEETE?!?!?! RÜNNATA!!!!!!!")
#Algab combat
def valikud():
    print(f'[1] Ründa vastast. (Kahju korrutaja {attack}%)')
    print(f'[2] Bloki ({protsent}% tõenäosus). ')
    print('[3] Ravi end 10 elu võrra.')
    
    valik = int(input('vali enda tegevus: '))
    return valik

#Funktsioon võitluse jaoks.

def kaklus (enemy_health, enemy_XP, enemy_attack, xp_attack, xp_defense):
    global health
    global XP
    global attack
    global defense
    global relv
    global mook_dmg
    global protsent
    
    while enemy_health >= 1 and health >= 1:
        valik = valikud()
        
        dmg = random.randint(5,10) # Kahjustus mida teed vastasele.
        booster = dmg*attack
        enemy_dmg = random.randint(3,10) # Kahjustus mida tehakse sulle.
        enemy_dmg = enemy_dmg
        
        print()
        
        if valik == 1:
            if dmg >= 12:
                enemy_health -= dmg
                health -= enemy_dmg
                print(
