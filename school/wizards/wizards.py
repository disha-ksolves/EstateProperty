# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Examdetail(models.TransientModel):

    _name = 'school.wizard'
    _description = 'Wizards'

    student_id = fields.Many2one('school.student', string="Student Name")
    subject_id = fields.Many2one('school.subject', string="Subject Name")
    exam_date = fields.Date('Exam Date')

    def exam_creation(self):
        print("Exam Created")
        self.env['school.exam'].create({'student_id':self.student_id.id,'subject_id':self.subject_id.id})

