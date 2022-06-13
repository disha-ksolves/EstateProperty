# -*- coding: utf-8 -*-

from odoo import fields, models


class Fees(models.Model):

    _name = 'school.fees'
    _description = 'Fees of students as per class level'
    _rec_name = 'name'

    student_id = fields.Many2one('school.student', string="Student_id")
    fees_amount = fields.Integer('Fees Amount')
    fees_date = fields.Date('Fees to be paid every month', required=True, default=fields.Datetime.now, copy=False)
    name = fields.Char('Name')
