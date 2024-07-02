from odoo import api,  fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    _order = 'sequence'

    name = fields.Char(string="Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
   
    
