# -*- coding: utf-8 -*-

from odoo import models, fields, api

class contract(models.Model):
    _name = 'contract.contract'

    name = fields.Char()
    client = fields.Many2one('res.partner')
    date = fields.Datetime(default=fields.Datetime.now)
    items = fields.One2many('contract.order.line','product_id','Order Items')
    total_price = fields.Float(compute="get_order_total_price")
    payment = fields.One2many('contract.payment','contract_id')
    no_of_payments = fields.Integer()

    def _get_the_total_price(self):   
        total = 0.00
        for i in self:
            for item in items:
                total += item.unit_price * item.qty
            i.total_price = total


    
class OrderLine(models.Model):
    _name = 'contract.order.line'
    order_id = fields.Many2one(
        comodel_name='contract.contract',
        ondelete='set null',)
    product_id = fields.Many2one(
        comodel_name='product.template',
        ondelete='set null',)
    qty = fields.Integer()
    unit_price = fields.Float(related="product_id.list_price")
    

class Payment(models.Model):
	_name = 'contract.payment'
	percent = fields.Float()
	contract_id = fields.Many2one('contract.contract')
	amount = fields.Float(compute="get_payment_amount")
	status = ields.Selection(
        string='Payment status',
        selection=[('paid', 'Paid'), ('unpaid', 'Unpaid')]
    )

    date = fields.Date()
    paid=fields.Float()


	def get_payment_amount(self):
		self.amount = percent*contract_id.total_price


