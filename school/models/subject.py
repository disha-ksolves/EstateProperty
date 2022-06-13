# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Subject(models.Model):

    _name = 'school.subject'
    _description = 'Subjects selected by students'
    _rec_name = 'name'

    name = fields.Char('Name')
    subject_name = fields.Selection([('maths', 'Maths'), ('science', 'Science'), ('physics', 'Physics'),
                                     ('chemistry', 'Chemistry')], string='Subjects')


