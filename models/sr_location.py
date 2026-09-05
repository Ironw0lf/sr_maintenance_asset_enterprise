from odoo import fields, models


class SrLocation(models.Model):
    _name = 'sr.location'
    _inherit = ['sr.location', 'sr.asset.link.mixin']

    purchase_date = fields.Date('Procurement Date')
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
