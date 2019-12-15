# -*- coding: utf-8 -*-
"""
	Pricelist Marketing Order Line 

	Clean Sub Sub Family - Too long - Delegate to Product

	Created: 			26 Jun 2019
	Last updated: 		14 Dec 2019
"""
from openerp import models, fields, api

class MarketingOrderLine(models.Model):
	"""
	Used by Marketing
	To report on the new patient sales
	"""
	_name = 'price_list.marketing.order_line'
	_description = "PriceList Marketing Order Line"
	_order = 'date desc'


# ----------------------------------------------------------- Class Vars -----------------------

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






# ----------------------------------------------------------- Relational ------------------------------------------------------

	family = fields.Selection(

			#selection=mkt_vars._family_list,
			selection=_family_list,

		)


	subfamily = fields.Selection(
			#selection=mkt_vars._subfamily_list,
			selection=_subfamily_list,
		)


	subsubfamily = fields.Selection(
			#selection=mkt_vars._subsubfamily_list,
			selection=_subsubfamily_list,
		)





# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Marketing Id
	marketing_id = fields.Many2one(			
			'openhealth.marketing',
			ondelete='cascade', 			
		)

	# Patient Line
	patient_line_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)


	order = fields.Many2one(
			'sale.order',
			ondelete='cascade',
		)

	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente',
			ondelete='cascade',
		)

	doctor = fields.Many2one(
			'oeh.medical.physician',
			#string = "Médico", 	
		)

	product_id = fields.Many2one(
			'product.product',
			ondelete='cascade',			
		)

# ----------------------------------------------------------- Fields ------------------------------------------------------

	date = fields.Datetime(
		)

	product_uom_qty = fields.Float(
		)

	price_unit = fields.Float(
		)

	price_net = fields.Float(
		)

	price_list = fields.Char(
		)

	state = fields.Char(
		)


# ----------------------------------------------------------- Setters - Dep ? ------------------------------------------------------

	def set_patient_line_id(self, patient_line_id):

		self.patient_line_id = patient_line_id


