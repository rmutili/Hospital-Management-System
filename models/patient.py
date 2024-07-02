from odoo import api,  fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    age = fields.Float(compute="_compute_age")
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel' 'patient_id', 'tag_id', string="Tags")

    @api.depends("age")
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.date_of_birth:
                record.age = (today - record.date_of_birth).days / 365.25
            else:
                record.age = 0

    
