from os import system, name
from random import choice

from classes import Fighter, Monster, Sword, Bow

START_DISTANCE = 100

weapons = [Sword(), Bow()]


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def battle(fighter_tmp, monster_tmp):
    ''' Реализация битвы между персонажами '''
    distance = START_DISTANCE
    step = 1
    fighter_tmp.change_weapon()
    monster_tmp.change_weapon()
    while True:
        print(f'\nХод № {step} - Расстояние между бойцами {distance} метров '
              f'Защита монстра: {monster_tmp.defense:.1f} - Защита бойца: '
              f'{fighter_tmp.defense:.1f}')
        fighter_tmp.weapon.distance = distance
        monster_tmp.defense = monster_tmp.defense - fighter_tmp.weapon.attack(
           fighter_tmp.name, distance)*fighter_tmp.attack_skill
        if monster_tmp.defense < 0:
            print(f'\nМонстр {monster_tmp.name} уничтожен!')
            break
        if distance > 2:
            distance -= 2
        else:
            distance = 2
        monster_tmp.weapon.distance = distance
        fighter_tmp.defense = fighter_tmp.defense - monster_tmp.weapon.attack(
            monster_tmp.name, distance)*monster_tmp.attack_skill
        if fighter_tmp.defense < 0:
            print(f'\nБоец {fighter_tmp.name} уничтожен!')
            break
        step += 1


def main():
    clear_screen()
    print('Смертельная битва началась')
    weapon_fighter = choice(weapons)
    fighter = Fighter('Лю Кан', weapon_fighter)

    weapon_monster = choice(weapons)
    monster = Monster('Саб-Зиро', weapon_monster)
    battle(fighter, monster)


if __name__ == '__main__':
    main()
