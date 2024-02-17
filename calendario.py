from funciones import es_bisiesto

class Dia:
    def __init__(self, dia = 1, mes = 1, anyo = 1970):
        # Inicializamos calendario. Valores por defecto 1 de enero de 1970
        self.dia = dia
        self.mes = mes
        self.anyo = anyo
        # Comprobamos que el calendario no dé fallos 
        self.comprobar_dia()
        self.comprobar_mes()
        self.comprobar_anyo()
        # Asignamos el día de la semana correspondiente
        self.dia_semana = self.zeller()

    def info(self):
        # Creamos una lista para corresponder al día numérico con su nombre
        dia_semana = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

        # Usamos un lista para corresponder el mes en número con su nombre
        mes_texto = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        
        return f"{dia_semana[self.dia_semana]}, {self.dia} de {mes_texto[self.mes-1]} de {self.anyo}"

    def zeller(self):
        mes = self.mes
        anyo = self.anyo

        # Ajustamos el mes si fuera enero
        if mes == 1 or mes == 2:
            mes += 12
            anyo -= 1
        
        # Calculamos el algoritmo
        a = anyo % 100
        b = anyo // 100
        c = 2 - b + b // 4
        d = a // 4
        e = 13 * (mes + 1) // 5
        if anyo >= 2000:
            # Aplicamos la corrección para años posteriores al 2000
            f = a + c + d + e + self.dia-1
            f = f % 7
        else:
            f = a + c + d + e + self.dia
            f = f % 7
        
        

        return f

    def comprobar_dia(self):
        # Aseguramos que el día dado no exceda el número de días del mes
        if (self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11) and self.dia > 30:
            raise ValueError
        elif self.mes == 2:
            if self.dia > 29:
                raise ValueError
            elif self.dia == 29 and not(es_bisiesto(self.anyo)):
                raise ValueError
        elif self.dia > 31:
            raise ValueError
    
    def comprobar_mes(self):
        # Aseguramos que el mes esté entre enero y diciembre
        if self.mes < 1 or self.mes > 12:
            raise ValueError
    
    def comprobar_anyo(self):
        # Aseguramos que el año sea en la era después de Cristo
        if self.anyo < 1:
            raise ValueError



class WallCalendar:
    def __init__(self, dia=1, mes=1, anyo=1970):
        # Inicializamos la fecha. Por defecto usamos el valor 1 de enero de 1970
        self.dia = dia
        self.mes = mes
        self.anyo = anyo
        
        # Pasamos el exceso de días al mes posterior
        dias = self.dias_en_mes(self.mes)
        while self.dia > dias:
            self.dia -= dias
            self.mes += 1
            dias = self.dias_en_mes(self.mes)
        
        # Pasamos el exceso de meses al año posterior
        while self.mes > 12:
            self.mes -= 12
            self.anyo += 1

        dia_semana = Dia(self.dia, self.mes, self.anyo)
        self.dia_semana = dia_semana.dia_semana
    
    def mostrar_dia(self):
        # Creamos una lista para corresponder al día numérico con su nombre
        dia_semana = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

        # Inicializamos una lista con el correspondiente en texto de cada mes.
        mes_texto = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return f"{dia_semana[self.dia_semana]}, {self.dia} de {mes_texto[self.mes-1]} de {self.anyo}"
        

    def dias_en_mes(self, mes):
        # Comprobamos el número de días del mes
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return 31
        elif mes == 2:
            if es_bisiesto(self.anyo):
                return 29
            else:
                return 28
        else:
            return 30
    
    def avanzar_un_dia(self):
        # Avanzamos un día en la instancia
        self.dia += 1
        self.dia_semana += 1

        # Comprobamos que no haya exceso de días en el mes tras el avance
        dias = self.dias_en_mes(self.mes)
        while self.dia > dias:
            self.dia -= dias
            self.mes += 1
            dias = self.dias_en_mes(self.mes)
        
        # Comprobamos que no haya exceso de años tras el avance
        while self.mes > 12:
            self.mes -= 12
            self.anyo += 1

    
    