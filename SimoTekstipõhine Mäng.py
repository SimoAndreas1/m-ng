# Tekstipõhine Mäng
# Simo Andreas Novikov
# IT-21

# moodulid
import random

# statistika
elud = 100 # Sinu elud, kui elud otsa saavad ss oled kutu :(
dmg = random.randint(20, 50) # summa vigastus mis sa vaenlasele tekitad
xp = 0 # puntkid, mida saad näha mängu lõpus, pole oluline aga las olla
lvl = 0 # su tase
velud = 100 # vaenlase elud
vdmg = random.randint(10, 30) # kahju mida vaenlane tekitab sinule

# menüü
print('Kalevipoja Seiklused')
print()
print('Loo kirjutamine ja Programmeerimine: Simo Andreas Novikov')
print()
algus = int(input('(1) Start (2) Lahku '))
print()

# võitluse funktsioon
def Voitlus(velud, elud):
    global algus
    while elud >= 0 and velud >= 0:
        velud -= dmg
        elud -= vdmg
        print()
        print(f'tegid {dmg} kahju')
        print()
        print(f'vaenlane tegi {vdmg} kahju')
        print()
        print(f'sinu elud: {elud}')
        print(f'vaenlase elud: {velud}')
    
    if velud <= 0:
        print()
        print('VÕIT!')
        print()
        print('GAME OVER')
        algus = 2
    else:
        print()
        print('Said Surma...')
        algus = 2

# nime valik
if algus == 1:
    kn = input('nimi: ')
    while algus == 1:
        print(algus)
        Voitlus(elud, velud)
elif algus == 2:
    exit()

print(f'Tere, {kn}! sa oled sattunud neetud maailma, kus deemonid on maailma üle võtnud. Sinu eesmärk on neile lõpp panna. Edu!')
print()

# mäng
while elud >= 0:
    print('lvl 1: Vihane Deemon')
    print()
    print('Deemon: Kuidas sa julged minu koopasse tulla. Ma nõuan võitlust!')
    print()
    print('kalevipoeg: Olgu, kui muud valikut ei ole.')
    Voitlus(elud, velud)
    break