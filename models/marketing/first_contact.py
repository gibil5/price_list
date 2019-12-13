# -*- coding: utf-8 -*-
"""
	First Contact - Object Oriented
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

import mkt_funcs

class FirstContact(models.Model):
	"""
	Used by Marketing
	"""
	_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.first_contact'

	_description = 'Openhealth Marketing First Contact'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Update First Contact ---------------------------------------------
	def update_per(self, mkt):
		"""
		Update First Contact
		Extract BL from Structure
		"""
		#print()
		#print('X - First Contact')

		mkt.how_none_per = mkt_funcs.get_per(mkt.how_none, mkt.total_count)
		mkt.how_reco_per = mkt_funcs.get_per(mkt.how_reco, mkt.total_count)
		mkt.how_tv_per = mkt_funcs.get_per(mkt.how_tv, mkt.total_count)
		mkt.how_radio_per = mkt_funcs.get_per(mkt.how_radio, mkt.total_count)
		mkt.how_inter_per = mkt_funcs.get_per(mkt.how_inter, mkt.total_count)
		mkt.how_web_per = mkt_funcs.get_per(mkt.how_web, mkt.total_count)
		mkt.how_mail_per = mkt_funcs.get_per(mkt.how_mail, mkt.total_count)
		mkt.how_u_per = mkt_funcs.get_per(mkt.how_u, mkt.total_count)
		mkt.how_facebook_per = mkt_funcs.get_per(mkt.how_facebook, mkt.total_count)
		mkt.how_instagram_per = mkt_funcs.get_per(mkt.how_instagram, mkt.total_count)
		mkt.how_callcenter_per = mkt_funcs.get_per(mkt.how_callcenter, mkt.total_count)
		mkt.how_old_patient_per = mkt_funcs.get_per(mkt.how_old_patient, mkt.total_count)



# ----------------------------------------------------------- Line Analysis - PL -----------------------
	def analyse(self, line):
		"""
		Patient Line Analysis to update counters
		"""
		#print()
		#print('X - First Line - analyse')


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
		#print()
		#print('X - Education - Get Counters')

		return self.none, self.recommendation, self.tv, self.radio, self.internet, self.website, self.mail_campaign, self.facebook,\
		self.instagram, self.callcenter, self.old_patient, self.undefined





# ----------------------------------------------------------- Fields ---------------------------------------------
	none = fields.Char(
			default=0,
			string='Ninguno',
		)


	recommendation = fields.Integer(
			default=0,
			string='Recomendación',
		)

	old_patient = fields.Integer(
			default=0,
			string='Paciente Antiguo',
		)



	tv = fields.Integer(
			default=0,
			string='TV',
		)

	radio = fields.Integer(
			default=0,
			string='Radio',
		)

	internet = fields.Integer(
			default=0,
			string='Internet',
		)


	website = fields.Integer(
			default=0,
			string='Sitio Web',
		)

	mail_campaign = fields.Integer(
			default=0,
			string='Campaña Mail',
		)

	facebook = fields.Integer(
			default=0,
			string='Facebook',
		)

	instagram = fields.Integer(
			default=0,
			string='Instagram',
		)

	callcenter = fields.Integer(
			default=0,
			string='Call Center',
		)

	undefined = fields.Integer(
			default=0,
			string='Indefinido',
		)

