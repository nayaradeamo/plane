from odoo import models,fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    codi = fields.Integer('codi',required=True)
    passatgers = fields.Integer('passatgers')
    datasortida = fields.Char('data de sortida')
    dataarrivada = fields.Char('data d_arrivada')