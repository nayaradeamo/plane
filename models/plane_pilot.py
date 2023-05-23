from odoo import models,fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    codi = fields.Integer('codi',required=True)
    nom = fields.Char('nom')
    cognom = fields.Char('cognoms')
    nif = fields.Char('nif')
    telf = fields.Char('telefon')
    email = fields.Char('email')
    pilot_vol= fields.One2many('plane.pilot','plane.vol',string='pilot_vol')