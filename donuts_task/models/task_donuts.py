from odoo import models, fields, api

class Donuts(models.Model):
    _name = 'donuts.task'
    _description = 'Module for a donut shop'

    name_product = fields.Char(
        string="Product name",
        required=True,
    )
    product_description = fields.Text(
        'This product is...',
    )
    
