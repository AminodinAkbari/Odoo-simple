from email.policy import default
import string
from odoo import fields, models, _
from datetime import datetime

priority_list = [
    ("H" , "High"),
    ("M" , "Medium"),
    ("L" , "Low"),
]


class Task(models.Model):
    _name = "todo.base_models"
    _description = "Tasks Model"

    name    = fields.Char(string="task name" ,required=True )
    date    = fields.Datetime(string = "Date Added" , default=datetime.now())
    done    = fields.Boolean(string = "Done ?" , default=False)
    
    priority = fields.Selection(priority_list ,
     default = "H" ,
     string  = "How important is this to you? " ,
     required = True)

    user    = fields.Many2one("todo.users" , string = "user")
