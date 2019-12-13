# -*- coding: utf-8 -*-
"""
	Origin - Object Oriented
	
	For Marketing

	Created: 				12 Dec 2019
	Last up: 				13 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Origin(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.origin'

	_description = 'Openhealth Marketing Origin'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Static Methods -----------------------

	@staticmethod
	def get_sp_name(name):
		"""
		Used by Lib Marketing
		"""
		#print()
		#print('Get Sp Name')
		#print(name)

		_dic = {
					False: '', 

					'tv_two': 'TV-2',
					'tv_four': 'TV-4',
					'tv_nine': 'TV-9',

					'sn_facebook': 'Facebook',
					'sn_instagram': 'Instagram',
					'sn_youtube': 'Youtube',
					'sn_twitter': 'Twitter',

					'web_page': 'Página web',

					'other': 'Otros',
					'recommendation': 'Recomendación',

		}

		#print(_dic[name]

		return _dic[name]





# ----------------------------------------------------------- Class Vars -----------------------
	tv_two_str = 'tv_two'
	tv_four_str = 'tv_four'
	tv_nine_str = 'tv_nine'

# ----------------------------------------------------------- Line Analysis -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		#print()
		#print('X - Origin - analyse')


		#print(line.origin)


		# Origin

		#if line.origin == 'tv_two': 
		if line.origin == self.tv_two_str: 
			self.tv_two = self.tv_two + 1

		#elif line.origin == 'tv_four': 
		elif line.origin == self.tv_four_str: 
			self.tv_four = self.tv_four + 1

		#elif line.origin == 'tv_nine': 
		elif line.origin == self.tv_nine_str: 
			self.tv_nine = self.tv_nine + 1



		elif line.origin == 'sn_facebook': 
			self.sn_facebook = self.sn_facebook + 1

		elif line.origin == 'sn_instagram': 
			self.sn_instagram = self.sn_instagram + 1

		elif line.origin == 'sn_youtube': 
			self.sn_youtube = self.sn_youtube + 1

		elif line.origin == 'sn_twitter': 
			self.sn_twitter = self.sn_twitter + 1


		#elif line.origin == 'Página web/Buscador': 
		elif line.origin == 'web_page': 
			self.web_page = self.web_page + 1


		# Recomm
		#elif line.origin == 'Recomendación': 
		elif line.origin == 'recommendation': 
			self.recommendation = self.recommendation + 1


		# Other
		elif line.origin == 'other': 
			self.other = self.other + 1

		else:
			print('This Should not happen !')



# ----------------------------------------------------------- Get Counters -----------------------
	def get_counters(self):
		"""
		Get Counters
		"""
		#print()
		#print('X - Education - Get Counters')

		return self.tv_two, self.tv_four, self.tv_nine,\
		 		self.sn_facebook, self.sn_instagram, self.sn_youtube, self.sn_twitter,\
		 		self.web_page, self.recommendation, self.other



# ----------------------------------------------------------- Fields ---------------------------------------------

# Tv
	tv_two = fields.Integer(
			default=0,
			string='TV-2',
		)

	tv_four = fields.Integer(
			default=0,
			string='TV-4',
		)

	tv_nine = fields.Integer(
			default=0,
			string='TV-9',
		)



# Social networks
	sn_facebook = fields.Integer(
			default=0,
			string='Facebook',
		)

	sn_instagram = fields.Integer(
			default=0,
			string='Instagram',
		)

	sn_youtube = fields.Integer(
			default=0,
			string='Youtube',
		)

	sn_twitter = fields.Integer(
			default=0,
			string='Twitter',
		)


# Others

	# Web Page
	web_page = fields.Integer(
			default=0,
			string='Página Web',
		)


	# Recomm
	recommendation = fields.Integer(
			default=0,
			string='Recomendación',
		)

	# Other
	other = fields.Integer(
			default=0,
			string='Otros',
		)





# ----------------------------------------------------------- Get Counters -----------------------
	def get_counters(self):
		"""
		Get Counters
		"""
		print()
		print('X - Origin - Get Counters')








