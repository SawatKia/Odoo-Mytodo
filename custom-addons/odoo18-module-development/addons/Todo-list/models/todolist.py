from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
    
class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tags'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index')

    @api.model
    def _setup_default_tags(self):
        default_tags = ['Work', 'Event', 'Life']
        for tag_name in default_tags:
            existing_tag = self.search([('name', '=', tag_name)])
            if not existing_tag:
                self.create({'name': tag_name})
    
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
    tag_ids = fields.Many2many(
        'todo.tag',
        string='Tags',
    )
    attendee_ids = fields.Many2many(comodel_name='res.users', string='Attendees')
    
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date:
                if record.start_date > record.end_date:
                    raise ValidationError(_('End date must be after start date.'))
    
    