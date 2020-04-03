# for TFT set 3 10.7
elements = ['Celestial','Chrono','Cybernetic','Dark_Star','Mech_Pilot','Rebel',#5
    'Space_Pirate','Star_Guardian','Valkyrie','Void','Blademaster','Blaster',#11
    'Brawler','Demolitionist','Infiltrator','Mana_Reaver','Mercenary','Mystic',#17
    'Protector','Sniper','Sorcerer','Starship','Vanguard']#22
champ_state_info = dict(
    zoe=dict(name='Zoe',cost=1,elem=[7,20]),
    ziggs=dict(name='Ziggs',cost=1,elem=[5,13]),
    xayah=dict(name='Xayah',cost=1,elem=[0,10]),
    twistedFate=dict(name='TwistedFate',cost=1,elem=[1,20]),
    poppy=dict(name='Poppy',cost=1,elem=[7,22]),
    malphite=dict(name='Malphite',cost=1,elem=[5,12]),
    leona=dict(name='Leona',cost=1,elem=[2,22]),
    khazix=dict(name='Khazix',cost=1,elem=[9,14]),
    jarvan_iv=dict(name='Jarvan IV',cost=1,elem=[3,18]),
    graves=dict(name='Graves',cost=1,elem=[6,11]),
    fiora=dict(name='Fiora',cost=1,elem=[2,10]),
    caitlyn=dict(name='Caitlyn',cost=1,elem=[1,19]),
    yasuo=dict(name='Yasuo',cost=2,elem=[5,10]),
    xin_zhao=dict(name='Xin_zhao',cost=1,elem=[0,18]),
    sona=dict(name='Sona',cost=2,elem=[5,17]),
    shen=dict(name='Shen',cost=2,elem=[1,9]),
    rakan=dict(name='Rakan',cost=2,elem=[0,18]),
    mordekaiser=dict(name='Mordekaiser',cost=2,elem=[3,22]),
    lucian=dict(name='Lucian',cost=2,elem=[2,11]),
    kaisa=dict(name='Kaisa',cost=2,elem=[9,14]),
    darius=dict(name='Darius',cost=2,elem=[6,15]),
    blitzcrank=dict(name='Blitzcrank',cost=2,elem=[1,12]),
    annie=dict(name='Annie',cost=2,elem=[4,20]),
    ahri=dict(name='Ahri',cost=2,elem=[7,20]),
    vi=dict(name='Vi',cost=3,elem=[2,12]),
    syndra=dict(name='Syndra',cost=3,elem=[7,20]),
    shaco=dict(name='Shaco',cost=3,elem=[3,14]),
    rumble=dict(name='Rumble',cost=3,elem=[4,13]),
    neeko=dict(name='Neeko',cost=3,elem=[7,18]),
    master_yi=dict(name='Master_yi',cost=3,elem=[5,10]),
    lux=dict(name='Lux',cost=3,elem=[3,20]),
    kassadin=dict(name='Kassadin',cost=3,elem=[0,15]),
    karma=dict(name='Karma',cost=3,elem=[3,17]),
    jayce=dict(name='Jayce',cost=3,elem=[6,22]),
    ezreal=dict(name='Ezreal',cost=3,elem=[1,11]),
    ashe=dict(name='Ashe',cost=3,elem=[1,19]),
    wukong=dict(name='Wukong',cost=4,elem=[1,22]),
    velkoz=dict(name='Velkoz',cost=4,elem=[9,20]),
    soraka=dict(name='Soraka',cost=4,elem=[7,17]),
    kayle=dict(name='Kayle',cost=4,elem=[8,10]),
    jinx=dict(name='Jinx',cost=4,elem=[5,11]),
    jhin=dict(name='Jhin',cost=4,elem=[3,19]),
    irelia=dict(name='Irelia',cost=4,elem=[2,10,15]),
    fizz=dict(name='Fizz',cost=4,elem=[4,14]),
    chogath=dict(name='Chogath',cost=4,elem=[9,12]),
    thresh=dict(name='Thresh',cost=5,elem=[1,15]),
    miss_fortune=dict(name='Miss_Fortune',cost=5,elem=[8,11,16]),
    lulu=dict(name='Lulu',cost=5,elem=[0,17]),
    gangplank=dict(name='Gangplank',cost=5,elem=[6,13,16]),
    ekko=dict(name='Ekko',cost=5,elem=[2,14]),
    aurelion_sol=dict(name='Aurelion_Sol',cost=5,elem=[5,21]),
    )
