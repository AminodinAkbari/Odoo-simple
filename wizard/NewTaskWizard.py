from odoo import fields , models , _
from datetime import datetime


priority_list = [
    ("H" , "High"),
    ("M" , "Medium"),
    ("L" , "Low"),
]

class CreateTaskWizard(models.TransientModel):

	_name = "todo.task.wiz"
	_description = "Create Task With Wizard"

	name    = fields.Char(string="task name" ,required=True )
	date    = fields.Datetime(string = "Date Added" , default=datetime.now())
	done    = fields.Boolean(string = "Done ?" , default=False)
	
	priority = fields.Selection(priority_list ,
	 default = "H" ,
	 string  = "How important is this to you? " ,
	 required = True)

	user    = fields.Many2one("todo.users" , string = "user")

	def action_create_task_in_db(self):
		vals = {
			'name' : self.name , 
			'date' : self.date ,
			'done' : self.done ,
			'priority' : self.priority ,
			'user' : self.user.id ,
		}

		task_record = self.env["todo.base_models"].create(vals)

		return{
			'name' : ('Task'),
			'type' : 'ir.actions.act_window',
			'view_mode' : 'form',
			'res_model' : 'todo.base_models',
			'res_id' : task_record.id,
			'target' : 'new'
		}