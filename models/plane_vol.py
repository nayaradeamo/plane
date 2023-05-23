from odoo import models,fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    name = fields.Char(compute='_get_name', string=" vol ", readonly='True', store=False)
    passatgers = fields.Integer('passatgers')
    data_sortida = fields.Datetime('data de sortida')
    data_arrivada = fields.Datetime('data d_arrivada')
    aeroport_id = fields.Many2one('plane.vol',string='desti')
    aeroport2_id = fields.Many2one('plane.vol',string='origen')
    avio_id= fields.Many2one('plane.vol',string='avio')
    pilot_id= fields.Many2one('plane.vol',string='pilot')

    def _get_name(self):
        for record in self:
            record.name = str(record.id)