from datetime import date
from odoo import api, fields, models


class DocumentRecord(models.Model):
    _name = "document.record"

    name = fields.Char(string='doc no', required=True, copy=False,
                       readonly=True, index=True,
                       default=lambda self: ('New'))
    doc_name = fields.Char(string="name")
    employee_id = fields.Many2one('hr.employee', string="Employee Name",
                                  required=True)
    document = fields.Binary(string="Document")
    end_date = fields.Date(string="Expiry Date")
    state = fields.Selection([('draft', 'Draft'), ('approve', 'Approve'),
                             ('refuse', 'Refuse'), ('expired', 'Expired')],
                             default='draft')


    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'document.record') or ('New')
        result = super(DocumentRecord, self).create(vals)

        return result


    def set_draft(self):
        self.write({
            'state': 'draft'
        })

    def set_approve(self):
        self.write({
            'state': 'approve'
        })

    def set_refuse(self):
        self.write({
            'state': 'refuse'
        })

    def _scheduler_demo(self):
        docs = self.env['document.record'].search([])
        for i in docs:
            if i.end_date == date.today():
                i.write({
                    'state': 'expired'
                })
                print('\n\n--docs--\n\n', i.state)
                print('\n\n--docs--\n\n', i.doc_name)
