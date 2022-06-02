#Mäng
#Simo Andreas Novikov
#28.04.2022

import random

#Mängus vajalikud muutujad


#MENÜÜ#

print()
print("Kalev")
print()
print()
print("Mängu looja: Simo Andreas Novikov")
print()
print()
algus = int(input("[1] Mängi [2] Välju Mängust"))
print()
if algus == 2:
    exit()
    
elif algus == 1:
    user_name = input("Nimetage ennast. (Näiteks: Kalev): ")
elif algus == 2:
    exit()
#Loo kontekst
print()
print("Sa alustad põllumaal peale suurt pidupäeva. \nSa mõistad midagi on mäda, kõik mis su ümber on tundub veider. \nIgal pool on maha lagunenud või lagunemas majad, maha jäätud vagunid. \nLiikudes edasi sa näed grupp inimesi võitlemas trollide ja mutantidega. \nSa näed kuidas kõik inimese surevad igalpool, sa otsustad asja enda kätte võtta, et mõista mis sinu kodumaaga juhtus.")
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
attack = 1 #viga tekitus
defense = 0 #kaitse
protsent = 30 #võimalus
level = 0 #tase

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
print("Te sisenesite koopasse.")
print()
print("Suvaline Troll: MIDA TE INIMESED MEIE KOOPAS TEETE?!?!?! RÜNNATA!!!!!!!")
print()
#Algab combat
def valikud():
    print(f'[1] Ründa vastast. (Kahju korrutaja {attack}%)')
    print(f'[2] Bloki ({protsent}% tõenäosus). ')
    print('[3] Ravi end 10 elu võrra.')
    
    valik = int(input('vali enda tegevus: '))
    return valik

#Funktsioon võitluse jaoks.

def kaklus(enemy_health, enemy_XP, enemy_dmg, exp_attack, exp_defense):
    global health
    global XP
    global attack
    global defense
    global protsent
    
    while enemy_health >= 1 and health >= 1:
        valik = valikud()
        
        dmg = random.randint(5,10) # Kahjustus mida teed vastasele.
        enemy_dmg = random.randint(3,10) # Kahjustus mida tehakse sulle.
        enemy_dmg = enemy_dmg
        
        print()
        
        if valik == 1:
            if dmg >= 12:
                enemy_health -= dmg
                health -= enemy_dmg
                print(f'Kriitiline löök. Tegid {dmg} kahju')
                print(f'Vastane tekitas sulle {enemy_dmg} kahju.')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {enemy_health}')
                print('─────────────────────────────────────')
                
            elif dmg in range(7,11):
                enemy_health -= dmg
                health -= enemy_dmg
                print(f'Täitsa hea löök. Kahjustasid teda {dmg} võrra!')
                print(f'Aisa raisk! Vastane tekitas sulle {enemy_dmg} kahju.')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {enemy_health}')
                print('─────────────────────────────────────')
                
            else:
                enemy_health -= dmg
                health -= enemy_dmg
                print(f'Ei olnud hea löök... Tegid {dmg} kahju')
                print(f'Aiaiai. Vastane tegi sulle {enemy_dmg} kahju')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {enemy_health}')
                print('─────────────────────────────────────')
                
        elif valik == 2:
            if random.randint(0,100) > protsent:
                health -= enemy_dmg
                print(f'OW! Vastane tegi sulle {enemy_dmg}.')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {enemy_health}')
                print('─────────────────────────────────────')
                    
            else:
                blokk = random.randint(1,3)
                enemy_health -= blokk
                print(f'Blokiga tegid {blokk} kahju.')
                print('YESS! Blokk õnnestus!')
                print(f'Sinu elud: {health}')
                print(f'Vastase elud: {enemy_health}')
                print('─────────────────────────────────────')
                    
        else:
            health += 10
            enemy_dmg = random.randint(1,10)
            health -= enemy_dmg
            print(f'AI! Vastane tegi sulle {enemy_dmg} kahju.')
            print(f'Sinu elud: {health}')
            print('─────────────────────────────────────')        
    if enemy_health <= 0:
        print(f'HÄSTI TEHTUD {user_name}!!!')
        XP += enemy_XP
        enemy_XP -= enemy_XP
        attack += exp_attack
        defense += exp_defense
        protsent += defense
                
    else:
        print('ISSAND KUI PASK SA OLED! SA JU SURID!!!')
        print('GAME OVER!')
        exit()
                
if level == 0:
    print('ESIMENE TASE')
    print('─────────────────────────────────────')
    print('Sa liigud mööda koobast edasi otsides põhjust kõigele mis viimasel ajal toimunud on.')
    print("Suvaline Troll: MIDA TE INIMESED MEIE KOOPAS TEETE?!?!?! RÜNNATA!!!!!!!")
    print()
    print('Võitlus algab vastasega. \nMida soovid teha?')
    print()
        
        
    kaklus(50, random.randint(7,10), 1, 0.05, 1)
    print('Õnnestus! Sa tapsid selle rõveda trolli ära! Su retk jätkab.')
    print()
    print('+0.05 ATTACK')
    print('+1% DEFENSE')
    level += 1
    print()
        
        
if level == 1:
    print('JÄRGMINE TASE')
    print('─────────────────────────────────────')
    print(f'Läbisid päris pika tee siin koopas. Lausa {random.randint(50,150)} meetrit')
    print('Valvur: Kuule! Siin on kaks poolt kuhu minna. Lähme äkki paremale poole. Vaatame mis see meile annab.')
    print('Kalev: Olgu.')
    print('Hiiglaslik Troll: KUIDAS SA KURAT SIIA SAID! KAS MU SÕDURID TEILE MAATASA EI TEINUD?')
    print('Kalev: Nägu näha, ei.')
    print('Hiiglaslik Troll: SIIS MA PEAN SEDA ISE TEGEMA!!!')
    print()
        
    kaklus(60, random.randint(10,15), 1.5, 0.03, 2)
        
    print('ÕNNESTUS! Sa panid maha Troll bossi! Ta on veel elus, et enda viimased sõnad sulle avaldada.')
    print('Kalev: Nonii. Mille pärast sina ja sinu trollid meie maal on?')
    print('Hiiglaslik troll: Sest te kuradi inimesed olete liiga lollid, et seda maailmat juhtida!')
    print('Kalev: Nagu näha. Ilmselt mitte. Aeg sulle lõpu peale teha.')
    print('Hiiglaslik Troll: EIII!!!!')
    print('Valvur: Nojah. Nii palju sellest. Maailm saab olla nüüd normaalne.')
    print('Kalev: Ma nüüd lähen teen enda talu korda. Nägemiseni.')
        
        
        
    print()
    print("--------------------")
    print("MÄNG LÄBI!")
    print("--------------------")
    print(f'SKOOR: {XP}')
    print("--------------------")
    print()
    print("Koostaja: Simo Andreas Novikov")
    print()