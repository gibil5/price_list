# -*- coding: utf-8 -*-
"""
		*** Product Product
 
		Created: 			 9 Apr 2019
		Last up: 	 		 3 Jul 2019
"""
from openerp import models, fields, api

class ProductProduct(models.Model):

	_inherit = 'product.product'

	_order = 'pl_idx'




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
					'cosmetology':		'cosmetology',

					'promotion':		'promotion',
					'echography':		'echography',
					'gynecology':		'gynecology',


					'commercial':		'commercial',
					'chavarri':			'chavarri',


					# 2018
					#'laser_ipl': 		'laser_ipl',
					#'laser_ndyag':		'laser_ndyag',

					#'carboxytherapy': 	'carboxytherapy',
					#'botulinum_toxin':	'botulinum_toxin',
					#'diamond_tip':		'diamond_tip',					
					#'criosurgery':		'criosurgery',
					#'intravenous_vitamin':		'intravenous_vitamin',

					#'x':		'x',
					#'other':		'other',

					#'diamond_tip':		'diamond_tip',

		}


		# 2019
		if self.pl_price_list in ['2019']:

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

