# -*- coding: utf-8 -*-
# from odoo import http


# class ScafModule(http.Controller):
#     @http.route('/scaf_module/scaf_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scaf_module/scaf_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('scaf_module.listing', {
#             'root': '/scaf_module/scaf_module',
#             'objects': http.request.env['scaf_module.scaf_module'].search([]),
#         })

#     @http.route('/scaf_module/scaf_module/objects/<model("scaf_module.scaf_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scaf_module.object', {
#             'object': obj
#         })
