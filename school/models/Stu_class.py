# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Classlevel(models.Model):

    _name = 'school.level'
    _description = 'Student Class'
    _rec_name = 'name'

    student_ids = fields.One2many('school.student', 'class_id', "Class")
    name = fields.Char('Class Name')