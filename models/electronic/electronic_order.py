# -*- coding: utf-8 -*-
"""
 	Electronic Order - Sunat compatible
 	Created: 			15 Apr 2019
 	Last updated: 		22 Jun 2019

"""
from __future__ import print_function  # Only needed for Python 2
import io
from openerp import models, fields, api
from openerp.addons.openhealth.models.containers import lib_exp
#from . import lib_coeffs
from . import pl_lib_exp


class electronic_order(models.Model):
	"""
	high level support for doing this and that.
	"""

	_inherit = 'openhealth.electronic.order'


# ----------------------------------------------------------- Configurator ------------------------
	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			#string="Configuracion",
			#required=False,
		)



# ----------------------------------------------------------- Native -------------------------------
	content = fields.Text()

	path = fields.Char()

	file_name = fields.Char()

	# Id
	id_serial_nr = fields.Char(
			'Id Serial Nr',
		)


# ----------------------------------------------------------- Electronic - Create Content -------------------------------

	def pl_init(self, id_serial_nr, path, file_name):
		"""
		Used by Txt Generation
		From pl_export
		"""
		print()
		print('Pl - Init')
		#print(self)
		#print(id_serial_nr)
		#print(path)
		#print(file_name)

		self.id_serial_nr = id_serial_nr
		self.path = path
		self.file_name = file_name

		self.configurator = self.container_id.configurator



# ----------------------------------------------------------- Electronic - Create Content -------------------------------

	def pl_create_txt(self):
		"""
		Used by Txt Generation
		From pl_export
		"""
		print()
		print('Pl - Create Txt')


		# Content - This !!!
		self.content = pl_lib_exp.get_file_content(self)

		
		#print(self.content)



# ----------------------------------------------------------- Electronic - Create File ----------------------------

	def pl_create_file(self):
		"""
		Used by Txt Generation
		From pl_export
		"""
		print()
		print('Pl - Create File')


		# Create File
		fname = self.path + '/' + self.file_name + '.txt'

		f = io.open(fname, mode="w", encoding="utf-8")

		print(self.content, file=f)
		
		f.close()



		# Create Txt Ids
		print(self.container_id)
		self.container_id.txt_ids.create({
											'name': 			self.file_name,
											'content': 			self.content,

											'container_id': 	self.container_id.id,
			})



# ----------------------------------------------------------- Required ----------------------------
	# Patient
	id_doc_type = fields.Char(
			string='Doc Id Tipo',
			default=".",
			required=True,
		)

	id_doc_type_code = fields.Char(
			string='Codigo',
			default=".",
			required=True,
		)


	# Order
	x_type = fields.Char(
			'Tipo',
			required=True,
		)

	type_code = fields.Char(
			'Codigo',
			required=True,
		)

	serial_nr = fields.Char(
			'Serial Nr',
			required=True,
		)

	receptor = fields.Char(
			string='Receptor',
			required=True,
		)

# ----------------------------------------------------------- Electronic -------------------------------

	#def get_coeff(self):
	#	"""
	#	Used by Txt Generation
	#	From containers.lib_exp
	#	"""
	#	print()
	#	print('Pl - Get Coeff')
	#	coeff = lib_coeffs.get_coeff(self.state)
	#	return coeff

