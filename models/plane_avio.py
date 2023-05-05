from odoo import models,fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    codi = fields.Integer('codi',required=True)
    imatge = fields.Image('imatge')
    marca = fields.Integer('marca')
    model = fields.Char('model')
    maxvel = fields.Float('velocitat maxima')