#!/usr/bin/env python3

class Functions:
	def __init__(self, current_f_index=0):
		self.current_f_index = current_f_index
		self.function_dictionnary = {
			"Pieds <-> Metres": (lambda a : a * 3.28084, lambda b : b / 3.28084),
			"Km/h <-> Miles/heure" : (lambda a: a / 1.60934, lambda b: b * 1.60934),
			"Km/h <-> Noeuds": (lambda a: a / 1.852, lambda b: b * 1.852),
			"MilesUS/gallon <-> Litres/km": (lambda a: a / 2.35215, lambda b: b * 2.35215),
			"MilesUK/gallon <-> Litres/km": (lambda a: a / 2.824814, lambda b: b * 2.824814), 
			"Celsius <-> Fahrenheit": (lambda a: (a* (9/5)) +32, lambda b: (b-32) * 5/9 ),
			"Celsius <-> Kelvin": (lambda a: a - 273.15, lambda b : b + 273.15),
			"Bits <-> Octets" : (lambda a: a * 8, lambda b: b / 8),
			"Heures <-> Minutes": (lambda a : a * 60, lambda b : b / 60),
			"Heures <-> secondes": (lambda a : a / 3600, lambda b : b * 3600), 
			"Minutes <-> Secondes": (lambda a: a / 60, lambda b : b * 60)}
		
	def unwrap(self):
		return list(self.function_dictionnary.keys()), list(self.function_dictionnary.keys())[self.current_f_index]
	
	def get_func(self, choice, pos):
		if (pos == 0):
			fst, _ = self.function_dictionnary[choice]
			return fst
		_, snd = self.function_dictionnary[choice]
		return snd