champ_cost_info = dict(
    c1=['zoe','ziggs','xayah','twistedFate','poppy','malphite',
        'leona','khazix','jarvan_iv','graves','fiora','caitlyn'],
    c2=['yasuo','xin_zhao','sona','shen','rakan','mordekaiser','lucian',
        'kaisa','darius','blitzcrank','annie','ahri'],
    c3=['vi','syndra','shaco','rumble','neeko','master_yi','lux',
        'kassadin','karma','jayce','ezreal','ashe'],
    c4=['wukong','velkoz','soraka','kayle','jinx','jhin','irelia',
        'fizz','chogath'],
    c5=['thresh','miss_fortune','lulu','gangplank','ekko','aurelion_sol']) # for distribution
champ_level_info = dict(
    zoe=dict(health=500,attack_damage=40,dps=28,attack_range=3,
        attack_speed=0.7,armor=20,magical_resistance=20,mana=[90,120]),
    ziggs=dict(health=500,attack_damage=40,dps=28,attack_range=3,
        attack_speed=0.7,armor=20,magical_resistance=20,mana=[0,40]),
    xayah=dict(health=500,attack_damage=55,dps=41,attack_range=3,
        attack_speed=0.75,armor=20,magical_resistance=20,mana=[0,50]),
    twistedFate=dict(health=500,attack_damage=40,dps=28,attack_range=3,
        attack_speed=0.7,armor=20,magical_resistance=20,mana=[0,75]),
    poppy=dict(health=650,attack_damage=50,dps=28,attack_range=1,
        attack_speed=0.55,armor=40,magical_resistance=20,mana=[60,100]),
    malphite=dict(health=700,attack_damage=70,dps=35,attack_range=1,
        attack_speed=0.5,armor=30,magical_resistance=20,mana=[0,0]),
    leona=dict(health=600,attack_damage=50,dps=28,attack_range=1,
        attack_speed=0.55,armor=40,magical_resistance=20,mana=[50,100]),
    khazix=dict(health=500,attack_damage=50,dps=30,attack_range=1,
        attack_speed=0.7,armor=25,magical_resistance=20,mana=[0,65]),
    jarvan_iv=dict(health=650,attack_damage=50,dps=30,attack_range=1,
        attack_speed=0.6,armor=40,magical_resistance=20,mana=[50,100]),
    graves=dict(health=650,attack_damage=55,dps=30,attack_range=1,
        attack_speed=0.55,armor=35,magical_resistance=20,mana=[50,80]),
    fiora=dict(health=450,attack_damage=45,dps=45,attack_range=1,
        attack_speed=1,armor=30,magical_resistance=20,mana=[0,85]),
    caitlyn=dict(health=500,attack_damage=45,dps=34,attack_range=5,
        attack_speed=0.75,armor=20,magical_resistance=20,mana=[0,125]),
    yasuo=dict(health=600,attack_damage=50,dps=38,attack_range=1,
        attack_speed=0.75,armor=30,magical_resistance=20,mana=[0,100]),
    xin_zhao=dict(health=650,attack_damage=60,dps=42,attack_range=1,
        attack_speed=0.7,armor=35,magical_resistance=20,mana=[0,50]),
    sona=dict(health=550,attack_damage=40,dps=26,attack_range=3,
        attack_speed=0.65,armor=20,magical_resistance=20,mana=[0,40]),
    shen=dict(health=700,attack_damage=60,dps=42,attack_range=1,
        attack_speed=0.7,armor=35,magical_resistance=20,mana=[100,150]),
    rakan=dict(health=600,attack_damage=45,dps=32,attack_range=2,
        attack_speed=0.7,armor=35,magical_resistance=20,mana=[50,150]),
    mordekaiser=dict(health=650,attack_damage=55,dps=33,attack_range=1,
        attack_speed=0.6,armor=40,magical_resistance=20,mana=[0,90]),
    lucian=dict(health=500,attack_damage=55,dps=39,attack_range=4,
        attack_speed=0.7,armor=25,magical_resistance=20,mana=[0,35]),
    kaisa=dict(health=550,attack_damage=50,dps=38,attack_range=2,
        attack_speed=0.75,armor=20,magical_resistance=20,mana=[0,60]),
    darius=dict(health=650,attack_damage=60,dps=39,attack_range=1,
        attack_speed=0.65,armor=35,magical_resistance=20,mana=[0,70]),
    blitzcrank=dict(health=650,attack_damage=55,dps=28,attack_range=1,
        attack_speed=0.5,armor=35,magical_resistance=20,mana=[125,125]),
    annie=dict(health=600,attack_damage=40,dps=26,attack_range=2,
        attack_speed=0.65,armor=35,magical_resistance=20,mana=[75,150]),
    ahri=dict(health=600,attack_damage=45,dps=34,attack_range=3,
        attack_speed=0.75,armor=20,magical_resistance=20,mana=[0,60]),
    vi=dict(health=750,attack_damage=60,dps=39,attack_range=1,
        attack_speed=0.65,armor=35,magical_resistance=20,mana=[70,140]),
    syndra=dict(health=600,attack_damage=45,dps=32,attack_range=3,
        attack_speed=0.7,armor=20,magical_resistance=20,mana=[0,50]),
    shaco=dict(health=650,attack_damage=55,dps=44,attack_range=1,
        attack_speed=0.8,armor=25,magical_resistance=20,mana=[0,60]),
    rumble=dict(health=800,attack_damage=50,dps=35,attack_range=1,
        attack_speed=0.7,armor=35,magical_resistance=20,mana=[0,60]),
    neeko=dict(health=800,attack_damage=50,dps=33,attack_range=2,
        attack_speed=0.65,armor=30,magical_resistance=20,mana=[75,150]),
    master_yi=dict(health=750,attack_damage=55,dps=44,attack_range=1,
        attack_speed=0.8,armor=30,magical_resistance=20,mana=[0,55]),
    lux=dict(health=600,attack_damage=40,dps=28,attack_range=4,
        attack_speed=0.7,armor=20,magical_resistance=20,mana=[50,100]),
    kassadin=dict(health=800,attack_damage=50,dps=33,attack_range=1,
        attack_speed=0.65,armor=30,magical_resistance=20,mana=[40,100]),
    karma=dict(health=600,attack_damage=50,dps=33,attack_range=3,
        attack_speed=0.65,armor=20,magical_resistance=20,mana=[75,100]),
    jayce=dict(health=750,attack_damage=60,dps=42,attack_range=1,
        attack_speed=0.7,armor=40,magical_resistance=20,mana=[0,80]),
    ezreal=dict(health=600,attack_damage=60,dps=42,attack_range=3,
        attack_speed=0.7,armor=20,magical_resistance=20,mana=[60,120]),
    ashe=dict(health=600,attack_damage=60,dps=48,attack_range=5,
        attack_speed=0.8,armor=20,magical_resistance=20,mana=[50,125]),
    wukong=dict(health=850,attack_damage=50,dps=38,attack_range=1,
        attack_speed=0.75,armor=40,magical_resistance=20,mana=[50,150]),
    velkoz=dict(health=650,attack_damage=45,dps=34,attack_range=4,
        attack_speed=0.75,armor=20,magical_resistance=20,mana=[0,80]),
    soraka=dict(health=650,attack_damage=45,dps=34,attack_range=3,
        attack_speed=0.75,armor=30,magical_resistance=20,mana=[50,150]),
    kayle=dict(health=700,attack_damage=60,dps=48,attack_range=3,
        attack_speed=0.8,armor=25,magical_resistance=20,mana=[0,60]),
    jinx=dict(health=600,attack_damage=70,dps=49,attack_range=3,
        attack_speed=0.7,armor=20,magical_resistance=20,mana=[0,0]),
    jhin=dict(health=600,attack_damage=90,dps=81,attack_range=5,
        attack_speed=0.9,armor=20,magical_resistance=20,mana=[0,0]),
    irelia=dict(health=800,attack_damage=70,dps=60,attack_range=1,
        attack_speed=0.85,armor=35,magical_resistance=20,mana=[0,30]),
    fizz=dict(health=650,attack_damage=60,dps=42,attack_range=1,
        attack_speed=0.75,armor=25,magical_resistance=20,mana=[80,150]),
    chogath=dict(health=1000,attack_damage=70,dps=42,attack_range=1,
        attack_speed=0.6,armor=20,magical_resistance=20,mana=[50,150]),
    thresh=dict(health=950,attack_damage=50,dps=48,attack_range=2,
        attack_speed=0.95,armor=35,magical_resistance=20,mana=[50,85]),
    miss_fortune=dict(health=800,attack_damage=60,dps=66,attack_range=4,
        attack_speed=1.1,armor=20,magical_resistance=20,mana=[50,150]),
    lulu=dict(health=800,attack_damage=45,dps=38,attack_range=3,
        attack_speed=0.85,armor=25,magical_resistance=20,mana=[75,150]),
    gangplank=dict(health=1000,attack_damage=60,dps=60,attack_range=1,
        attack_speed=1,armor=30,magical_resistance=20,mana=[50,150]),
    ekko=dict(health=850,attack_damage=60,dps=54,attack_range=1,
        attack_speed=0.9,armor=30,magical_resistance=20,mana=[50,150]),
    aurelion_sol=dict(health=900,attack_damage=10,dps=8,attack_range=1,
        attack_speed=0.8,armor=30,magical_resistance=20,mana=[30,80]),
    )
