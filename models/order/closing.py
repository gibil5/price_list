# -*- coding: utf-8 -*-
"""
 	Closing - 1st Level

	Created: 			18 Oct 2017
	Last up: 	 		30 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

from . import clos_funcs
from . import pl_clos_funcs


class Closing(models.Model):
	"""
	Native class.
	Encapsulates Odoo services.
	"""
	_inherit = 'openhealth.closing'




# ----------------------------------------------------- Relational - Counters ------------------------------------------------------------------

	# Closing Form
	closing_form = fields.Many2one(

			'openhealth.closing.form', 

		)





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
	def update_totals(self):
		"""
		Update Closing - Cierre de Caja
		Proof - Documentos de pago
		Form - Formas de pago
		"""
		print()
		print('2019 - Update Totals')



		# Proof Totals
		clos_funcs.set_proof_totals(self)




# Form Totals - Uses Closing Form

		# Create Closing Form
		self.closing_form = self.env["openhealth.closing.form"].create({
																			'name': 'Closing Form',
																			'date': self.date,
																	})
		# Analise
		self.closing_form.analyse()


		# Get Totals
		self.cash_tot, self.ame_tot, self.din_tot, 	self.mac_tot, self.mad_tot, self.vic_tot, self.vid_tot, \
			self.bbva_tot, self.interbank_tot, self.scotiabank_tot, self.bcp = self.closing_form.get_totals()





# All Totals
		clos_funcs.set_totals(self)




		# Totals - Form
		self.total_form = self.cash_tot + self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot + \
							self.bbva_tot + self.interbank_tot + self.scotiabank_tot + self.bcp_tot

		self.total_form_wblack = self.total_proof_wblack
		self.cash_tot_wblack = self.cash_tot - (self.total_form - self.total_form_wblack)




		# Subtotals
		self.total_cash = self.cash_tot

		self.total_cards = self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot

		self.total_banks = self.bbva_tot + self.interbank_tot + self.scotiabank_tot + self.bcp_tot

	# update_totals




# ----------------------------------------------------------- Update ------------------------------
	# Update
	@api.multi
	def update(self):
		"""
		Build the Closing (Cierre de Caja). 
		For a given day.
		"""
		print()
		print('2019 - Update')

		self.update_totals()



# ----------------------------------------------------------- Reset ------------------------------
	@api.multi
	def reset(self):
		"""
		Reset
		"""
		print()
		print('2019 - Reset')

		self.total = 0
		self.total_cash = 0
		self.total_banks = 0


		self.total_proof = 0
		self.total_form = 0


		self.cash_tot = 0
		self.serial_nr_first_crn = ''
		self.serial_nr_last_crn = ''




