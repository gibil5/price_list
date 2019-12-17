# -*- coding: utf-8 -*-
"""
	Patient Line - Object Oriented

	Only functions. Not the data model. 

	Created: 				16 May 2018
	Last up: 				14 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import eval_vars
from openerp.addons.openhealth.models.product import prodvars

from openerp.addons.price_list.models.patient.patient import Patient


class PatientLine(models.Model):
	"""
	Used by Marketing - Update Patients
	"""
	_inherit = 'openhealth.patient.line'

	_order = 'date_create asc'



# ----------------------------------------------------------- Counter Update ------------------------------------------------------

	def counters_update(self, line):
		"""
		New - 2019
		This is just counter update
		Analyses Line to update counters
		"""
		#print()
		#print('X - Macro Line Analysis')


		# Patient Line Macros	

		# Init
		qty = line.product_uom_qty


		# Doctor
		if self.doctor.name in [False]:
			self.doctor = line.doctor



	# Family Analysis


		# Increase Sales
		if line.state in ['sale']:

			# Consultation
			if line.family in ['consultation']:
				self.inc_nr_consultation(qty)

			# Procedure
			elif line.family in ['procedure']:
				self.inc_nr_procedure(qty)
				
				# All
				self.add_procedure_treatment(line.product_id)
				self.add_procedure_pathology(line.product_id)
				self.add_procedure_zone(line.product_id)

			# Product
			elif line.family in ['product']:
				self.inc_nr_product(qty)

			# Increase Sales
			self.inc_nr_sale(qty)



		# Increase Drafts
		elif line.state in ['draft']:
			self.inc_nr_draft(qty)
















# ----------------------------------------------------------- Update Fields Vip ------------------------------------------------------
	# Update fields Vip
	@api.multi
	def update_fields_vip(self):  
		#print()
		#print('X - Update fields - Vip')


		# Nr Lines Vip 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_id_vip','=', self.id),
																			]) 
		self.nr_lines_vip = count

	# update_fields_vip










# ----------------------------------------------------------- Relational ------------------------------------------------------
	# Marketing Id 
	marketing_id = fields.Many2one(
			'openhealth.marketing',
			ondelete='cascade', 
		)

	# Sales
	pl_sale_line = fields.One2many(
			'price_list.marketing.order_line',
			'patient_line_id',
		)




# ----------------------------------------------------------- Origin ------------------------------------------------------
	# Origin 
	origin = fields.Char(
			string = 'Origen',
		)


# ----------------------------------------------------------- Natives - Required ------------------------------------------------------

	# Date
	date_record = fields.Datetime(
			string="Fecha de Registro",
			required=True,
		)

	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Paciente", 
			required=True,
		)

	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)


	# Contact
	phone_1 = fields.Char(
			'Tel 1', 
			#required=True,
			required=False,
		)

	phone_2 = fields.Char(
			'Tel 2', 
			#required=True,
			required=False,
		)

	email = fields.Char(
			'Email', 
			#required=True,
			required=False,
		)


	# EMR
	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 						
			selection = eval_vars._chief_complaint_list, 
			#required=True,
		)

	diagnosis = fields.Char(
			'Diagnóstico', 
			#required=True,
		)


	# Demographics
	age_years = fields.Integer(
			string = "Edad", 		
			#default=-1, 
			required=True,
		)

	dob = fields.Date(
			string="Fecha nacimiento",
			required=True,
		)



	# Sex 
	sex = fields.Selection(

			selection = Patient._sex_type_list,

			string="Sexo",
			required=False,
		)

	

	# Education 
	education = fields.Selection(

			selection = Patient._education_level_type,

			string = 'Grado de instrucción',
			required=False,
		)

	# Function
	function = fields.Char(
			'Ocupación', 
			#required=True,
			required=False,
		)


	
	# Location
	city = fields.Char(
			'Ciudad', 
			required=True,
		)

	district = fields.Char(
			'Distrito', 
			#required=True,
			required=False,
		)









# ----------------------------------------------------------- Setters ------------------------------------------------------
	def set_vip(self, value):
		self.vip = value
		# Parent
		self.marketing_id.vip_true = self.marketing_id.vip_true + 1


# ----------------------------------------------------------- Incs ------------------------------------------------------
	def inc_nr_sale(self, qty):
		"""
		Used by Pat Line Funcs - Macro line analysis
		"""
		self.nr_sale = self.nr_sale + qty


	def inc_nr_draft(self, qty):
		"""
		Used by Pat Line Funcs - Macro line analysis
		"""
		self.nr_budget = self.nr_budget + qty


	def inc_nr_consultation(self, qty):
		"""
		Used by Pat Line Funcs - Macro line analysis
		"""
		self.nr_consu = self.nr_consu + qty


	def inc_nr_procedure(self, qty):
		"""
		Used by Pat Line Funcs - Macro line analysis
		"""
		self.nr_proc = self.nr_proc + qty


	def inc_nr_product(self, qty):
		"""
		Used by Pat Line Funcs - Macro line analysis
		"""
		self.nr_products = self.nr_products + qty




# ----------------------------------------------------------- Adds ------------------------------------------------------

	# Add procedure treatment
	def add_procedure_treatment(self, product):
		"""
		Used by Pat Line Funcs - Macro line analysis
		"""

		# All PL
		treatment = product.get_treatment()

		if treatment != self.proc_treatment:	
			if self.proc_treatment in [False]:
				self.proc_treatment = treatment
			else:	
				self.proc_treatment = self.proc_treatment + ', ' + treatment




	# Add procedure patho
	def add_procedure_pathology(self, product):
		"""
		Used by Pat Line Funcs - Macro line analysis
		"""

		# All PL
		pathology = product.get_pathology()

		if pathology != self.proc_pathology:	
			if self.proc_pathology in [False]:
				self.proc_pathology = pathology
			else:
				self.proc_pathology = self.proc_pathology + ', ' + pathology



	# Add procedure zone
	def add_procedure_zone(self, product):
		"""
		Used by Pat Line Funcs - Macro line analysis
		"""

		# All PL
		zone = product.get_zone()

		if zone != self.proc_zone:	
			if self.proc_zone in [False]:
				self.proc_zone = zone
			else:
				self.proc_zone = self.proc_zone + ', ' + zone





# ----------------------------------------------------------- Clean ------------------------------------------------------

	# Clean
	def clean(self):  
		#print()
		#print('Clean')

		# Dep
		#self.sl_nr_sale = 0
		#self.sl_nr_consu = 0
		#self.sl_nr_products = 0
		#self.sl_nr_proc = 0
		#self.sl_nr_budget = 0


		self.nr_sale = 0
		self.nr_consu = 0
		self.nr_products = 0
		self.nr_proc = 0
		self.nr_budget = 0

		self.proc_treatment = False
		self.proc_pathology = False
		self.proc_zone = False




# ----------------------------------------------------------- Natives ------------------------------------------------------

	# Nr Sales
	sl_nr_sale = fields.Integer(
			'SL Nr Ventas',
		)

	# Nr Consultations
	sl_nr_consu = fields.Integer(
			'SL Nr Consultas',
		)

	# Nr Products
	sl_nr_products = fields.Integer(
			'SL Nr Productos',
		)

	# Nr Procedures
	sl_nr_proc = fields.Integer(
			'SL Nr Procedimientos',
		)

	# Nr Budgets
	sl_nr_budget = fields.Integer(
			'SL Nr Presupuestos',
		)



# ----------------------------------------------------------- Natives ------------------------------------------------------

	# Nr Sales
	nr_sale = fields.Integer(
			'Nr Ventas',
		)

	# Nr Consultations
	nr_consu = fields.Integer(
			'Nr Consultas',
		)

	# Nr Products
	nr_products = fields.Integer(
			'Nr Productos',
		)

	# Nr Procedures
	nr_proc = fields.Integer(
			'Nr Procedimientos',
		)

	# Nr Budgets
	nr_budget = fields.Integer(
			'Nr Presupuestos pendientes',
		)


	# Procs
	proc_treatment = fields.Char(
			'Proc Tratamiento',
		)

	proc_pathology = fields.Char(
			'Proc Patologia',
		)

	proc_zone = fields.Char(
			'Proc Zona',
		)


