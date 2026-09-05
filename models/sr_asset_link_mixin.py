from odoo import fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class SrAssetLinkMixin(models.AbstractModel):
    _name = 'sr.asset.link.mixin'
    _description = 'Fixed Asset Link'

    sr_asset_id = fields.Many2one(
        'account.asset',
        string='Fixed Asset',
        tracking=True,
        domain="[('state', '!=', 'model')]",
        help='Optional link to the fixed asset record in Accounting, for '
             'reference to its depreciation schedule and book value. Never '
             'created automatically here - the asset must already exist. '
             'Open it via the smart button to see its full depreciation '
             'details in Accounting.',
    )
    asset_state = fields.Selection(related='sr_asset_id.state', string='Asset Status')
    asset_currency_id = fields.Many2one(related='sr_asset_id.currency_id', string='Asset Currency')
    asset_acquisition_date = fields.Date(
        related='sr_asset_id.acquisition_date',
        string='Asset Acquisition Date',
    )
    asset_original_value = fields.Monetary(
        related='sr_asset_id.original_value',
        string='Asset Original Value',
        currency_field='asset_currency_id',
    )
    asset_salvage_value = fields.Monetary(
        related='sr_asset_id.salvage_value',
        string='Asset Salvage Value',
        currency_field='asset_currency_id',
    )
    asset_book_value = fields.Monetary(
        related='sr_asset_id.book_value',
        string='Asset Book Value',
        currency_field='asset_currency_id',
    )
    asset_depreciation_move_ids = fields.One2many(
        related='sr_asset_id.depreciation_move_ids',
        string='Depreciation Board',
    )

    def action_view_sr_asset(self):
        self.ensure_one()

        if not self.sr_asset_id:
            raise UserError(_('No fixed asset linked.'))

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.asset',
            'res_id': self.sr_asset_id.id,
            'view_mode': 'form',
        }
