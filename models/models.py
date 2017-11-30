# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Plants(models.Model):
    _name = "nursery.plant"

    name = fields.Char("Plant Name")
    price = fields.Float()
    description = fields.Text()

    order_ids = fields.One2many("nursery.order", "plant_id", string="Orders")


class Customer(models.Model):
    _name = "nursery.customer"

    name = fields.Char("Customer Name", required=True)
    email = fields.Char(help="To received the newsletter")


class Orders(models.Model):
    _name = "nursery.order"

    name = fields.Datetime(default=fields.Datetime.now)
    plant_id = fields.Many2one("nursery.plant", required=True)
    customer_id = fields.Many2one("nursery.customer", required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Calceled')

    ], default='draft')

    last_modification = fields.Datetime(readonly=True)
    
    def write(self, vals):
        # helper to "YYYY-MM-DD"
        vals["last_modification"] = fields.Datetime.now()
        return super(Orders, self).write(vals)

    def unlink(self):
        # self is a recordset
        for order in self:
            if order.state == "confirm":
                # UserWarning or UserError
                raise UserError("You cannot delete confirmd orders.")
        return super(Orders, self).unlink()
