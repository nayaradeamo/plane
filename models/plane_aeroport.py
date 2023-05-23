from odoo import models,fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    name = fields.Char(compute='_get_name', string="nom del aeroport i el seu pais", readonly='True', store=False)
    nom = fields.Char('nom')
    imatge = fields.Image('imatge')
    ciutat= fields.Char('ciutat')
    pais = fields.Char('pais')
    latitud = fields.Float('latitud')
    longitud = fields.Float('longitud')
    aeroport_ids = fields.One2many('plane.aeroport','aeroport_id',string='desti')
    aeroport2_ids = fields.One2many('plane.aeroport','aeroport2_id',string='origen')
    
    def _get_name(self):
        for record in self:
            record.name = str(record.nom)+ "de "+ str(record.pais)