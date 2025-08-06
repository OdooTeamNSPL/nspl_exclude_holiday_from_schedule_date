from odoo import models, fields, api, _


class CompanyHolidays(models.Model):
    _name = 'company.holidays'
    _description = 'Company Holidays'

    name = fields.Char(string='Holiday Description', required=True)
    holiday_date = fields.Date(string='Holiday Date', required=True)
