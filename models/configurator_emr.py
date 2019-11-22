# -*- coding: utf-8 -*-
"""
Configurator - EMR

Created: 			25 Jan 2019
Last updated: 		29 Aug 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class ConfiguratorEmr(models.Model):
	"""
	Extends the Business Rules
	Should not contain Data Model.
	"""
	_inherit = 'openhealth.configurator.emr'




# ----------------------------------------------------------- Get Inactive Days -------------------------------
	def get_inactive_days(self):
		"""
		Gets Inactive Days. From Configurator.
		LOD friendly.
		"""
		print()
		print('Configurator - Get Inactive Days')
		days_inactive = []
		if self.name not in [False]:		
			for day in self.day_line:								# Respects the LOD
				if day.holiday:
					days_inactive.append(day.date)
		return days_inactive
