# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Student(models.Model):

    _name = 'school.exam'
    _description = 'Exam Details'

    student_id = fields.Many2one('school.student', string="Student Name")
    subject_id = fields.Many2one('school.subject', string="Subjects")
    student_mark = fields.Integer("Exams Details")





