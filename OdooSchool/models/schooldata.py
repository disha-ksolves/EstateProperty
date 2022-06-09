from odoo import api, fields, models


class SchoolModel(models.Model):

    _name = "school.model"
    _description = "School Details"

    name = fields.Char('School Name', required=True)
