	# co2
	#@api.multi
	#def create_service_co2(self):
	#	ret = reco_funcs.create_service_co2(self)
	#	return ret

	# excilite
	#@api.multi
	#def create_service_excilite(self):
	#	ret = reco_funcs.create_service_excilite(self)
	#	return ret

	# ipl
	#@api.multi
	#def create_service_ipl(self):
	#	ret = reco_funcs.create_service_ipl(self)
	#	return ret


	# ndyag
	#@api.multi
	#def create_service_ndyag(self):
	#	ret = reco_funcs.create_service_ndyag(self)
	#	return ret

	# quick
	#@api.multi
	#def create_service_quick(self):
	#	ret = reco_funcs.create_service_quick(self)
	#	return ret




	# medical
	#@api.multi
	#def create_service_medical(self):
	#	ret = reco_funcs.create_service_medical(self)
	#	return ret

	# cosmetology
	#@api.multi
	#def create_service_cosmetology(self):
	#	ret = reco_funcs.create_service_cosmetology(self)
	#	return ret

	# product
	#@api.multi
	#def create_service_product(self):
	#	ret = reco_funcs.create_service_product(self)
	#	return ret



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



# ---------------------------------------------- Create Service - Co2 --------------------------------------------------------

# Co2 
def create_service_co2(self):  

	treatment_id = self.id

	family = 'laser'
	subfamily = 'co2'
		
	# Open 	
	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current - Laser Co2',

			#'res_model': 'openhealth.service.co2',				
			'res_model': 'price_list.service_co2',				
			
			#'res_id': consultation_id,
			"views": [[False, "form"]],
			#'view_type': 'form',
			'view_mode': 'form',	
			'target': 'current',
			'flags': 	{
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': False, }
						},
			'context': {							
							'default_pl_family': family,
							'default_pl_subfamily': subfamily,

							'default_treatment': treatment_id,
						}
			}
# create_service_co2





# ---------------------------------------------- Create Service - Excilite --------------------------------------------------------

def create_service_excilite(self):  

	# Init 
	treatment_id = self.id 

	family = 'laser'
	subfamily = 'excilite'

			
	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current - Laser Excilite', 
			'view_type': 'form',
			'view_mode': 'form',			
			'target': 'current',

			#'res_model': 'openhealth.service.excilite',				
			'res_model': 'price_list.service_excilite',				
			
			#'res_id': 23,
			'flags': 	{
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},

			'context': {
							'default_treatment': treatment_id,

							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
						}
			}
# create_service_excilite


# ---------------------------------------------- Create Service - IPL --------------------------------------------------------		

def create_service_ipl(self):  

	# Init 
	treatment_id = self.id 

	family = 'laser'
	subfamily = 'm22'


	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current - Laser Excilite', 
			'view_type': 'form',
			'view_mode': 'form',			
			'target': 'current',			

			#'res_model': 'openhealth.service.ipl',				
			'res_model': 'price_list.service_ipl',				
			
			#'res_id': 23,
			'flags': 	{
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
			'context': {
							'default_treatment': treatment_id,
							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
						}
			}
# create_service_ipl






# ---------------------------------------------- Create Service - Quick --------------------------------------------------------

# Quick 
def create_service_quick(self):  

	# Init 
	treatment_id = self.id 

	family = 'laser'
	subfamily = 'quick'

	
	# Open 
	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current - Laser quick', 
			
			#'res_model': 'openhealth.service.quick',		
			'res_model': 'price_list.service_quick',				
			
			#'res_id': consultation_id,
			"views": [[False, "form"]],
			#'view_type': 'form',
			'view_mode': 'form',	
			'target': 'current',
			'flags': 	{
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': False, }
						},
			'context': {
							'default_treatment': treatment_id,

							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
						}
			}
# create_service_quick






# ---------------------------------------------- Create Service - NDYAG --------------------------------------------------------

def create_service_ndyag(self):  

	# Init 
	treatment_id = self.id 

	family = 'laser'
	subfamily = 'm22'

	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current - Laser Ndyag', 
			'view_type': 'form',
			'view_mode': 'form',
			'target': 'current',								

			#'res_model': 'openhealth.service.ndyag',				
			'res_model': 'price_list.service_ndyag',				

			#'res_id': 23,
			'flags': 	{
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
			'context': {
							'default_treatment': treatment_id,

							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
						}
			}
