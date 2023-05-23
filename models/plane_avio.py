from odoo import models,fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    codi = fields.Integer('codi',required=True)
    imatge = fields.Image('imatge')
    marca = fields.Integer('marca')
    model = fields.Char('model')
    max_vel = fields.Float('velocitat maxima')
    avio_vol = fields.One2many('plane.avio','plane.vol',string='avio_vol')