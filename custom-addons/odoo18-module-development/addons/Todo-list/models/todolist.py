from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'
    _order = 'id desc'
    
    # more fields visit https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html#fields
    name = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description', sanitize=True)
    start_date = fields.Date(string='Start Date', required=True, default=fields.Date.today)
    end_date = fields.Date(string='End Date', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),# value, label
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete')
    ], string='Status', default='draft', tracking=True)
    tags = fields.Selection([
        ('work', 'Work'),
        ('event', 'Event'),
        ('life', 'Life')
    ], string='Tags', default='work', tracking=True)
    attendee_ids = fields.Many2many(comodel_name='res.users', string='Attendees')
    
    #FIXME - end date must be after start date