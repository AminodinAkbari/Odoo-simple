from odoo import fields , models , _
# from utills.custom_lists import priority_list



class Users(models.Model):
	_name 		 = "todo.users"
	_description = "Users Of our app"

	name     = fields.Char(string = "First Name" , required = True)
	family   = fields.Char(string = "Last Name" , required = True)
	# email  = 


