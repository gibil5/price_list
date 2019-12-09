



"id", "price", "qty", "product", "treatment", "create_uid", "write_uid", "create_date", "write_date"

'price_list_cart_line_id_seq', 
120.0, 
1, 

4936, 

1976, 
1, 
1, 
(now() at time zone 'UTC'), 
(now() at time zone 'UTC')






		return {
				# Created
				'res_id': order.id,
				# Mandatory
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action
				'res_model': 'sale.order',
				# Views
				"views": [[False, "form"]],
				'view_mode': 'form',
				'target': 'current',
				#'view_id': view_id,
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False,
				'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						},
				'context': {}
			}