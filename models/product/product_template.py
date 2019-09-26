# -*- coding: utf-8 -*-
"""
*** Product Template

Created: 			  8 Apr 2019
Last up: 	 		 23 Aug 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from . import px_vars
from . import chk_product
from . import pl_prod_vars
from . import exc_prod

class ProductTemplate(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'product.template'

	_order = 'pl_idx_int'

	_description = 'Product Template'





# ----------------------------------------------------------- Getters -------------------------

	# Get Treatment
	#@api.multi
	def get_treatment(self):
		"""
		Get Product Treatment
		Used by: Session, Control.
		"""

		# Init
		_dic = {
					'LASER CO2 FRACCIONAL': 	'laser_co2',

					'QUICKLASER': 				'laser_quick',

					'LASER EXCILITE':			'laser_excilite',

					'LASER M22 IPL':			'laser_ipl',

					'LASER M22 ND YAG':			'laser_ndyag',
		}

		treatment = False


		print(self.pl_treatment)


		if self.pl_price_list in ['2019']:

			if self.pl_treatment in _dic:

				treatment = _dic[self.pl_treatment]

			else:
				print('Error: 1')


		elif self.pl_price_list in ['2018']:
			treatment = self.x_treatment

		
		else:
			print('Error: 2')


		return treatment




# ----------------------------------------------------------- Fields ------------------------

	pl_price_list = fields.Selection(

			#selection=px_vars._price_list_list,

			[
				('2019', '2019'),
				('2018', '2018'),
			],
		
			string='Lista de Precios',
			required=True,
		)





# ----------------------------------------------------------- Fix - Button -----------
	@api.multi
	def fix(self):
		"""
		Fix Product
		"""
		print()
		print('Product Fix')

		# Handle Exceptions
		#exc_prod.handle_exceptions(self)
		exc_prod.fix_exceptions(self)




# ----------------------------------------------------------- Validate - Button -----------
	@api.multi
	def validate(self):
		"""
		Validate Product
		"""
		print()
		print('Product Validate')

		# Handle Exceptions
		exc_prod.handle_exceptions(self)


	@api.multi
	def validate_all(self):
		"""
		Validate Product
		"""
		print()
		print('Product Validate All')


		# Search
		products = self.env['product.template'].search([
																	('pl_price_list', 'in', ['2019']),
															],
															#order='pl_prefix,pl_idx_int asc',
															#order='pl_idx_int,pl_prefix asc',
															order='pl_prefix asc',
															#limit=10,
															#limit=100,
															limit=600,
														)
		# Loop
		idx = 0
		for product in products:
			print()
			print(product.name)
	
			idx = idx + 1

			# Handle Exceptions
			exc_prod.handle_exceptions(product)

		print(idx)



# ----------------------------------------------------------- Configurator ------------------------
	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
		)


	def init_configurator(self):
		"""
		Initializes the Configurator
		Is compatible with Tacna. Does the search by type, not by name
		"""
		# Search
		if self.configurator.name in [False]:
			self.configurator = self.env['openhealth.configurator.emr'].search([
																					('x_type', 'in', ['emr']),
															],
															#order='date_begin,name asc',
															limit=1,
														)








# ----------------------------------------------------------- Natives ----------------------------------------------------
	# Treatment
	x_treatment = fields.Selection(

			#selection=prodvars._treatment_list,
			selection=pl_prod_vars._treatment_list,
		
			required=False,
		)


# ----------------------------------------------------------- Correct ----------------------------------------------------

	corr_medical = fields.Boolean(
		)

	corr_cosmetology = fields.Boolean(
		)



# ----------------------------------------------------------- Correct ----------------------------------------------------
	@api.multi
	def correct_subfamilies(self):
		"""
		Update
		"""
		print()
		print('Correct Subfamilies')


		model = 'product.template'

		family = ''


		if self.corr_medical:
			family = 'medical'

		if self.corr_cosmetology:
			family = 'cosmetology'



		# Search
		products = self.env[model].search([
														#('name', '=', name),
														('pl_price_list', 'in', ['2019']),
				
														('pl_family', 'in', [family]),
											],
												#order='date_order desc',
												#limit=1,
									)
		print(products)



		_dic_med = {
					'VICTAMINA C ENDOVENOSA': 	'vitamin_c_intravenous',

					'INFILTRACIONES': 		'infiltrations',
					'CRIOCIRUGIA': 			'cryosurgery',
					'ESCLEROTERAPIA': 		'sclerotherapy',
					'PLASMA': 				'plasma',

					'BOTOX': 				'botox',
					'REDUX': 				'redux',
					'ACIDO HIALURONICO': 	'hyaluronic_acid',
					'MESOTERAPIA NCTF': 	'mesotherapy',
		}

		_dic_cos = {

					'CARBOXITERAPIA': 					'carboxytherapy',
					'PUNTA DE DIAMANTES': 				'diamond_tip',
					'LASER TRIACTIVE + CARBOXITERAPIA': 'laser_triactive_carboxytherapy',
		}


		for product in products:
			print(product.name)
			print(product.pl_family)
			print(product.pl_treatment)
			print(product.pl_subfamily)
			print()

			if product.pl_family in ['medical']:
				product.pl_subfamily = _dic_med[product.pl_treatment]

			elif product.pl_family in ['cosmetology']:
				product.pl_subfamily = _dic_cos[product.pl_treatment]




# ---------------------------------------------- Fields - Categorized -----------------------------
	
	# Required

	pl_family = fields.Selection(

			selection=px_vars._family_list,
		
			string='Family',
			required=True,
		)

	pl_subfamily = fields.Selection(

			selection=px_vars._subfamily_list,
		
			string='Subfamily',
			required=True,
		)





	# Not Required
	pl_manufacturer = fields.Selection(
			selection=px_vars._manufacturer_list,
			string='Fabricante',
		)

	pl_brand = fields.Selection(
			selection=px_vars._brand_list,
			string='Marca',
		)






	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Treatment',
			#required=True,
		)

	pl_zone = fields.Selection(
			selection=px_vars._zone_list,
			string='Zone',
			#required=True,
		)

	pl_pathology = fields.Selection(
			selection=px_vars._pathology_list,
			string='Pathology',
			#required=True,
		)

	pl_level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			#required=True,
		)

	pl_sessions = fields.Selection(
			selection=px_vars._sessions_list,
			string='Sessions',
			#required=True,
		)

	pl_time = fields.Selection(
			selection=px_vars._time_list,
			string='Time',
			#required=True,
		)



# ---------------------------------------------- Fields - Floats ----------------------------------

	pl_price = fields.Float(
			'Price',
		)

	pl_price_vip = fields.Float(
			'Precio Vip',
		)

	pl_price_company = fields.Float(
			'Precio Empresa',
		)

	pl_price_session = fields.Float(
			'Price session',
		)

	pl_price_session_next = fields.Float(
			'Price session next',
		)

	pl_price_max = fields.Float(
			'Price max',
		)



# ---------------------------------------- Constraints Python - Name -------------------------

	# Check Name
	@api.constrains('name')
	def check_name(self):
		"""
		Check Name
		"""
		chk_product.check_name(self)


# ----------------------------------------------------------- Update ----------------------------------------------------
	#@api.multi
	#def update(self):
	#	"""
	#	Update
	#	"""
		#print()
		#print('Product Template - Update')
	#	self.pl_idx_int = int(self.pl_idx)
	#	self.purchase_ok = False





# ---------------------------------------------- Fields - Chars -----------------------------------

	pl_name_short = fields.Char(
			'Name short',
			required=True,
		)

	pl_prefix = fields.Char(
			'Prefix',
			#required=True,
		)

	pl_idx = fields.Char(
			'Idx',
			#required=True,
		)

	pl_code = fields.Char(
			'Code',
			#required=True,
		)

	pl_idx_int = fields.Integer(
			#'Idx I',
			'Indice',
			#required=True,
		)

	pl_account = fields.Char(
			'Cuenta contable',
			required=False,
		)

	pl_time_stamp = fields.Char(
			required=False,
		)

