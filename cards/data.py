'''

'''

# global constants

IMAGE_DIRECTORY = "../images/"

# card colors
GRAY    = 0
BLACK   = 1
WHITE   = 2

# card types
MONSTER = 0
MAGIC   = 1
TRAP    = 2
FIELD   = 3

# card rarities
SURPLUS     = 0 # 70% of cards
COMMON      = 1 # 20% of cards
UNCOMMON    = 2 # ~8% of cards
RARE        = 3 # ~1% of cards
ULTRA       = 4 # ultra-rare
UNIQUE      = 5 # one-of-a-kind

# text colors for info formatting
COLORS={
# NAME      : 'rrggbbaa' # a == alpha
'RED'       : 'ff0000ff',
'ORANGE'    : 'ff8800ff',
'YELLOW'    : 'ffff00ff',
'GREEN'     : '00ff00ff',
'CYAN'      : '00ffffff',
'BLUE'      : '0000ffff',
'PURPLE'    : 'ff00ffff',
'WHITE'     : 'ffffffff',
'BLACK'     : '000000ff',
    }

class Global:
    ID = 100000

def nextID():
    Global.ID += 1
    return Global.ID

def getImagePath(imageName):
    return "{}{}".format(IMAGE_DIRECTORY, imageName)

def getCardID(name): return CARDS[name][0]
def getCardType(name): return CARDS[name][1]
def getCardColor(name): return CARDS[name][2]
def getCardRarity(name): return CARDS[name][3]
def getCardImage(name): return CARDS[name][4]
def getCardSummonCost(name): return CARDS[name][5]
def getCardAtk(name): return CARDS[name][6]
def getCardDef(name): return CARDS[name][7]
def getCardInfo(name): return CARDS[name][8]

