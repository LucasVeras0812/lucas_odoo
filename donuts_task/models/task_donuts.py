from odoo import models, fields, api

class Donuts(models.Model):
    _name = 'donuts.task'
    _description = 'Module for a donut shop'

    product_name = fields.Char(
        string="Product name",
        required=True,
    )
    product_description = fields.Text(
        string='This product is...',
    )
    
