# -*- coding: utf-8 -*-
"""
	First Contact - Object Oriented
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class FirstContact(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.first_contact'

	_description = 'Openhealth Marketing First Contact'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Line Analysis - PL -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		print()
		print('X - First Line - analyse')


		# First Contact 

		if line.first_contact == 'none': 
			self.none = self.none + 1

		elif line.first_contact == 'recommendation': 
			self.recommendation = self.recommendation + 1

		elif line.first_contact == 'tv': 
			self.tv = self.tv + 1



		elif line.first_contact == 'radio': 
			self.radio = self.radio + 1

		elif line.first_contact == 'internet': 
			self.internet = self.internet + 1

		elif line.first_contact == 'website':
			self.website = self.website + 1



		elif line.first_contact == 'mail_campaign':
			self.mail_campaign = self.mail_campaign + 1

		elif line.first_contact == 'facebook':
			self.facebook = self.facebook + 1

		elif line.first_contact == 'instagram':
			self.instagram = self.instagram + 1



		elif line.first_contact == 'callcenter':
			self.callcenter = self.callcenter + 1

		elif line.first_contact == 'old_patient':
			self.old_patient = self.old_patient + 1

		elif line.first_contact in [False, '']:
			self.undefined = self.undefined + 1

		else:
			print('Eror: This should not happen !')



# ----------------------------------------------------------- Get Counters -----------------------
	def get_counters(self):
		"""
		Get Counters
		"""
		print()
		print('X - Education - Get Counters')

		return self.none, self.recommendation, self.tv, self.radio, self.internet, self.website, self.mail_campaign, self.facebook,\
		self.instagram, self.callcenter, self.old_patient, self.undefined





# ----------------------------------------------------------- Fields ---------------------------------------------
	none = fields.Char()


	recommendation = fields.Integer(
			default=0,
		)

	old_patient = fields.Integer(
			default=0,
		)



	tv = fields.Integer(
			default=0,
		)

	radio = fields.Integer(
			default=0,
		)

	internet = fields.Integer(
			default=0,
		)


	website = fields.Integer(
			default=0,
		)

	mail_campaign = fields.Integer(
			default=0,
		)

	facebook = fields.Integer(
			default=0,
		)

	instagram = fields.Integer(
			default=0,
		)

	callcenter = fields.Integer(
			default=0,
		)

	undefined = fields.Integer(
			default=0,
		)

