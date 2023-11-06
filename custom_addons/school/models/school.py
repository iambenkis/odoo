from odoo import api,fields, models, _
from odoo.exceptions import ValidationError

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
    status = fields.Boolean(string="Status", default=False)
    annual_fees = fields.Float(string="Annual Fees", compute="_compute_tri_annual_fees")
    department_id = fields.Many2one('school_table.department', string="Department")

    _sql_constraints = [
         ('unique_name', 'UNIQUE(name)', 'The name must be unique!'),
    ]

    @api.depends('avg_expected_price')
    def _compute_tri_annual_fees(self):
        for record in self:
            record.annual_fees = record.avg_expected_price * 3

    def update_status(self):
        for record in self:
            record.status = not record.status