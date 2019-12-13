# -*- coding: utf-8 -*-

# Used by:
# 	- Marketing


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






_h_sector_city =  {
				'Other': 		'Otros',

				'Lima':			'Lima',
				'Callao': 		'Lima',
				'Huacho': 		'Lima',
				'Ancash': 		'Centro',
				'Huancavelica': 'Centro',
				'Huancayo': 	'Centro',
				'Huanuco': 		'Centro',
				'Huaraz': 		'Centro', 
				'Pucallpa': 	'Centro',
				'Cerro de Pasco': 	'Centro', 
				'Chiclayo': 	'Costa Norte',
				'Cajamarca': 	'Costa Norte',
				'Piura': 		'Costa Norte',
				'Trujillo': 	'Costa Norte',
				'Tumbes': 		'Costa Norte',
				'Ica': 			'Costa Sur',
				'Arequipa': 	'Costa Sur',
				'Tacna': 		'Costa Sur',
				'Moquegua': 	'Costa Sur',
				'Abancay': 		'Sur Este',
				'Ayacucho': 	'Sur Este',
				'Cuzco': 		'Sur Este',
				'Puerto Maldonado': 	'Sur Este', 		# Madre de Dios 
				'Puno': 		'Sur Este',
				'Iquitos': 		'Nor Este',
				'Chachapoyas': 	'Nor Este',
				'Moyobamba': 	'Nor Este',						# San Martin
				'Otros': 		'Otros',
}





zip_dic =  {
		'Santiago De Surco':	33,
		
		'Lima':			1,
		'Ancón':		2,
		'Ate':			3,
		'Barranco':		4,
		'Breña':		5,
		'Carabayllo':	6,
		'Comas':		7,
		'Chaclacayo':	8,
		'Chorrillos':	9,
		'El Agustino':	10,
		'Jesús María':	11,
		'La Molina':	12,
		'La Victoria':	13,
		'Lince':		14,
		'Lurigancho':	15,
		'Lurín':		16,
		'Magdalena del Mar':	17,
		'Miraflores':	18,
		'Pachacamac':	19,
		'Pucusana':		20,
		'Pueblo Libre':	21,
		'Puente Piedra':22,
		'Punta Negra':	23,
		'Punta Hermosa':24,
		'Rímac':		25,
		'San Bartolo':	26,
		'San Isidro':	27,
		'Independencia':	28,
		'San Juan de Miraflores':	29,
		'San Luis':	30,
		'San Martín de Porres':	31,
		'San Miguel':	32,
		'Santiago de Surco':	33,
		'Surquillo':	34,
		'Villa María del Triunfo':	35,
		'San Juan de Lurigancho':	36,
		'Santa María del Mar':	37,
		'Santa Rosa':	38,
		'Los Olivos':	39,
		'Cieneguilla':	40,
		'San Borja':	41,
		'Villa El Salvador':	42,
		'Santa Anita':	43,		
}



_h_sector =  {
				'Santiago De Surco':	'Lima Tradicional',
				'Other': 		'Otros',

		# Tradicional
		'Lima':			'Lima Tradicional',
		'Barranco':		'Lima Tradicional',
		'Breña':		'Lima Tradicional',
		'Jesús María':	'Lima Tradicional',
		'La Molina':	'Lima Tradicional',
		'La Victoria':	'Lima Tradicional',
		'Lince':		'Lima Tradicional',
		'Magdalena del Mar':	'Lima Tradicional',
		'Miraflores':	'Lima Tradicional',
		'Pueblo Libre':	'Lima Tradicional',
		'Rímac':		'Lima Tradicional',
		'San Borja':	'Lima Tradicional',
		'San Isidro':	'Lima Tradicional',
		'San Luis':		'Lima Tradicional',
		'San Miguel':	'Lima Tradicional',
		'Santiago de Surco':	'Lima Tradicional',
		'Surquillo':	'Lima Tradicional',



		# Norte 
		'Ancón':			'Lima Norte',
		'Carabayllo':		'Lima Norte',
		'Comas':			'Lima Norte',
		'Independencia':	'Lima Norte',
		'Los Olivos':		'Lima Norte',
		'Puente Piedra':	'Lima Norte',
		'San Martín de Porres':	'Lima Norte',
		'Santa Rosa':		'Lima Norte',



		# Sur 
		'Chorrillos':				'Lima Sur',
		'Lurín':					'Lima Sur',
		'Pachacamac':				'Lima Sur',
		'Pucusana':					'Lima Sur',
		'Punta Negra':				'Lima Sur',
		'Punta Hermosa':			'Lima Sur',
		'San Bartolo':				'Lima Sur',
		'San Juan de Miraflores':	'Lima Sur',
		'Santa María del Mar':		'Lima Sur',
		'Villa El Salvador':		'Lima Sur',
		'Villa María del Triunfo':	'Lima Sur',



		# Este 
		'Ate':			'Lima Este',
		'Chaclacayo':	'Lima Este',
		'Cieneguilla':	'Lima Este',
		'El Agustino':	'Lima Este',
		'Lurigancho':	'Lima Este',
		'San Juan de Lurigancho':	'Lima Este',
		'Santa Anita':	'Lima Este',
		


		# Oeste 
		'Callao':		'Lima Oeste',
}











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


