from odoo import fields, models, _

class Hospital(models.Model):
    _name = "hospital_table"
    _description = "This is a hospital Model for testing purposes"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description", required=True)
    speciality = fields.Char(string="Speciality")
    days_of_availability = fields.Selection([
        ('mon', 'Monday'), 
        ('wed', 'Wednesday'), 
        ('fri', 'Friday'),
        ('sat', 'Saturday'), 
    ])