from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime

class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tag'

    tag_name = fields.Selection([
        ('work', 'Work'),
        ('event', 'Event'),
        ('life', 'Life'),
        ('achievement', 'Achievement')], string='Tag')
    todo_list_id = fields.Many2one(comodel_name='todo.list', string='Todo List')  # Add this field
    # user_id = fields.One2Many(comodel_name='res.users', inverse_name=)

    # _sql_constraints = [
    #     ('unique_name_per_user', 'unique(name, user_id)', 'Tag name must be unique per user!')
    # ]

    #FIXME - add ability to add more tags


class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'
    _order = 'id desc'

    name = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description', sanitize=True)
    start_date = fields.Date(string='Start Date', required=True, default=fields.Date.today)
    end_date = fields.Date(string='End Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete')
    ], string='Status', default='draft', tracking=True)
    tag_ids = fields.One2many(comodel_name='todo.tag', inverse_name='todo_list_id', string='Tags')  # Use the new field as inverse_name
    attendee_ids = fields.Many2many(comodel_name='res.users', string='Attendees')
    
    #FIXME - end date must be after start date