from odoo import fields, models, _

class Department(models.Model):
    _name = 'school_table.department' 
    _description = "School department Model"

    name = fields.Char(string="Name", required=True) 