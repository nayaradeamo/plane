from odoo import models,fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    codi = fields.Integer('codi',required=True)
    passatgers = fields.Integer('passatgers')
    data_sortida = fields.Datetime('data de sortida')
    data_arrivada = fields.Datetime('data d_arrivada')
    vol_aeroport = fields.Many2one('plane.vol','plane.aeroport',string='desti')
    vol_aeroport2 = fields.Many2one('plane.vol','plane.aeroport',string='origen')
    vol_avio = fields.Many2one('plane.vol','plane.avio',string='vol_avio')
    vol_pilot = fields.Many2one('plane.vol','plane.pilot',string='vol_pilot')