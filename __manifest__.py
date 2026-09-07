{
    "name": "SR Maintenance - Asset Accounting Bridge (Enterprise)",
    "version": "19.0.1.0.0",
    "summary": "Link SR Maintenance equipment and locations to Odoo Enterprise fixed assets",
    "description": """
SR Maintenance - Asset Accounting Bridge (Enterprise)

Adds an optional link from SR Maintenance equipment and locations to a
fixed asset record (account.asset, Odoo Enterprise's native Assets app),
with a smart button to open it.

The link is passive: it never creates or modifies the fixed asset, it
only references one that already exists in Accounting.

The Fixed Asset tab shows status, acquisition date, original/salvage/
book value and the full depreciation board (journal entries), mirroring
the Community bridge (sr_maintenance_asset, built against the OCA
account_asset_management module). Field names were confirmed against a
real Enterprise instance (AWSS) via the field metadata returned by
get_views, since account_asset's source is proprietary and could not be
verified beforehand any other way.
    """,
    "author": "Serge Rivoallan",
    "website": "https://sr-maintenance.com",
    "category": "Manufacturing/Maintenance",
    "license": "LGPL-3",
    "depends": [
        "sr_maintenance",
        "account_asset",
    ],
    "data": [
        "views/sr_equipment_views.xml",
        "views/sr_location_views.xml",
    ],
    "installable": True,
}
