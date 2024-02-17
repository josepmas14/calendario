from calendario import Dia, WallCalendar

def test_inicializar_calendario_por_defecto():

    fecha = Dia()
    assert fecha.dia == 1
    assert fecha.mes == 1
    assert fecha.anyo == 1970

    assert fecha.dia_semana == 5
    assert fecha.info() == "Jueves, 1 de enero de 1970"

def test_inicializar_calendario_cumple_Salva():
    fecha = Dia(26,11,2019)
    assert fecha.dia == 26
    assert fecha.mes == 11
    assert fecha.anyo == 2019

    assert fecha.dia_semana == 3
    assert fecha.info() == "Martes, 26 de noviembre de 2019"


def test_inicializar_calendario_dia_erroneo():
    try:
        fecha = Dia(31,11,2019)
    except ValueError:
        a = "Día erróneo"
    assert a == "Día erróneo"

def test_inicializar_calendario_mes_erroneo():
    try:
        fecha = Dia(3,17,2019)
    except ValueError:
        a = "Mes erróneo"
    assert a == "Mes erróneo"    

def test_inicializar_calendario_anyo_erroneo():
    try:
        fecha = Dia(3,12,-2019)
    except ValueError:
        a = "Año erróneo"
    assert a == "Año erróneo"    

def test_inicializar_calendario_bisiesto_erroneo():
    try:
        fecha = Dia(29,2,2019)
    except ValueError:
        a = "Día erróneo"
    assert a == "Día erróneo"


def test_inicializar_pared_por_defecto():
    calendario = WallCalendar()
    assert calendario.dia == 1
    assert calendario.mes == 1
    assert calendario.anyo == 1970

    assert calendario.dia_semana == 5
    assert calendario.mostrar_dia() == "Jueves, 1 de enero de 1970"

def test_inicializar_pared_dias_de_mas():
    calendario = WallCalendar(90,1,1970)
    assert calendario.dia == 31
    assert calendario.mes == 3
    assert calendario.anyo == 1970

    assert calendario.dia_semana == 3
    assert calendario.mostrar_dia() == "Martes, 31 de marzo de 1970"

def test_avanzar_un_dia():
    calendario = WallCalendar(21,11,2022)
    calendario.avanzar_un_dia()
    assert calendario.dia == 22
    assert calendario.mes == 11
    assert calendario.anyo == 2022
    calendario = WallCalendar(31,12,2022)
    calendario.avanzar_un_dia()
    assert calendario.dia == 1
    assert calendario.mes == 1
    assert calendario.anyo == 2023

def test_bisiesto_pared():
    calendario = WallCalendar(28,2,2024)
    assert calendario.dia == 28
    assert calendario.mes == 2
    assert calendario.anyo == 2024
    assert calendario.mostrar_dia() == "Miércoles, 28 de febrero de 2024"

    calendario.avanzar_un_dia()
    assert calendario.dia == 29
    assert calendario.mes == 2
    assert calendario.anyo == 2024
    assert calendario.mostrar_dia() == "Jueves, 29 de febrero de 2024"

    calendario.avanzar_un_dia()
    assert calendario.dia == 1
    assert calendario.mes == 3
    assert calendario.anyo == 2024
    assert calendario.mostrar_dia() == "Viernes, 1 de marzo de 2024"