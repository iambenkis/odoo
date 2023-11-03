from odoo import fields, models, _

class School(models.Model):
    _name = 'school_table'
    _description = "This is a school Model for testing purposes"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description", required=True)
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Starting date", required=True)
    avg_expected_price = fields.Float(string="Average Expected Price")
    num_of_classes = fields.Integer(string="Number of Classes")
    school_of_option = fields.Selection([
        ('elo', 'Electronic'),
        ('elec', 'Electricity'), 
        ('meca', 'Mechanic'),
    ], string="School Options",)
    customer_id = fields.Many2one('res.customer', string="Customer")