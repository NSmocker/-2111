



class Character:
  def __init__(self, character_type, move_speed,nickname,hp,mana,damage):
    self.character_type = character_type
    self.nickname = nickname
    self.move_speed = move_speed
    self.hp = hp
    self.mana = mana
    self.damage = damage


def MakeDamage(attacker_character, victim_character):
  print("Персонаж " +attacker_character.nickname + "наносить шкоду персонажу" + victim_character.nickname )
  victim_character.hp =   victim_character.hp - attacker_character.damage
  print("Кількість ХП у персонажа "+ victim_character.nickname +" :"+ str(victim_character.hp) )

character1 = Character("NPC",50,"Селянин",100,100,0)
character2 = Character("Monster",350,"Малий Зомбі",50,0,10)
character3 = Character("Monster",100,"Зомбі",100,0,15)
character4 = Character(nickname="Скелет",character_type="Monster",move_speed=100,hp=100,mana=0,damage=50)
MakeDamage(character3,character1)
