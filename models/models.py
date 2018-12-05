# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WorkshopService(models.Model):
    _inherit = 'fleet.vehicle.log.services'

    service_status = fields.Selection(
        selection=[('todo','To-Do'),('inprogress','In-progress'),('done','Done')],
        default= 'todo')

    def inprogress_service(self):
        self.service_status = 'inprogress'

    def done_service(self):
        self.service_status = 'done'

        
        


