# -*- coding: utf-8 -*-
"""
 	Closing

	Created: 			18 Oct 2017
	Last up: 	 		 6 Feb 2019
"""
from __future__ import print_function
from openerp import models, fields, api
#from . import clos_funcs
#from . import ord_vars
from openerp.addons.openhealth.models.order import clos_funcs
from . import pl_clos_funcs

class Closing(models.Model):
	"""
	Native class.
	Encapsulates Odoo services.
	"""
	_inherit = 'openhealth.closing'




# ----------------------------------------------------------- Natives -----------------------
	total_banks = fields.Float(
			'Total Bancos',
		)


	bbva_tot = fields.Float(
			'BBVA',
		)

	interbank_tot = fields.Float(
			'Interbank',
		)

	scotiabank_tot = fields.Float(
			'Scotiabank',
		)

	bcp_tot = fields.Float(
			'BCP',
		)


# ----------------------------------------------------------- Update Totals -----------------------
	# Update Totals
	@api.multi
	#def update_totals(self):
	def update_totals(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Update Totals')


		# Proof
		clos_funcs.set_proof_totals(self)


		# Form
		#clos_funcs.set_form_totals(self)
		pl_clos_funcs.pl_set_form_totals(self)


		# All
		clos_funcs.set_totals(self)



		# Totals
		#self.total_form = self.cash_tot + self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot
		self.total_form = self.cash_tot + self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot + \
							self.bbva_tot + self.interbank_tot + self.scotiabank_tot + self.bcp_tot

		self.total_form_wblack = self.total_proof_wblack
		self.cash_tot_wblack = self.cash_tot - (self.total_form - self.total_form_wblack)

		# Subtotals
		self.total_cards = self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot
		self.total_cash = self.cash_tot

		self.total_banks = self.bbva_tot + self.interbank_tot + self.scotiabank_tot + self.bcp_tot



	# update_totals

