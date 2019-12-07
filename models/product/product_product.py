# -*- coding: utf-8 -*-
"""
		*** Product Product
 
		Created: 			 9 Apr 2019
		Last up: 	 		27 Sep 2019

	- Respect the Law of Demeter. Avoid Train Wrecks.
"""
from __future__ import print_function
from openerp import models, fields, api

class ProductProduct(models.Model):
	"""
	Product Product. Used by Order Line
	"""
	_inherit = 'product.product'

	_order = 'pl_idx'



# ----------------------------------------------------------- IS Funcs -------------------------
	def is_product(self):
		"""
		Test if it is a Product
		Used by: PL - Report Sale Product (Reporte de Ventas)
		"""

		is_product = False


		# Only 2019 is covered 
		if self.pl_price_list in ['2019']:


			if self.pl_family in ['topical', 'card', 'kit']:   		# LOD compliant !

				is_product = True

			else:				
				is_product = False

		else:
			print('Error: This should not happen !')


		return is_product



# ----------------------------------------------------------- IS Funcs -------------------------

	def is_procedure(self):
		"""
		Test if it is a procedure
		Used by: PL - Treatment
		"""

		is_procedure = False


		# 2019
		if self.pl_price_list in ['2019']:

			if self.pl_family in  ['laser', 'medical', 'cosmetology', 'echography', 'gynecology', 'promotion']:

				is_procedure = True

			else:				
				is_procedure = False

		else:
			print('Error: This should not happen !')


		return is_procedure


# ----------------------------------------------------------- Getters -------------------------

	#@api.multi
	def get_product_template(self):
		"""
		Get Product Template
		Used by: PL Creates.
		"""

		product_template = False

		# 2019
		if self.pl_price_list in ['2019']:

			# Search
			product_template = self.env['product.template'].search([
																		('name', '=', self.name),
																		('pl_price_list', 'in', ['2019']),
													],
														#order='create_date desc',
														limit=1,
													)

		# 2019
		elif self.pl_price_list in ['2018']:

			# Search
			product_template = self.env['product.template'].search([
																		('name', '=', self.name),
																		('pl_price_list', 'in', ['2018']),
													],
														#order='create_date desc',
														limit=1,
													)

		else:
			print('Error: This should not happen !')


		return product_template




# ----------------------------------------------------------- Getters -------------------------

	#@api.multi
	def get_family(self):
		"""
		Get Product Family
		Used by: Order.
		"""

		family = False


		# 2019
		if self.pl_price_list in ['2019']:

			family = self.pl_family


		# 2018
		elif self.pl_price_list in ['2018']:

			family = self.x_family


		# No price list
		else:
			print('Error: This should not happen')


		return family




# ----------------------------------------------------------- Is Current Price List -------------------------------

	def is_current_price_list(self):
		#print()
		#print('Product - Is Current Price List')

		if self.pl_price_list in ['2019']:					# Respects the LOD
			is_current = True

		else:		
			is_current = False

		return is_current




# ---------------------------------------------- Getters - Used by Marketing -----------------------------------

	# Sub sub family
	def get_subsubfamily(self):
		"""
		Contains all Business Logic
		Do not access class variables directly
		Used by Create Sale Lines
		"""

		_dic = {
					'consultation':		'consultation',

					'co2':		'laser_co2',
					'excilite':	'laser_excilite',
					'm22':		'laser_m22',
					'quick':	'laser_quick',


					'medical':		'medical',

					'botox':			'botox',
					'cryosurgery':		'cryosurgery',
					'hyaluronic_acid':	'hyaluronic_acid',

					'infiltrations':		'infiltrations',
					'mesotherapy':			'mesotherapy',
					'plasma':				'plasma',


					'REDUX':					'REDUX',
					'redux':					'redux',

					'sclerotherapy':			'sclerotherapy',
					'vitamin_c_intravenous':	'vitamin_c_intravenous',




					'cosmetology':		'cosmetology',
					#'LASER TRIACTIVE + CARBOXITERAPIA':		'LASER TRIACTIVE + CARBOXITERAPIA',
					#'CARBOXITERAPIA':		'CARBOXITERAPIA',
					#'PUNTA DE DIAMANTES':		'PUNTA DE DIAMANTES',
					'carboxytherapy': 	'carboxytherapy',
					'diamond_tip':		'diamond_tip',					
					'laser_triactive_carboxytherapy':		'laser_triactive_carboxytherapy',					



					'promotion':		'promotion',
					'echography':		'echography',
					'gynecology':		'gynecology',


					'commercial':		'commercial',
					'chavarri':			'chavarri',

					'other':			'other',
					'commission':		'commission',



					# 2018
					#'laser_ipl': 		'laser_ipl',
					#'laser_ndyag':		'laser_ndyag',

					#'carboxytherapy': 	'carboxytherapy',
					#'botulinum_toxin':	'botulinum_toxin',
					#'diamond_tip':		'diamond_tip',					
					#'criosurgery':		'criosurgery',
					#'intravenous_vitamin':		'intravenous_vitamin',

					#'x':		'x',

					#'diamond_tip':		'diamond_tip',

		}


		# 2019
		if self.pl_price_list in ['2019']:

			#if self.pl_subfamily in ['medical', 'cosmetology']:
			if self.pl_subfamily in ['medical']:
				#subsubfamily = _dic[self.pl_subfamily]
				subsubfamily = _dic[self.pl_treatment]

			else:
				subsubfamily = _dic[self.pl_subfamily]



		# Other
		else:
			subsubfamily = self.x_treatment



		return subsubfamily





# ---------------------------------------------- Getters - Important ! -----------------------------------
	# Treatment
	def get_treatment(self):
		"""
		Contains all Business Logic
		Do not access class variables directly
		"""

		# 2019
		if self.pl_price_list in ['2019']:
			treatment = self.pl_treatment
		# Other
		else:
			treatment = self.x_treatment

		return treatment



	# Pathology
	def get_pathology(self):
		"""
		Contains all Business Logic
		Do not access class variables directly
		"""

		# 2019
		if self.pl_price_list in ['2019']:
			pathology = self.pl_pathology
		# Other
		else:
			pathology = self.x_pathology

		return pathology



	# Zone
	def get_zone(self):
		"""
		Contains all Business Logic
		Do not access class variables directly
		"""

		# 2019
		if self.pl_price_list in ['2019']:
			zone = self.pl_zone
		# Other
		else:
			zone = self.x_zone

		return zone		




# ----------------------------------------------------------- Print Ticket -------------------------------

	def get_name_ticket(self):
		"""
		Used by Print Ticket.
		"""
		#return self.x_name_ticket
		return self.pl_name_short

