	#date = fields.Datetime(
	name = fields.Datetime(


	#def _default_task_ids(self):

	#task_ids = fields.Many2many('price_list.task', default=_default_task_ids)



	# ----------------------------------------------------------- Fields ---------------------
	appointment = fields.One2many(
			'price_list.appointment',
			'matrix_id',
		)



	# ----------------------------------------------------------- Update - Button ---------------------

	@api.multi
	def update(self):
		"""
		Update
		"""
		print()
		print('Update')


	# ----------------------------------------------------------- validate - Button ---------------------

	@api.multi
	def validate(self):
		"""
		validate
		"""
		print()
		print('validate')





	@api.multi
	def create(self):
		"""
		create
		"""
		print()
		print('Create')

		# your list of project should come from the context, some selection
	   	# in a previous wizard or wherever else

		projects = self.env['price_list.project'].browse([1, 2, 3])
		print(projects)

		# same with users

		users = self.env['price_list.user'].browse([1, 2, 3])
		print(users)


		return [
		   (0, 0, {'project_id': p.id, 'user_id': u.id, 'planned_hours': 0})

		   # if the project doesn't have a task for the user, create a new one
		   #if not p.task_ids.filtered(lambda x: x.user_id == u) else
		   # otherwise, return the task
		   #(4, p.task_ids.filtered(lambda x: x.user_id == u)[0].id)
		   for p in projects
		   for u in users
		]



	# ----------------------------------------------------------- create - Button ---------------------

	#@api.multi
	#def create(self):
	#	"""
	#	create
	#	"""
	#	print()
	#	print('create')
