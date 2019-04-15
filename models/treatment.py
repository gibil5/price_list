# -*- coding: utf-8 -*-
"""
 		*** Treatment

 		Created: 			26 Aug 2016
 		Last up: 	 		21 Jan 2019
"""
from __future__ import print_function

from openerp import models, fields, api

from . import reco_funcs



class Treatment(models.Model):

	_inherit = 'openhealth.treatment'



	# gyn
	@api.multi
	def create_service_gyn(self):

		ret = reco_funcs.create_service_gyn(self)
		
		return ret



	# echo
	@api.multi
	def create_service_echo(self):
		
		ret = reco_funcs.create_service_echo(self)
		
		return ret


	# promo
	@api.multi
	def create_service_promo(self):
		
		ret = reco_funcs.create_service_promo(self)
		
		return ret


