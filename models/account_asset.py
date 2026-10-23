from odoo import api, fields, models, _


class AccountAsset(models.Model):
    _name = 'account.asset'
    _inherit = 'account.asset'

    sr_equipment_ids = fields.One2many('sr.equipment', 'sr_asset_id', string='Equipment')
    sr_equipment_count = fields.Integer(compute='_compute_sr_equipment_count')
    sr_location_ids = fields.One2many('sr.location', 'sr_asset_id', string='Locations')
    sr_location_count = fields.Integer(compute='_compute_sr_location_count')

    @api.depends('sr_equipment_ids')
    def _compute_sr_equipment_count(self):
        for asset in self:
            asset.sr_equipment_count = len(asset.sr_equipment_ids)

    @api.depends('sr_location_ids')
    def _compute_sr_location_count(self):
        for asset in self:
            asset.sr_location_count = len(asset.sr_location_ids)

    def action_view_sr_equipment(self):
        self.ensure_one()

        if len(self.sr_equipment_ids) == 1:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sr.equipment',
                'res_id': self.sr_equipment_ids.id,
                'view_mode': 'form',
            }

        return {
            'type': 'ir.actions.act_window',
            'name': _('Equipment'),
            'res_model': 'sr.equipment',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.sr_equipment_ids.ids)],
        }

    def action_view_sr_location(self):
        self.ensure_one()

        if len(self.sr_location_ids) == 1:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sr.location',
                'res_id': self.sr_location_ids.id,
                'view_mode': 'form',
            }

        return {
            'type': 'ir.actions.act_window',
            'name': _('Locations'),
            'res_model': 'sr.location',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.sr_location_ids.ids)],
        }
