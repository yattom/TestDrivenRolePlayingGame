class Hero:
  def __init__(self, level):
    self.level = level
    self.base_atk = 1
    self.base_blk = 1
    self.max_hp = self.hp = 10
    self.alive = True
  
  def is_alive(self):
    return self.hp > 0

  def take_damage(self, dmg):
    assert dmg > 0
    self.hp -= dmg
    if self.hp < 0:
      # dead
      self.hp = 0
  
  @property
  def atk(self):
    return self.base_atk

  @property
  def blk(self):
    return self.base_blk


class Creatures:
  class Creature:
    def __init__(self, level, atk, blk, hp):
      self.level = level
      self.atk = atk
      self.blk = blk
      self.hp = hp
    
    def take_damage(self, dmg):
      assert dmg > 0
      self.hp -= dmg
      if self.hp < 0:
        # dead
        self.hp = 0
    
    def is_alive(self):
      return self.hp > 0
  
  class Dragon(Creature):
    def __init__(self):
      super().__init__(100, 100, 100, 1000)

  class LargeMouse(Creature):
    def __init__(self):
      super().__init__(1, 1, 0, 1)

  class WildDog(Creature):
    def __init__(self):
      super().__init__(1, 2, 0, 4)

  @staticmethod
  def spawn(type):
    if type == 'VeryWeakEnemy':
      return Creatures.LargeMouse()
    if type == 'WeakEnemy':
      return Creatures.WildDog()
    assert False, "type is invalid: type='{}'".format(type)
    
    
class Encounter:
  def __init__(self, hero, foe):
    self.hero = hero
    self.foe = foe
  
  def resolve(self):
    while(self.hero.is_alive() and self.foe.is_alive()):
      dmg_to_foe = self.hero.atk - self.foe.blk
      if dmg_to_foe > 0:
        self.foe.take_damage(dmg_to_foe)
        if not self.foe.is_alive():
          break
      dmg_to_hero = self.foe.atk - self.hero.blk
      if dmg_to_hero > 0:
        self.hero.take_damage(dmg_to_hero)
        if not self.hero.is_alive():
          break


class Judgement:
  def generic(cond, reason):
    class Generic:
      def __init__(self, hero):
        if cond(hero):
          self.passed = True
        else:
          self.passed = False
          self.reason = reason
    return Generic
        
  class Level(generic(lambda hero: hero.level >= 10, "Level too low")):
    pass
        
  class Alive(generic(lambda hero: hero.is_alive(), "Dead")):
    pass
        
  def __init__(self, hero):
    self.hero = hero
    judges = [
      Judgement.Alive(hero),
      Judgement.Level(hero),
    ]
    
    self.passed = True
    self.reasons = []
    for j in judges:
      if not j.passed:
        self.reasons.append(j.reason)
        self.passed = False