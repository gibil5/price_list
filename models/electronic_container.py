# -*- coding: utf-8 -*-
"""
	Container

	Created: 				30 Sep 2018
	Last mod: 				 2 May 2019
"""
from __future__ import print_function
import base64
import io
import datetime
from openerp import models, fields, api
from openerp.addons.openhealth.models.management import mgt_funcs
from openerp.addons.openhealth.models.management import mgt_vars
from openerp.addons.openhealth.models.containers import export
from . import pl_export
from openerp import _
from openerp.exceptions import Warning as UserError

class ElectronicContainer(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'openhealth.container'




# ----------------------------------------------------------- Relational ------------------------
	# Electronic Order
	electronic_order_ids = fields.One2many(
			'openhealth.electronic.order',
			'container_id',
		)


# ----------------------------------------------------------- Configurator ------------------------
	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			#required=True,
			required=False,
		)





# ----------------------------------------------------------- Dates -----------
	# Dates
	export_date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
			required=True,
		)

	# Dates
	export_date_end = fields.Date(
			string="Fecha Final",
			default=fields.Date.today,
			required=True,
		)

	several_dates = fields.Boolean(
			'Varias Fechas',
		)

	vspace = fields.Char(
			' ',
		)


# ----------------------------------------------------------- Electronic -----------
	# Name
	name = fields.Char(
			'Nombre',
			default='Generador',
			required=True,
		)


	# State Array
	state_arr = fields.Selection(
			selection=mgt_vars._state_arr_list,
			string='State Array',
			default='sale,cancel,credit_note',
			required=True,
		)

	# Type Array
	type_arr = fields.Selection(
			selection=mgt_vars._type_arr_list,
			string='Type Array',
			default='ticket_receipt,ticket_invoice',
			required=True,
		)




