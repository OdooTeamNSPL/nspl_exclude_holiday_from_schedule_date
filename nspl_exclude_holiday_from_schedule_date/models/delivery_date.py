from datetime import timedelta
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('order_line')
    def _onchange_order_line_delivery_date(self):
        for order in self:
            if not order.order_line:
                continue

            lead_days = max(order.order_line.mapped('product_id.sale_delay'), default=0)
            delivery_date = order._get_delivery_date(order.date_order, int(lead_days))
            order.commitment_date = delivery_date

    def _get_delivery_date(self, start_date, lead_days):
        holidays = self.env['company.holidays'].search([]).mapped('holiday_date')
        holidays = set(fields.Date.from_string(h) for h in holidays)

        date = fields.Datetime.from_string(start_date)
        added_days = 0

        while added_days < lead_days:
            date += timedelta(days=1)
            if date.weekday() < 5 and date.date() not in holidays:
                added_days += 1

        return date
