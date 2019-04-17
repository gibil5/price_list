

# ---------------------------------------------- Fields - Categorized ---------
	
	pl_family = fields.Selection(

			selection=pl_vars_prod._family_list,

			string='Family',
			required=True,
		)

	pl_subfamily = fields.Selection(

			selection=pl_vars_prod._subfamily_list,

			string='Subfamily',
			required=True,
		)




	pl_manufacturer = fields.Selection(
			selection=pl_vars._manufacturer_list,
			string='Manufacturer',
		)

	pl_brand = fields.Selection(
			selection=pl_vars._brand_list,
			string='brand',
		)




	pl_treatment = fields.Selection(
			selection=pl_vars._treatment_list,
			string='Treatment',
			required=False,
		)

	pl_zone = fields.Selection(
			selection=pl_vars._zone_list,
			string='Zone',
			required=False,
		)

	pl_pathology = fields.Selection(
			selection=pl_vars._pathology_list,
			string='Pathology',
			required=False,
		)



	pl_level = fields.Selection(
			selection=pl_vars._level_list,
			string='Level',
			required=False,
		)

	pl_sessions = fields.Selection(
			selection=pl_vars._sessions_list,
			string='Sessions',
			required=False,
		)

	pl_time = fields.Selection(
			selection=pl_vars._time_list,
			string='Time',
			required=False,
		)



# ---------------------------------------------- Fields - Floats -----------------------

	pl_price = fields.Float(
			'Price',
			required=True,
		)


	pl_price_company = fields.Float(
			'Price company',
			required=True,
		)
