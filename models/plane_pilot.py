from odoo import models,fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    nom = fields.Char('nom')
    cognom = fields.Char('cognoms')
    nif = fields.Char('nif')
    telf = fields.Char('telefon')
    email = fields.Char('email')
    pilot_ids= fields.One2many('plane.pilot','pilot_id',string='pilot')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom)+ " "+ str(record.cognom)