from odoo import api, models, fields, _

class Plb(models.Model):
    _name = 'plb'
    _description = 'plb'
    _inherit = ['mail.thread']
    _rec_name = "name"

    name = fields.Char(string="name", index=True)
    attachment_ids = fields.Many2many('ir.attachment', 'attachment_id', string='Attachments', copy=False)