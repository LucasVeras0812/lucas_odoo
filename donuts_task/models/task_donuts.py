from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TaskDonuts(models.Model):
    _name = 'task.donuts'
    _description = 'Module for a donut shop'
    _rec_name = 'product_name'

    product_name = fields.Char(
        string='Product name',
        required=True,
    )
    type_donuts = fields.Selection(
        string='Type of donuts',
        required=True,
        selection=[
            ('gourmet', 'Gourmet'),
            ('stuffed', 'Sttufed'),
            ('traditional', 'Traditional'),
            ])
    flavor = fields.Char(
        string="Flavor",
        required=True,
    )
    type_coverage = fields.Selection(
        string='Type of coverage',
        required=True,
        selection=[
            ('chocolate', 'Chocolate'),
            ('white_chocolate', 'White chocolate'),
            ('no_coverage', 'No coverage'),
            ])
    price_product = fields.Float(
        string='Price of Donut',
        required=True,
    )
    image = fields.Binary(
        string='',
        attachment=True,  # Salva a imagem como um anexo
    )

    @api.constrains('price_product', 'type_donuts')
    def _check_price_product(self):
        for record in self:
            # define os preços mínimos para cada tipo de donut criando um dicionário
            min_prices = {
                'traditional': 9,
                'stuffed': 14,
                'gourmet': 18,
            }
            # verifica se o preço é menor que o mínimo configurado para o tipo de donuts selecionado
            if record.price_product < min_prices.get(record.type_donuts, 0):
                raise ValidationError(
                    f'O preço para um donuts do tipo "{record.type_donuts.capitalize()}" '
                    f'não pode ser menor que {min_prices[record.type_donuts]:.2f}!'
                )

    


