# SR Maintenance - Asset Accounting Bridge (Enterprise)

Links SR Maintenance equipment and locations to a fixed asset record in
Odoo Enterprise's native Assets app, for reference to its depreciation
schedule and book value from the maintenance side.

## What it's for

Equipment already tracks a purchase value and a replacement value, but
has no connection to the actual fixed asset record accountants manage
for depreciation. This module adds that connection - a simple reference,
not a duplicate of the accounting data.

The link is deliberately **passive**: it never creates, modifies, or
deletes the fixed asset. It only points to one that already exists in
Accounting, so a technician or asset manager can see its accounting
status without leaving the equipment or location record.

## Features

On both **Equipment** and **Location** records, a new "🏦 Fixed Asset"
tab shows:

- The linked fixed asset (`account.asset`) - asset templates (state
  "Model") are excluded from the selection, only real assets can be
  linked
- Procurement date
- Asset status (Draft/Running/On Hold/Closed/Cancelled)
- Acquisition date
- Original value, salvage value (non-depreciable value), and current
  book value
- The full depreciation board (one line per depreciation journal entry,
  with amount, cumulative depreciation, remaining value and posting
  status), with the journal entry itself one click away

A smart button on both forms opens the linked asset's full record in
Accounting.

## A note on how this was built

Odoo Enterprise's `account_asset` module is proprietary - its source
isn't available to read the way the Community/OCA equivalent's is. Every
field name used in this module (`original_value`, `acquisition_date`,
`book_value`, `depreciation_move_ids`, etc.) was confirmed against a real
Enterprise instance before being relied on - first through developer-mode
field tooltips, then more completely through the raw field metadata
returned by the `get_views` call (visible in the browser's Network tab
when opening an asset form) - rather than guessed from documentation or
from the Community module's different field names.

## Dependencies

Requires an **Odoo Enterprise** license with the native `account_asset`
app (Accounting → Assets) installed. It is **not compatible** with the
OCA `account_asset_management` module - the two provide the same
`account.asset` model and cannot be installed together. For a Community
client without Enterprise, use the separate `sr_maintenance_asset`
bridge module instead.

## Installation

1. Place this module in the addons path, alongside SR Maintenance.
2. Restart Odoo.
3. Apps → Update Apps List → Install "SR Maintenance - Asset Accounting
   Bridge (Enterprise)".

## License

LGPL-3
