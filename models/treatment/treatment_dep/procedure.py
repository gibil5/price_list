# -*- coding: utf-8 -*-
"""
	*** Procedure - Dep - 10 Augo 2020

	Created: 				 1 Nov 2016
	Last updated: 	 	 	26 Sep 2019
"""
from openerp import models, fields, api
from . import pro_con_funcs
from . import pro_ses_funcs

class Procedure(models.Model):
	"""
	Procedure Class. Used by Treatment.
	"""
	_inherit = 'openhealth.procedure'

	_description = 'Procedure'


# ----------------------------------------------------------- Create Control Man -------------------------
	# Create Controls Manual
	#@api.multi	
	#def create_controls_manual(self):
	#	print()
	#	print('Pl - Create Controls Manual')
	#	nr_controls = 1
	#	nr_ctl_created = self.env['openhealth.control'].search_count([
	#																	('procedure','=', self.id), 
	#																]) 
		# Create
	#	ret = pro_con_funcs.create_controls(self, nr_controls, nr_ctl_created)



# ----------------------------------------------------------- Create Session Man -------------------------
	# Create Sessions Manual
	#@api.multi	
	#def create_sessions_manual(self):
	#	print()
	#	print('Pl - Create Sessions Manual')

	#	nr_sessions = 1

	#	nr_ses_created = self.env['openhealth.session.med'].search_count([
	#																		('procedure', '=', self.id), 
	#																])

		# Create
	#	ret = pro_ses_funcs.create_sessions(self, nr_sessions, nr_ses_created)




	
# ---------------------------------------------- Fields ------------------------------------------
	# Laser
	#pl_laser = fields.Char(		
	#		string="Pl Láser",
	#		compute='_compute_pl_laser',
	#	)

	#@api.multi
	#@api.depends('product')
	#def _compute_pl_laser(self):
	#	for record in self:
	#		record.pl_laser = record.product.pl_treatment