champ_distribution = dict(
    l1=[1,0,0,0,0],
    l2=[1,0,0,0,0],#4
    l3=[0.70,0.3,0.0,0.0,0.0],#6
    l4=[0.50,0.35,0.15,0.0,0.0],#10
    l5=[0.35,0.4,0.2,0.05,0.0],#20
    l6=[0.2,0.35,0.35,0.1,0.0],#32
    l7=[0.14,0.3,0.4,0.15,0.01],#50
    l8=[0.15,0.2,0.35,0.24,0.06],#66
    l9=[0.1,0.15,0.3,0.3,0.15]
    )
sushi_distribution = dict(
    r1=[1,0,0,0,0],
    r2=[0.12,0.44,0.44,0,0],
    r3=[0.12,0.2,0.38,0.3,0],
    r4=[0.05,0.15,0.3,0.4,0.1],
    r5=[0.05,0.15,0.3,0.4,0.1],
    r6=[0.05,0.15,0.3,0.4,0.1],
    r7=[0.05,0.15,0.3,0.4,0.1]
    )

synergy_info = dict(
    Celestial=dict(rate=[2,4,6],effect=[0.15,0.3,0.6],
        description='heal of damage percent'),
    Chrono=dict(rate=[2,4,6],effect=[0.15,0.35,0.65],
        description='attack speed'),
    Cybernetic=dict(rate=[3,6],effect=[[350,50],[800,80]],
        description='health,damage when item occupied'),
    Dark_Star=dict(rate=[3,6,9],effect=[[0.7,1],[1.5,3],[2.5,5]],
        description='damage percent, hexes'),
    Mech_Pilot=dict(rate=[3],effect=[1],
        description='mech robot'),
    Rebel=dict(rate=[3,6],effect=[[150,0.1],[225,0.12]],
        description='shield,damaage per adjacent units'),
    Space_Pirate=dict(rate=[2,4],effect=[[0.5,0],[0.5,0.15]],
        description='percent of 1 gold & random item'),
    Star_Guardian=dict(rate=[3,6],effect=[30,60],
        description='mana restore when other champ use skill'),
    Valkyrie=dict(rate=[2],effect=[0.5],
        description='critical when health below percent'),
    Void=dict(rate=[3],effect=[1.0],
        description='true damage'),
    Blademaster=dict(rate=[3,6],effect=[0.3,0.55],
        description='chance to attack other two champs'),
    Blaster=dict(rate=[2,4],effect=[3,6],
        description='additional attack for every fourth attack'),
    Brawler=dict(rate=[2,4],effect=[300,750],
        description='additional health'),
    Demolitionist=dict(rate=[3],effect=[1.5],
        description='stun for seconds when skill'),
    Infiltrator=dict(rate=[2,4],effect=[0.5,0.8],
        description='bonus attack speed, when initialize when takedown'),
    Mana_Reaver=dict(rate=[2,4],effect=[0.4,0.4],
        description='first attack or all attacks mana usage increase'),
    Mercenary=dict(rate=[1],effect=[5],
        description='add skill'),
    Mystic=dict(rate=[2,4],effect=[30,120],
        description='skill resistance'),
    Protector=dict(rate=[2,4],effect=[0.2,0.4],
        description='4 secs for max health shields when skill cast'),
    Sniper=dict(rate=[2],effect=[0.12],
        description='damage increase per hex'),
    Sorcerer=dict(rate=[2,4,6],effect=[0.2,0.4,0.8],
        description='skill damage increase'),
    Starship=dict(rate=[1],effect=[20],
        description='20 mana per sec & move around'),
    Vanguard=dict(rate=[2,4],effect=[60,250],
        description='add armor'),
    )
