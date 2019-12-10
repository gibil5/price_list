# -*- coding: utf-8 -*-
#
# 	Patient Line
# 
# 	Created: 				16 May 2018
#
from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import eval_vars

from openerp.addons.openhealth.models.product import prodvars

from openerp.addons.openhealth.models.patient import pat_vars
from . import mkt_funcs

class PatientLine(models.Model):

	_inherit = 'openhealth.patient.line'

	_order = 'date_create asc'




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
			selection = pat_vars._sex_type_list,
			string="Sexo",
			#required=True,
			required=False,
		)

	

	# Education 
	education = fields.Selection(
			selection = pat_vars._education_level_type,
			string = 'Grado de instrucción',
			#required=True,
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


	# Sales - Dep !
	sale_line = fields.One2many(
			'openhealth.marketing.order.line',
			'patient_line_sale_id',
		)



# ----------------------------------------------------------- Analysis ------------------------------------------------------

	def analysis(self, line):

		mkt_funcs.macro_line_analysis(self, line)		# LIB

		# Update sale line
		line.set_patient_line_id(self.id)



# ----------------------------------------------------------- Setters ------------------------------------------------------

	#def add_procedure_treatment(self, treatment):
	def add_procedure_treatment(self, product):

		# All Price Lists
		#if product.pl_price_list in ['2019']:
		#	treatment = product.pl_treatment
		#else:
		#	treatment = product.x_treatment


		# All PL
		treatment = product.get_treatment()

		if treatment != self.proc_treatment:	
			if self.proc_treatment in [False]:
				self.proc_treatment = treatment
			else:	
				self.proc_treatment = self.proc_treatment + ', ' + treatment




	#def add_procedure_pathology(self, pathology):
	def add_procedure_pathology(self, product):

		# All Price Lists
		#if product.pl_price_list in ['2019']:
		#	pathology = product.pl_pathology
		#else:
		#	pathology = product.x_pathology


		# All PL
		pathology = product.get_pathology()

		if pathology != self.proc_pathology:	
			if self.proc_pathology in [False]:
				self.proc_pathology = pathology
			else:
				self.proc_pathology = self.proc_pathology + ', ' + pathology


	#def add_procedure_zone(self, zone):
	def add_procedure_zone(self, product):

		# All Price Lists
		#if product.pl_price_list in ['2019']:
		#	zone = product.pl_zone
		#else:
		#	zone = product.x_zone


		# All PL
		zone = product.get_zone()

		if zone != self.proc_zone:	
			if self.proc_zone in [False]:
				self.proc_zone = zone
			else:
				self.proc_zone = self.proc_zone + ', ' + zone





	def set_vip(self, value):
		self.vip = value
		# Parent
		self.marketing_id.vip_true = self.marketing_id.vip_true + 1


# ----------------------------------------------------------- Incs ------------------------------------------------------

	def inc_nr_sale(self, qty):
		#self.sl_nr_sale = self.sl_nr_sale + qty
		self.nr_sale = self.nr_sale + qty


	def inc_nr_draft(self, qty):
		#self.sl_nr_budget = self.sl_nr_budget + qty
		self.nr_budget = self.nr_budget + qty




	def inc_nr_consultation(self, qty):
		#self.sl_nr_consu = self.sl_nr_consu + qty
		self.nr_consu = self.nr_consu + qty


	def inc_nr_procedure(self, qty):
		#self.sl_nr_proc = self.sl_nr_proc + qty
		self.nr_proc = self.nr_proc + qty


	def inc_nr_product(self, qty):
		#self.sl_nr_products = self.sl_nr_products + qty
		self.nr_products = self.nr_products + qty









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








# ----------------------------------------------------------- Natives ------------------------------------------------------

	proc_treatment = fields.Char(
			'Proc Tratamiento',
		)

	proc_pathology = fields.Char(
			'Proc Patologia',
		)

	proc_zone = fields.Char(
			'Proc Zona',
		)


	#proc_zone = fields.Char(
	#		'Proc Zona',
	#	)




# ----------------------------------------------------------- Update Fields Proc - Deprecated ! ------------------------------------------------------

	# Update fields Proc
	@api.multi
	def update_nrs(self):  
		#print()
		#print('Pl - Update Nrs')
		#print 


		# Sales 
		for line in self.sale_line: 
			# Doctor 
			if self.doctor.name == False: 
				self.doctor = line.doctor.id 



		# Budgets
		self.budget_amount = ''
		self.budget_prod = ''
		for line in self.budget_line: 


			# Doctor 
			if self.doctor.name == False: 
				self.doctor = line.doctor.id 



		
			# Budget Amount 
			self.budget_amount = self.budget_amount + str(line.price_total) + ', '

			# Budget Flag 
			if line.price_total >= 1500: 
				self.budget_flag = True



			# Budget Prod
			if line.product_id.x_treatment != False: 
				if line.product_id.x_treatment in prodvars._h_subfamily: 
					self.budget_prod = self.budget_prod + prodvars._h_subfamily[line.product_id.x_treatment] + ', '
				else: 
					self.budget_prod = self.budget_prod + line.product_id.x_treatment + ', '




		# Amount and Prod 
		self.budget_amount = self.budget_amount[:-2]
		self.budget_prod = self.budget_prod[:-2]




		# Nr Budgets
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_budget_id','=', self.id),
																			]) 
		self.nr_budget = count




		# Nr Sale
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_sale_id','=', self.id),
																			]) 
		self.nr_sale = count




		# Nr Consultations
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_consu_id','=', self.id),
																			]) 
		self.nr_consu = count




		# Nr Product - Dep
		#count = self.env['openhealth.marketing.order.line'].search_count([
		#																		('patient_line_product_id','=', self.id),
		#																	]) 
		#self.nr_products = count





		# Nr Proc 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_proc_id','=', self.id),
																			]) 
		self.nr_proc = count





		# Nr Reco 
		count = self.env['openhealth.marketing.recom.line'].search_count([
																				('patient_line_id','=', self.id),
																			]) 
		self.nr_reco = count

	# update_nrs



# ----------------------------------------------------------- Update ------------------------------------------------------

	def update_emr(self):
		#print()
		#print('Update EMR')

		self.treatment = self.env['openhealth.treatment'].search([
																	('patient','=', self.patient.name),
														],
														order='start_date desc',
														limit=1,)

		self.consultation = self.env['openhealth.consultation'].search([
																		('treatment','=', self.treatment.id),
														],
														order='evaluation_start_date desc',
														limit=1,)

		self.chief_complaint = self.treatment.chief_complaint

		self.diagnosis = self.consultation.x_diagnosis

