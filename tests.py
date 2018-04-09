import pytest
from tdrpg import Hero, Creatures, Encounter, Judgement, Items

@pytest.mark.skip
def test_triumphant():
  '''
  Write code here to make test_triumphant() pass.
  Look for clues in test cases below.

  このテストケースにコードを書いて、テストが成功するようにしてください。
  他のテストケースにヒントが隠されています。
  '''
  hero = Hero(level=1)
  
  # Adventure!
  # ... write something here
  
  judgement = Judgement(hero)
  assert judgement.passed
  assert judgement.final_message == "Hero is triumphant!"
  

def test_newborn_hero():
  hero = Hero(level=1)
  judgement = Judgement(hero)
  assert judgement.passed == False
  assert "Level too low" in judgement.reasons
  
  
def test_suicidal_attack():
  hero = Hero(level=1)
  foe = Creatures.Dragon()
  Encounter(hero, foe).resolve()
  judgement = Judgement(hero)
  assert judgement.passed == False
  assert "Dead" in judgement.reasons


def test_fight_weakling_and_survive():
  hero = Hero(level=1)
  foe = Creatures.spawn("VeryWeakEnemy")
  Encounter(hero, foe).resolve()
  assert hero.is_alive()


def test_fighting_weak_enemies_will_damage_hero_and_eventually_kill():
  hero = Hero(level=1)
  assert hero.max_hp == hero.hp 
  foe = Creatures.spawn("WeakEnemy")
  Encounter(hero, foe).resolve()
  assert hero.is_alive()
  assert hero.max_hp > hero.hp 
  
  for i in range(3):
    Encounter(hero, Creatures.spawn("WeakEnemy")).resolve()
  assert hero.is_alive() == False
  
  
def test_fight_with_weapon():
  barehand_hero = Hero(level=1)
  armed_hero = Hero(level=1)
  armed_hero.equip(Items.Sword())
  rounds_barehand = Encounter(barehand_hero, Creatures.spawn("WeakEnemy")).resolve().rounds 
  rounds_armed = Encounter(armed_hero, Creatures.spawn("WeakEnemy")).resolve().rounds 
  assert rounds_barehand > rounds_armed
  assert barehand_hero.is_alive()
  assert armed_hedo.is_alive()