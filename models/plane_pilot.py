from odoo import models,fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    codi = fields.Integer('codi',required=True)
    nom = fields.Char('nom')
    cognoms = field.Char('cognoms')
    nif = field.Char('nif')
    telf = field.Char('telefon')
    email = field.Char('email')