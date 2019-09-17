# -*- coding: utf-8 -*-
"""
	Procedure 	

	Created: 				 1 Nov 2016
	Last updated: 	 	 	25 Apr 2019
"""
from openerp import models, fields, api

#from . import px_vars		# Dep

from . import pro_con_funcs

from . import pro_ses_funcs

class Procedure(models.Model):
	"""
	Procedure Class.
	Used by Treatment.
	"""
	_inherit = 'openhealth.procedure'

	_description = 'Procedure'




# ----------------------------------------------------------- Create Session Man -------------------------
	# Create Sessions Manual
	@api.multi	
	def create_sessions_manual(self):
		print()
		print('Pl - Create Sessions Manual')

		nr_sessions = 1

		nr_ses_created = self.env['openhealth.session.med'].search_count([
																			('procedure', '=', self.id), 
																	])

		# Create
		ret = pro_ses_funcs.create_sessions(self, nr_sessions, nr_ses_created)




# ----------------------------------------------------------- Create Control Man -------------------------
	# Create Controls Manual
	@api.multi	
	def create_controls_manual(self):
		print()
		print('Pl - Create Controls Manual')
		
		nr_controls = 1

		nr_ctl_created = self.env['openhealth.control'].search_count([
																		('procedure','=', self.id), 
																	]) 

		# Create
		ret = pro_con_funcs.create_controls(self, nr_controls, nr_ctl_created)



	





# ---------------------------------------------- Fields ------------------------------------------
	# Laser
	#laser = fields.Selection(
	#pl_laser = fields.Selection(
	pl_laser = fields.Char(

			#selection=prodvars._laser_type_list,
			#selection=px_vars._treatment_list,  			# Dep
		
			string="Pl Láser",

			#compute='_compute_laser',
			compute='_compute_pl_laser',
		)

	#@api.multi
	@api.depends('product')
	#def _compute_laser(self):
	def _compute_pl_laser(self):
		for record in self:

			#record.laser = record.product.x_treatment
			record.pl_laser = record.product.pl_treatment







