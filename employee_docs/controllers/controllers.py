# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeDocs(http.Controller):
#     @http.route('/employee_docs/employee_docs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_docs/employee_docs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_docs.listing', {
#             'root': '/employee_docs/employee_docs',
#             'objects': http.request.env['employee_docs.employee_docs'].search([]),
#         })

#     @http.route('/employee_docs/employee_docs/objects/<model("employee_docs.employee_docs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_docs.object', {
#             'object': obj
#         })