# create_service_ndyag







# ---------------------------------------------- Create Service - MEDICAL --------------------------------------------------------

def create_service_medical(self):  

	# Init 
	treatment_id = self.id 		

	family = 'medical'
	subfamily = 'medical'


	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current - Medical', 
			'view_type': 'form',
			'view_mode': 'form',			
			'target': 'current',

			#'res_model': 'openhealth.service.medical',				
			'res_model': 'price_list.service_medical',				
			
			'flags': 	{
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
			'context': {
							'default_treatment': treatment_id,
							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
						}
			}
# create_service_medical




# ---------------------------------------------- Create Service - Cosmetology --------------------------------------------------------

def create_service_cosmetology(self):  

	# Init 
	treatment_id = self.id 		

	family = 'cosmetology'
	subfamily = 'cosmetology'


	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current - Cosmetology', 
			'view_type': 'form',
			'view_mode': 'form',			
			'target': 'current',

			#'res_model': 'openhealth.service.cosmetology',				
			'res_model': 'price_list.service_cosmetology',				
			
			'flags': 	{
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
			'context': {
							'default_treatment': treatment_id,
							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
						}
			}
# create_service_cosmetology





# ---------------------------------------------- Create Service - Product --------------------------------------------------------
# Product 
def create_service_product(self):  

	# Init 
	treatment_id = self.id 

	family = 'topical'
	subfamily = False

	
	# Open 
	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current - Product', 

			#'res_model': 'openhealth.service.product',		
			'res_model': 'price_list.service_product',				
			
			#'res_id': res_id,
			"views": [[False, "form"]],
			#'view_type': 'form',
			'view_mode': 'form',	
			'target': 'current',
			'flags': 	{
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': False, }
						},
			'context': {
							'default_treatment': treatment_id,
							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
						}
			}
# create_service_product






# ---------------------------------------------- Create Service - gyn -----------------------------

# gyn 
def create_service_gyn(self):  

	treatment_id = self.id 
	family = 'gynecology'
	subfamily = 'gynecology'


	# Open 	
	return {
			'type': 'ir.actions.act_window',

			'name': ' New Service Current - Laser gyn', 
			
			'res_model': 'price_list.service_gynecology',				

			#'res_id': consultation_id,

			"views": [[False, "form"]],
			
			#'view_type': 'form',
			
			'view_mode': 'form',	
			
			'target': 'current',
			
			'flags': 	{
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': False, }
						},

			'context': {							
							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
							'default_treatment': treatment_id,
						}

			}
# create_service_gyn




# ---------------------------------------------- Create Service - echo -----------------------------

# echo 
def create_service_echo(self):  

	treatment_id = self.id
	family = 'echography'
	subfamily = 'echography'

	# Open 	
	return {
			'type': 'ir.actions.act_window',

			'name': ' New Service Current - Laser echo', 
			
			'res_model': 'price_list.service_echography',				

			#'res_id': consultation_id,

			"views": [[False, "form"]],
			
			#'view_type': 'form',
			
			'view_mode': 'form',	
			
			'target': 'current',
			
			'flags': 	{
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': False, }
						},
			'context': {							
							'default_pl_family': family,
							'default_pl_subfamily': subfamily,

							'default_treatment': treatment_id,
						}
			}
# create_service_echo








# ---------------------------------------------- Create Service - promo -----------------------------

# promo 
def create_service_promo(self):  

	treatment_id = self.id 
	family = 'promotion'
	subfamily = 'promotion'

	# Open 	
	return {
			'type': 'ir.actions.act_window',

			'name': ' New Service Current - Laser promo', 
			
			'res_model': 'price_list.service_promotion',				

			#'res_id': consultation_id,

			"views": [[False, "form"]],
			
			#'view_type': 'form',
			
			'view_mode': 'form',	
			
			'target': 'current',
			
			'flags': 	{
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': False, }
						},
			'context': {							
							'default_pl_family': family,
							'default_pl_subfamily': subfamily,
	
							'default_treatment': treatment_id,
						}
			}
# create_service_promo









