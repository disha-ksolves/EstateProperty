# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Student(models.Model):

    _name = 'school.student'
    _description = 'Student Details'
    _order = 'first_name'
    _rec_name = 'first_name'

    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    age = fields.Integer('Age', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    student_dob = fields.Date('Date of Birth')
    phone_number = fields.Char(string='Mobile Number', required=True)
    address = fields.Char(string='Address', required=True)

    subject_ids = fields.Many2many('school.subject', string="List of Subjects")
    class_id = fields.Many2one('school.level', string="Class")
    amount_ids = fields.One2many('school.fees', "student_id", string="FeeAmount")
