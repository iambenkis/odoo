# -*- coding: utf-8 -*-

from odoo import models, fields, api


class People(models.Model):
    _name = 'people'
    _description = 'Custom contact '

    name = fields.Char(string='Name', required=True)
    is_company = fields.Boolean(string='Is a Company', default=False, compute='_is_company')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    country = fields.Selection([
        ('CO', 'Congo'),
        ('BE', 'Belgium'),
        ('FR', 'France'),
        ('US', 'USA'),
    ], string='Country')
    contact_type = fields.Selection([
        ('individual', 'Individual'), 
        ('company', 'Company')], 
        string='Contact Type', default='individual')

    rccm = fields.Char(string='RCCM', domain="[('is_company','=',True)]")
    id_nat = fields.Char(string='Id. Nat.', domain="[('is_company','=',True)]")
    nif = fields.Char(string='NIF', domain="[('is_company','=',True)]", compute="_compute_nif", inverse="_inverse_nif" , store=True) #compute="_compute_nif", store=True
    tva = fields.Char(string='TVA', domain="[('is_company','=',True)]")

    @api.depends('contact_type')
    def _is_company(self):
        for record in self:
            record.is_company = record.contact_type == 'company'
    
    @api.depends('country')
    def _compute_nif(self):
        for record in self:
            record.nif = record.tva if record.country == "CO" else record.nif

    def _inverse_nif(self):
        for record in self:
            record.nif = record.nif