CARDS={
# name : (ID, type, rarity, image / # req. sacrifices, atk, def, color / info)

    # equips
    
'Potion of War':(
    nextID(), MAGIC, GRAY, COMMON, 'potion_of_war.png',
    0, 0, 1,
    """ Equip/ Effect: +1/+0 for target Monster. """,
    ),
    
'Potion of Peace':(
    nextID(), MAGIC, GRAY, COMMON, 'potion_of_peace.png',
    0, 0, 1,
    """ Equip/ Effect: +0/+1 for target Monster. """,
    ),
    
'Hellbane':(
    nextID(), MAGIC, WHITE, COMMON, 'hellbane.png',
    0, 0, 2,
    """ Equip/ Effect: +2/+0 for target <color = #YELLOW>White</color> Monster. """,
    ),

'Dark Blade':(
    nextID(), MAGIC, BLACK, COMMON, 'dark_blade.png',
    0, 0, 2,
    """ Equip/ Effect: +2/+0 for target <color = #PURPLE>Black</color> Monster. """,
    ),

'Sacrificial Blade':(
    nextID(), MAGIC, BLACK, UNCOMMON, 'sacrificial_blade.png',
    1, 0, 2,
    """ Equip/ Effect: +2/+0 for target Monster. """,
    ),

    # damaging magic
    
'Firebomb':(
    nextID(), MAGIC, BLACK, COMMON, 'firebomb.png',
    0, 0, 1,
    """ Effect: Deal 3 <color = #RED><b>fire</b></color> damage to target card. """,
    ),
    
'Cavalry Charge':(
    nextID(), MAGIC, WHITE, COMMON, 'cavalry_charge.png',
    0, 0, 4,
    """ Effect: Target Monster has: +3/+0, Support; for 1 turn. """,
    ),

'Unholy Smite':(
    nextID(), MAGIC, BLACK, UNCOMMON, 'unholy_smite.png',
    0, 0, 1,
    """ Effect: Deal 2 damage to target card <b>or</b> 1 damage to opponent directly. """,
    ),

'Holy Smite':(
    nextID(), MAGIC, WHITE, UNCOMMON, 'holy_smite.png',
    0, 0, 1,
    """ Effect: Deal 4 damage to target card. """,
    ),

    # misc. magic

'All Inclusive Resort':(
    nextID(), MAGIC, WHITE, RARE, 'all_inclusive_resort.png',
    0, 0, 1,
    """ Effect: Destroy target Field card. """,
    ),

    # traps

'Hex':(
    nextID(), MAGIC, BLACK, UNCOMMON, 'hex.png',
    0, 0, 1,
    """ Trigger: Opponent activates a trap card.
Effect: Negate the effect and destroy the card. """,
    ),

'Teeth and Chains':(
    nextID(), MAGIC, GRAY, UNCOMMON, 'teeth_and_chains.png',
    0, 0, 1,
    """ Trigger: Opponent attacks a Monster you control.
Effect: Negate the attack and equip this card to the attacker for -2/-2. """,
    ),

'Pitfall':(
    nextID(), MAGIC, WHITE, RARE, 'pitfall.png',
    1, 0, 1,
    """ Trigger: Opponent attacks a Monster you control.
Effect: Negate the attack and destroy the attacking card. """,
    ),

    # field cards

'Graveyard':(
    nextID(), FIELD, BLACK, UNCOMMON, 'graveyard.png',
    0, 0, 7,
    """ Effect: +1/+0 for all Black Monsters. """,
    ),

'Temple':(
    nextID(), FIELD, WHITE, UNCOMMON, 'temple.png',
    0, 0, 7,
    """ Effect: +1/+0 for all White Monsters. """,
    ),

'Mire':(
    nextID(), FIELD, BLACK, UNCOMMON, 'mire.png',
    0, 0, 7,
    """ Effect: +0/+1 for all Black Monsters. """,
    ),

'Meadow':(
    nextID(), FIELD, WHITE, UNCOMMON, 'meadow.png',
    0, 0, 7,
    """ Effect: +0/+1 for all White Monsters. """,
    ),

'Penetrating Darkness':(
    nextID(), FIELD, BLACK, UNCOMMON, 'penetrating_darkness.png',
    0, 0, 3,
    """ Effect: -1/+0 for all White Monsters. """,
    ),

'Suppressing Light':(
    nextID(), FIELD, WHITE, UNCOMMON, 'suppressing_light.png',
    0, 0, 3,
    """ Effect: -1/+0 for all Black Monsters. """,
    ),

'Massengrab':(
    nextID(), FIELD, BLACK, UNCOMMON, 'massengrab.png',
    0, 0, 3,
    """ Effect: +0/-1 for all White Monsters. """,
    ),

'Holy Desert':(
    nextID(), FIELD, WHITE, UNCOMMON, 'holy_desert.png',
    0, 0, 3,
    """ Effect: +0/-1 to Def for all Black Monsters. """,
    ),

    # surplus monsters

'Pygmy Demon':(
    nextID(), MONSTER, BLACK, SURPLUS, 'pygmy_demon.png',
    0, 1, 1,
    """ Atk/ Support/ Effect: When summoned from your hand, you may summon another
<i>%NAME%</i> card from your deck. """,
    ),

'Brothers In Arms':(
    nextID(), MONSTER, GRAY, SURPLUS, 'brothers_in_arms.png',
    0, 1, 1,
    """ Atk/ Support/ Effect: Has +1/+1 for every other <i>%NAME%</i> you control. """,
    ),

    # common monsters

'Knight In Shining Armor':(
    nextID(), MONSTER, WHITE, COMMON, 'knight_in_shining_armor.png',
    0, 2, 3,
    """ Atk/ """,
    ),

'Paladin of the Sun':(
    nextID(), MONSTER, WHITE, COMMON, 'paladin_of_the_sun.png',
    0, 2, 2,
    """ Atk/ Support/ """,
    ),

'Ranger':(
    nextID(), MONSTER, WHITE, COMMON, 'ranger.png',
    0, 1, 1,
    """ Atk/ Ranged 2/ Support/ """,
    ),

'Crossbowelf':(
    nextID(), MONSTER, WHITE, COMMON, 'crossbow_elf.png',
    0, 2, 2,
    """ Atk/ Ranged 2/ Effect: Cannot attack if it attacked last turn. """,
    ),

'Rogue':(
    nextID(), MONSTER, BLACK, COMMON, 'rogue.png',
    1, 3, 3,
    """ Atk/ Effect: Use to destroy one card which is equipped to a card in play. """,
    ),

'Plague Bearer':(
    nextID(), MONSTER, BLACK, COMMON, 'plague_bearer.png',
    0, 1, 2,
    """ Atk/ Effect: When <i>%NAME%</i> attacks, it applies
<color = #PURPLE><b>miasma</b></color>. """,
    ),

'Plague Doctor':(
    nextID(), MONSTER, BLACK, COMMON, 'plague_doctor.png',
    0, 1, 4,
    """ Atk/ Resistance: Miasma/ Effect: Use to clear Miasma from target player,
<b>or</b> sacrifice <i>%NAME%</i> to clear Plague from target player. """,
    ),

    # uncommon monsters

'Longbowman':(
    nextID(), MONSTER, WHITE, UNCOMMON, 'longbowman.png',
    0, 2, 1,
    """ Atk/ Ranged 3/ """,
    ),

'Necromancer':(
    nextID(), MONSTER, BLACK, UNCOMMON, 'necromancer.png',
    0, 1, 3,
    """ Atk/ Effect: Use to summon one Monster from the dead; that Monster has
+0/-2 and will be removed from play if it dies again. """,
    ),

'Drech':(
    nextID(), MONSTER, WHITE, UNCOMMON, 'drech.png',
    0, 1, 3,
    """ Atk/ Effect: Use to create one 0/1 White Monster named "Drech Spore"
and play it under your control. """,
    ),

    # rare monsters
    
'Fortress Demon':(
    nextID(), MONSTER, BLACK, RARE, 'fortress_demon.png',
    2, 1, 10,
    """ Atk/ """,
    ),
    
'Claymore Demon':(
    nextID(), MONSTER, BLACK, RARE, 'claymore_demon.png',
    2, 10, 1,
    """ Atk/ """,
    ),

'Brick Man':(
    nextID(), MONSTER, WHITE, RARE, 'brick_man.png',
    1, 2, 6,
    """ Atk/ Support/ """,
    ),
    
'Fickle Cannon':(
    nextID(), MONSTER, WHITE, RARE, 'fickle_cannon.png',
    0, 8, 2,
    """ Atk/ Trigger: <i>%NAME%</i> attacks/ Effect: Flip a coin. If tails, the attack
fails. """,
    ),

    # ultra-rare monsters

'Protoborg':(
    nextID(), MONSTER, WHITE, ULTRA, 'protoborg.png',
    3, 7, 7,
    """ Atk/ Effect: When <i>%NAME%</i> attacks, you may apply
<color = #RED><b>fire</b></color>. """,
    ),

'dummy':(
    nextID(), MONSTER, BLACK, SURPLUS, '_____.png',
    0, 0, 1,
    """ Atk/ """,
    ),

} # immediately modify CARDS dict to improve formatting for data storage
count_types = [0,0,0,0]
count_colors= [0,0,0]
ndex = 8
for k,v in CARDS.items():
    assert(type(v[ndex]) == str)
    nv = list(v)

    # count number of each type of cards
    count_types[nv[1]] += 1
    count_colors[nv[7]] += 1
    
    # clean up string
    nv[ndex] = nv[ndex].replace("\n", ' ') # replace newlines in the info string with spaces
    # replace #COLOR strings with hexadecimal values
    for kk,vv in COLORS.items():
        nv[ndex] = nv[ndex].replace('#{}'.format(kk), '#{}'.format(vv))
    if nv[ndex][-1]==' ':
        nv[ndex] = nv[ndex][:-1] # remove trailing space
    nv[ndex] = nv[ndex].replace('%NAME%', kk) # %NAME% == this card's name
    nv[ndex] = nv[ndex].replace('%NL%', '\n') # %NL% == newline
    CARDS[k] = nv
#


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #               testing                 #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print("Count of Monster: ", count_types[MONSTER])
print("Count of Magic: ", count_types[MAGIC])
print("Count of Traps: ", count_types[TRAP])
print("Count of Field: ", count_types[FIELD])

print("Count of Gray: ", count_colors[GRAY])
print("Count of White: ", count_colors[WHITE])
print("Count of Black: ", count_colors[BLACK])
##print(CARDS['Firebomb'][ndex])














