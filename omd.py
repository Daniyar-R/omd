# Guido van Rossum <guido@python.org>

def step1():
    """Первый шаг утки-маляра"""

    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    """Второй шаг утки-маляра, если она пошла с зонтом"""

    print('По дороге в бар на утку-маляра чуть не пролили краску, но зонтик защитил её.\n'
          'Ура!\n'
          'Вдруг утка-маляр вспомнила, что ей нужно готовиться к завтрашним занятиям '
          'по химии лакокрасочных материалов. '
          'Ей всё-таки пойти в бар?'
          )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        print('Утка-маляр нашла в баре новых друзей-программистов и решила сменить профессию!')
    else:
        print('Утка-маляр сдала зачет на отлично!')


def step2_no_umbrella():
    """Второй шаг утки-маляра, если она пошла без зонта"""

    print('По дороге в бар на утку-маляра пролили краску. \n'
          'Теперь она стоит перед выбором: вернуться домой и принять ванну, или вместо этого пойти на колорфест. '
          'Ей всё-таки пойти на колорфест?'
          )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        print('Утка-маляр нашла на колорфесте новых друзей-диджеев и решила сменить профессию!')
    else:
        print('Утка-маляр отмылась и хорошенько отдохнула!')


if __name__ == '__main__':
    step1()
