from odoo import models


class SrEquipment(models.Model):
    _name = 'sr.equipment'
    _inherit = ['sr.equipment', 'sr.asset.link.mixin']
