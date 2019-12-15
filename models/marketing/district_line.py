# -*- coding: utf-8 -*-
"""
	District Line - Object Oriented
	
	For Marketing

	Created: 				13 Dec 2019
	Last up: 				13 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

import unidecode

class DistrictLine(models.Model):	
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.district.line'
	
	#_name = 'openhealth.district.line'
	
	#_order = 'idx asc'


# ----------------------------------------------------------- Class Methods -----------------------

	@classmethod
	def get_district_sector(cls, name):
		"""
		Get District Sector
		Used by Lib Marketing
		"""
		print()
		print('Get District Sector')
		print(name)

		#unaccented_string = unidecode.unidecode(accented_string)		
		name = unidecode.unidecode(name)
		
		return cls.district_sector[name]


	@classmethod
	def get_zip_code(cls, name):
		"""
		Get Zip Code
		Used by Lib Marketing
		"""
		print()
		print('Get Zip')
		print(name)

		name = unidecode.unidecode(name)
		
		return cls.zip_dic[name]



	


# ----------------------------------------------------------- Class Vars -----------------------

	#_h_sector =  {
	district_sector =  {
				False: 		'x',

				'Santiago De Surco':	'Lima Tradicional',
				'Other': 		'Otros',

		# Tradicional
		'Lima':			'Lima Tradicional',
		'Barranco':		'Lima Tradicional',
		'Breña':		'Lima Tradicional',
		'Jesus Maria':	'Lima Tradicional',
		'La Molina':	'Lima Tradicional',
		'La Victoria':	'Lima Tradicional',
		'Lince':		'Lima Tradicional',
		'Magdalena del Mar':	'Lima Tradicional',
		'Miraflores':	'Lima Tradicional',
		'Pueblo Libre':	'Lima Tradicional',
		'Rimac':		'Lima Tradicional',
		'San Borja':	'Lima Tradicional',
		'San Isidro':	'Lima Tradicional',
		'San Luis':		'Lima Tradicional',
		'San Miguel':	'Lima Tradicional',
		'Santiago de Surco':	'Lima Tradicional',
		'Surquillo':	'Lima Tradicional',

		# Norte 
		'Ancon':			'Lima Norte',
		'Carabayllo':		'Lima Norte',
		'Comas':			'Lima Norte',
		'Independencia':	'Lima Norte',
		'Los Olivos':		'Lima Norte',
		'Puente Piedra':	'Lima Norte',
		'San Martin de Porres':	'Lima Norte',
		'Santa Rosa':		'Lima Norte',

		# Sur 
		'Chorrillos':				'Lima Sur',
		'Lurin':					'Lima Sur',
		'Pachacamac':				'Lima Sur',
		'Pucusana':					'Lima Sur',
		'Punta Negra':				'Lima Sur',
		'Punta Hermosa':			'Lima Sur',
		'San Bartolo':				'Lima Sur',
		'San Juan de Miraflores':	'Lima Sur',
		'Santa Maria del Mar':		'Lima Sur',
		'Villa El Salvador':		'Lima Sur',

		'Villa Maria del Triunfo':	'Lima Sur',

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


	zip_dic =  {
				False: 		0,
		'Santiago De Surco':	33,
		
		'Lima':			1,
		'Ancon':		2,
		'Ate':			3,
		'Barranco':		4,
		'Breña':		5,
		'Carabayllo':	6,
		'Comas':		7,
		'Chaclacayo':	8,
		'Chorrillos':	9,
		'El Agustino':	10,
		'Jesus Maria':	11,
		'La Molina':	12,
		'La Victoria':	13,
		'Lince':		14,
		'Lurigancho':	15,
		'Lurin':		16,
		'Magdalena del Mar':	17,
		'Miraflores':	18,
		'Pachacamac':	19,
		'Pucusana':		20,
		'Pueblo Libre':	21,
		'Puente Piedra':22,
		'Punta Negra':	23,
		'Punta Hermosa':24,
		'Rimac':		25,
		'San Bartolo':	26,
		'San Isidro':	27,
		'Independencia':	28,
		'San Juan de Miraflores':	29,
		'San Luis':	30,
		'San Martin de Porres':	31,
		'San Miguel':	32,
		'Santiago de Surco':	33,
		'Surquillo':	34,
		'Villa Maria del Triunfo':	35,
		'San Juan de Lurigancho':	36,
		'Santa Maria del Mar':	37,
		'Santa Rosa':	38,
		'Los Olivos':	39,
		'Cieneguilla':	40,
		'San Borja':	41,
		'Villa El Salvador':	42,
		'Santa Anita':	43,		
	}




