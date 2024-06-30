from abc import ABC, abstractmethod
from random import random


class Character(ABC):
    @abstractmethod
    def change_weapon(self):
        pass


class Weapon(ABC):
    @abstractmethod
    def attack(self, character, distance):
        pass


class Fighter(Character):
    def __init__(self, name, weapon, defense=300, attack_skill=3):
        self.name = name
        self.weapon = weapon
        self.defense = defense
        self.attack_skill = attack_skill

    def change_weapon(self):
        print(f'Боец {self.name} выбрал оружие - '
              f'{self.weapon.__class__.__name__}: cила атаки '
              f'c учетом навыка бойца: '
              f'{self.weapon.att_score*self.attack_skill}')


class Monster(Character):
    def __init__(self, name, weapon, defense=500, attack_skill=2):
        self.name = name
        self.weapon = weapon
        self.defense = defense
        self.attack_skill = attack_skill

    def change_weapon(self):
        print(f'Монстр {self.name} выбрал оружие -'
              f' {self.weapon.__class__.__name__}: cила атаки '
              f'c учетом навыка бойца: '
              f'{self.weapon.att_score*self.attack_skill}')


class Sword(Weapon):
    def __init__(self, att_score=100):
        self.att_score = att_score

    def attack(self, character, distance):
        if distance < 3:
            print(f'  {character} наносит удар мечом ', end='')
            # Возвращает урон с учтом везения
            return self.att_score*random()
        else:
            print(f'   {character} ждет ', end='')
            return 0


class Bow(Weapon):
    def __init__(self, att_score=150):
        self.att_score = att_score

    def attack(self, character, distance):
        print(f'  {character} стреляет из лука ', end='')
        # Урон с учетом везения
        att_score_result = self.att_score*random()
        if distance < 2:
            return 0
        elif distance < 20:
            return att_score_result
        elif distance < 50:
            return att_score_result*0.7
        elif distance <= 100:
            return att_score_result*0.5
        elif distance > 100:
            return 0
            
