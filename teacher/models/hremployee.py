# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Hr(models.Model):
    _inherit = "hr.employee"

    class_ids = fields.Many2many('school.level', string="Classes")
    subject_ids = fields.Many2many('school.subject', string="Subjects")