# ----------------------------------------------------------- Export TXT ------------------------------
	@api.multi
	#def export_txt(self):
	def pl_export_txt(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Export - Txt')

		# Clean
		self.txt_ids.unlink()



		# Export - Here !
		#fname = export.export_txt(self, self.electronic_order_ids, self.export_date)
		fname = pl_export.pl_export_txt(self, self.electronic_order_ids, self.export_date)



		# Download file
		fname_txt = fname.split('/')[-1]

		# Read Binary
		f = io.open(fname, mode="rb")
		out = f.read()
		f.close()

		# Update
		self.write({
					'txt_pack': base64.b64encode(out),
					'txt_pack_name': fname_txt,
				})
	# export_txt






# ----------------------------------------------------------- Update Sales - Electronic -----------

	# Update Electronic
	@api.multi
	def update_electronic(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Update - Electronic')

		# Clean
		#self.electronic_order.unlink()
		self.electronic_order_ids.unlink()


		if not self.several_dates:
			self.export_date_end = self.export_date_begin


		# Orders
		#orders, count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)
		#orders, count = mgt_funcs.get_orders_filter(self, self.export_date_begin, self.export_date_begin, self.state_arr, self.type_arr)
		orders, count = mgt_funcs.get_orders_filter(self, self.export_date_begin, self.export_date_end, self.state_arr, self.type_arr)

		print(orders)
		print(count)


		# Init
		amount_total = 0
		receipt_count = 0
		invoice_count = 0

		# Loop
		for order in orders:
			#print order
			#print order.x_type

			# Generate Id Doc
			if order.x_type in ['ticket_invoice', 'invoice']:

				#receptor = order.patient.x_firm.upper()
				order.pl_receptor = order.patient.x_firm.upper()

				id_doc = order.patient.x_ruc
				id_doc_type = 'ruc'
				id_doc_type_code = '6'
			else:
				#receptor = order.patient.name
				order.pl_receptor = order.patient.name

				id_doc = order.patient.x_id_doc
				id_doc_type = order.patient.x_id_doc_type
				id_doc_type_code = order.patient.x_id_doc_type_code

			# Patch
			#if order.patient.x_id_doc == False and order.patient.x_id_doc_type == False:
			if not order.patient.x_id_doc and not order.patient.x_id_doc_type:
				if order.patient.x_dni != False:
					id_doc = order.patient.x_dni
					id_doc_type = 'dni'
					id_doc_type_code = 1


			#print(receptor)
			#print(order.pl_receptor)
			#print(id_doc)
			#print(id_doc_type)
			#print(id_doc_type_code)



			# Validate Patient - Id Doc
			error, msg = order.patient.validate()
			#print(error)
			#print(msg)
			if error in [1]:
				raise UserError(_(msg))
			print()


			# Validate Order - Type, Serial Nr and Receptor
			error, msg = order.validate_electronic()
			#print(error)
			#print(msg)
			if error in [1]:
				raise UserError(_(msg))
			print()


			# Create Electronic Order
			#electronic_order = self.electronic_order.create({
			electronic_order = self.electronic_order_ids.create({
																# Required
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,
																'x_type': 				order.x_type,
																'type_code': 			order.x_type_code,
																'serial_nr': 			order.x_serial_nr,
																#'receptor': 			receptor,
																'receptor': 			order.pl_receptor,


																'name': 				order.name,
																'patient': 				order.patient.id,

																'x_date_created': 		order.date_order,


																#'amount_total': 		order.amount_total,
																'amount_total_net': 	order.x_total_net,
																'amount_total_tax': 	order.x_total_tax,

																'amount_total': 		order.x_amount_flow,




																'doctor': 				order.x_doctor.id,
																'state': 				order.state,

																# Counter
																'counter_value': 		order.x_counter_value,
																'delta': 				order.x_delta,

																# Credit Note
																'credit_note_owner': 	order.x_credit_note_owner.id,
																'credit_note_type': 	order.x_credit_note_type,


																# Handles
																#'management_id': self.id,
																#'container_id': self.container.id,
																'container_id': self.id,
			})
			#print(electronic_order)
			#print(electronic_order.container_id)
			#print(electronic_order.name)



			# Create Lines
			for line in order.order_line:
				#print line
				#print line.product_id.name
				#print line.product_uom_qty
				#print line.price_unit
				#print electronic_order
				#print

				electronic_order.electronic_line_ids.create({
																					# Line
																					'product_id': 			line.product_id.id,
																					'product_uom_qty': 		line.product_uom_qty,
																					'price_unit': 			line.price_unit,

																					# Rel
																					'electronic_order_id': 	electronic_order.id,
					})



			# Update Amount Total
			#if order.state in ['sale', 'cancel']:
			if order.state in ['sale', 'cancel', 'credit_note']:


				# Total
				#amount_total = amount_total + order.amount_total
				amount_total = amount_total + order.x_amount_flow


				# Count
				if order.x_type in ['ticket_receipt']:
					receipt_count = receipt_count + 1
				elif order.x_type in ['ticket_invoice']:
					invoice_count = invoice_count + 1



		return amount_total, receipt_count, invoice_count

	# update_electronic



# ----------------------------------------------------------- Electronic --------------------------
	# Create Electronic
	@api.multi
	def pl_create_electronic(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Create - Electronic')

		# Clean
		self.electronic_order_ids.unlink()

		# Init Dates
		date_format = "%Y-%m-%d"
		date_dt = datetime.datetime.strptime(self.export_date_begin, date_format) + datetime.timedelta(hours=+5, minutes=0)
		self.export_date = date_dt.strftime(date_format).replace('-', '_')

		# Init
		self.state_arr = 'sale,cancel,credit_note'
		self.type_arr = 'ticket_receipt,ticket_invoice'

		# Create Electronic
		self.amount_total, self.receipt_count, self.invoice_count = self.update_electronic()

	# create_electronic





# ----------------------------------------------------------- Clean -----------------------------
	# Clear
	@api.multi
	def clear(self):
		"""
		Cleans all variables.
		"""

		#self.txt_pack.unlink()
		self.txt_pack = False

		# Electronic
		self.electronic_order_ids.unlink()
		# Txt
		self.txt_ids.unlink()
		# Stats
		self.amount_total = 0
		self.invoice_count = 0
		self.receipt_count = 0
	# clear
