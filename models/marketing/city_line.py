# -*- coding: utf-8 -*-
"""
	City Line - Object Oriented
	
	For Marketing

	Created: 				13 Dec 2019
	Last up: 				13 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class CityLine(models.Model):	
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.city.line'
	
	#_name = 'openhealth.city.line'
	
	#_order = 'idx asc'



# ----------------------------------------------------------- Class Vars -----------------------

	#_h_sector_city =  {
	city_sector =  {
				False: 		'x',
				'Puerto_Maldonado': 	'Sur Este', 		# Madre de Dios 
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



