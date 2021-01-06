from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"


    def get_docs_count(self):
        count = self.env['document.record'].search_count([
            ('employee_id', '=', self.id)])
        self.docs_count = count

    docs_count = fields.Integer(compute='get_docs_count')


    def get_docs(self):
        return {
            'name': 'Document',
            'domain': [('employee_id', '=', self.id)],
            'context': {'default_employee_id': self.id},
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'document.record',
            'view_mode': 'tree,form',
            'view_id': False,
        }
