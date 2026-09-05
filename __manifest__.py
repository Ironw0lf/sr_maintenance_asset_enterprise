{
    "name": "SR Maintenance - Asset Accounting Bridge (Enterprise)",
    "version": "18.0.1.0.0",
    "summary": "Link SR Maintenance equipment and locations to Odoo Enterprise fixed assets",
    "description": """
SR Maintenance - Asset Accounting Bridge (Enterprise)

Adds an optional link from SR Maintenance equipment and locations to a
fixed asset record (account.asset, Odoo Enterprise's native Assets app),
with a smart button to open it.

The link is passive: it never creates or modifies the fixed asset, it
only references one that already exists in Accounting.

Deliberately minimal: unlike the Community bridge (sr_maintenance_asset,
built against the OCA account_asset_management module whose source is
public), this module targets Odoo Enterprise's native account_asset,
which is proprietary - its internal field names could not be verified
against real source or a real instance before first deployment. This
version only relies on the model name (account.asset), not on any of
its internal fields, to avoid guessing field names that could fail to
install. Depreciation info shown inline (as in the Community bridge)
can be added once field names are confirmed against a real Enterprise
instance.
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
