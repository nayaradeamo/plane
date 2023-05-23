from odoo import models,fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    name = fields.Char(compute='_get_name', string="codi i model avio", readonly='True', store=False)
    codi = fields.Integer('codi',required=True)
    imatge = fields.Image('imatge')
    marca = fields.Integer('marca')
    model = fields.Char('model')
    max_vel = fields.Float('velocitat maxima')
    avio_ids = fields.One2many('plane.avio','avio_id',string='avio')

    def _get_name(self):
        for record in self:
            record.name = str(record.codi)+ " "+ str(record.model)