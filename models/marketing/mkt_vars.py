# -*- coding: utf-8 -*-
"""
	Mkt Vars - All Should become Class Vars - To each BL CLass
	
	Used by:
		- Marketing

	Created: 2019
	Last up: 14 Dec 2019
"""


_mode_list = [
		('normal',	'normal'),
		('legacy',	'legacy'),
		('test',	'test'),
]


_family_list = [

		('consultation',	'Consulta'), 
		('procedure',		'Procedimiento'),
		('product',			'Producto'), 

		('x', 				'x'), 
]


_subfamily_list = [

		# Services
		('consultation',	'Consulta'), 

		('laser',			'Laser'),
		('medical',			'T. Medico'),
		('cosmetology',		'Cosmeatria'),

		('gynecology',		'Ginecologia'),
		('echography',		'Ecografia'),
		('promotion',		'Promocion'),


		# Product
		('topical',			'Topico'),
		('kit',				'Kit'),
		('card',			'Tarjeta'),

		('other',			'Otros'), 
		('commission',		'Comision'), 




		('x', 				'x'), 

		#('none',			'none'),
		#('credit_note',		'credit_note'), 
]

_subsubfamily_list = [

		# Services
		('consultation',		'Consulta'), 

		#('co2',				'Laser Co2'),
		#('quick',				'Quick Laser'), 		
		#('m22',				'Laser M22'),
		('laser_co2',			'Laser Co2'),
		('laser_excilite',		'Laser Excilite'),
		('laser_m22',			'Laser M22'),
		('laser_quick',			'Quick Laser'), 		




		# Medical
		('medical',				'T. Medico'),

		('botox',				'Botox'),
		('cryosurgery',			'Criocirugia'),
		('hyaluronic_acid',		'Acido Hialuronico'),

		('infiltrations',		'Infiltraciones'),
		('mesotherapy',			'Mesoterapia'),
		('plasma',				'Plasma'),


		('REDUX',				'REDUX'),
		('redux',				'Redux'),

		('sclerotherapy',		'Escleroterapia'),
		('vitamin_c_intravenous',	'Vitamina C Endovenosa'),






		# Cosmetology
		('cosmetology',		'Cosmeatria'),
		#('LASER TRIACTIVE + CARBOXITERAPIA',		'LASER TRIACTIVE + CARBOXITERAPIA'),
		#('CARBOXITERAPIA',		'CARBOXITERAPIA'),
		#('PUNTA DE DIAMANTES',		'PUNTA DE DIAMANTES'),
		('carboxytherapy', 					'Carboxiterapia'),
		('diamond_tip', 					'Punta de Diamante'),
		('laser_triactive_carboxytherapy', 	'Laser Triactivo + Cosmeatria'),


		# New
		('gynecology',		'Ginecologia'),
		('echography',		'Ecografia'),
		('promotion',		'Promocion'),

		# Product
		('commercial',		'Comercial'),
		('chavarri',		'Chavarri'),

		# Other
		('other',			'Otros'), 
		('commission',		'Comision'), 






		# 2018

		# Medical
		#('botulinum_toxin', 'botulinum_toxin'),
		#('criosurgery', 	'criosurgery'), 
		#('hyaluronic_acid', 	'hyaluronic_acid'), 
		#('infiltration',			'infiltration'), 
		#('intravenous_vitamin', 	'intravenous_vitamin'), 
		#('intravenous_vitamin', 	'intravenous_vitamin'), 
		#('lepismatic',			'lepismatic'), 
		#('mesotherapy_nctf',			'mesotherapy_nctf'), 
		('botulinum_toxin', 	'Botox - 2018'),
		('criosurgery', 		'Criocirugia - 2018'), 
		('hyaluronic_acid', 	'Acido Hialuronico - 2018'), 
		('infiltration',		'Infiltraciones - 2018'), 
		('intravenous_vitamin', 'Vitamina C Endovenosa - 2018'), 
		('lepismatic',			'Lepismatico - 2018'), 
		('mesotherapy_nctf',	'Mesoterapia NCTF - 2018'), 




		# Cosmetology
		('triactive_carboxytherapy',			'triactive_carboxytherapy'), 
		('triactive_carboxytherapy_reductionchamber',			'triactive_carboxytherapy_reductionchamber'), 
		('carboxytherapy', 	'carboxytherapy'),
		('diamond_tip', 	'diamond_tip'),


		# Laser
		('laser_ipl', 		'laser_ipl'), 
		('laser_ndyag', 	'laser_ndyag'), 

		('x', 				'x'), 
		#('other',			'other'), 
		
]




_year_order_list = [
					('2019', 		'2019'),
					('2018', 		'2018'),
					('2017', 		'2017'),
					('2016', 		'2016'),
]

_month_order_list = [
					('01', 		'ENE'),
					('02', 		'FEB'),
					('03', 		'MAR'),
					('04', 		'ABR'),
					('05', 		'MAY'),
					('06', 		'JUN'),
					('07', 		'JUL'),
					('08', 		'AGO'),
					('09', 		'SET'),
					('10', 		'OCT'),
					('11', 		'NOV'),
					('12', 		'DIC'),
]
