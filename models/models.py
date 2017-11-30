# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Plants(models.Model):
    _name = "nursery.plant"

    name = fields.Char("Plant Name")
    price = fields.Float()
    description = fields.Text()


class Customer(models.Model):
    _name = "nursery.customer"

    name = fields.Char("Customer Name", required=True)
    email = fields.Char(help="To received the newsletter")


class Orders(models.Model):
    _name = "nursery.order"

    plant_id = fields.Many2one("nursery.plant", required=True)