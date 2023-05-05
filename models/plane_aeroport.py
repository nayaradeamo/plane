from odoo import models,fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    codi = fields.Integer('codi',required=True)
    nom = fields.Char('nom')
    imatge = fields.Image('imatge')
    ciutat= fields.Char('ciutat')
    pais = fields.Char('pais')
    latitud = fields.Float('latitud')
    longitud = fields.Float('longitud')