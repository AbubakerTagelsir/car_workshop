# -*- coding: utf-8 -*-

from odoo import models, fields, api

<<<<<<< HEAD
class WorkshopService(models.Model):
    _inherit = 'fleet.vehicle.log.services'

    service_status = fields.Selection(
        selection=[('todo','To-Do'),('inprogress','In-progress'),('done','Done')],
        default= 'todo')

    def inprogress_service(self):
        self.service_status = 'inprogress'

    def done_service(self):
        self.service_status = 'done'

        
        
=======
class contract(models.Model):
    _name = 'contract.contract'

    name = fields.Char(compute='get_name')
    client = fields.Many2one('res.partner')
    date = fields.Datetime(default=fields.Datetime.now)
    items = fields.One2many('contract.order.line','product_id','Order Items')
    total_price = fields.Float(compute="get_order_total_price")
    payments = fields.One2many('contract.payment','contract_id')
    no_of_payments = fields.Integer()
    invoices=fields.One2many('accounts.invoice','contract_id')
    state = fields.Selection(
        selection=[('draft', 'Draft'), ('submit', 'Submited'), ('accepted', "Accepted"), ('reject', "Rejected"), ('canceled', "Canceled")],
        default='draft'
    )


    @api.onchange(no_of_payments)
    def create_payments(self):
        for i in range (no_of_payments):
            self.env['contract.payment'].create({
                'contract_id': self.id
                'percent': 100/(self.no_of_payments)
            })


    def get_name(self):
        self.name='CON'+str(self.id)

    def get_order_total_price(self):   
        total = 0.00
        for i in self:
            for item in items:
                total += item.unit_price * item.qty
            i.total_price = total

    def get_payment_status(self):
        total_paied=self.invoices.total_paid_amount
        count = 0
        for p in self.payments:
            count += p.amount
            if count < total_paied:
                p.status = 'paid'

    
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
    name=fields.Char(compute='get_payment_name')
	percent = fields.Float()
	contract_id = fields.Many2one('contract.contract')
	amount = fields.Float(compute="get_payment_amount")
	status = fields.Selection(
        string='Payment status',
        selection=[('paid', 'Paid'), ('unpaid', 'Unpaid')]
        default="unpaid"
    ) 

    date = fields.Date()
    

    def get_payment_name(self):
        self.name='Pay'+str(self.id)

	def get_payment_amount(self):
		self.amount = (percent/100)*contract_id.total_price

   
        
    

class Invoices(models.Model):
    
    _inherit = 'account.invoice'
    paid_amount=fields.Float()
    total_paid_amount=fields.Float(compute='get_the_total__invoices')
    contract_id = fields.Many2one('contract.contract') 
    def get_the_total_invoices(self):
        total=0
        for i in self:
            total+=i.paid_amount
        self.total_paid_amount=total
            

class SaleOrder(models.Model):
    
    _inherit = 'sale.order'
    contract_id=f


            
>>>>>>> 7aed3472e6df125f4837e63b67f10807f47d1fe1


