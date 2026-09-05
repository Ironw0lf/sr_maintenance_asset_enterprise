from odoo import fields, models


class SrLocation(models.Model):
    _name = 'sr.location'
    _inherit = ['sr.location', 'sr.asset.link.mixin']

    purchase_date = fields.Date('Procurement Date')
