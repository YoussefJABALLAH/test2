from odoo import api, models, fields, _

class Ft(models.Model):
    _name = 'ft'
    _description = 'ft'
    _inherit = ['mail.thread']
    _rec_name = "name"

    name = fields.Char(string="name", index=True)
    attachment_ids = fields.Many2many('ir.attachment', 'attachment_id', string='Attachments', copy=False)