from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
    
class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tags'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index')

    @api.model
    def init(self):
        default_tags = ['Work', 'Event', 'Life achievements']
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
    start_date = fields.Datetime(string='Start Date', required=True, default=fields.Datetime.today)
    end_date = fields.Datetime(string='End Date', required=True)
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
    todo_item_ids = fields.One2many('todo.item', 'todo_list_id', string='Todo Items')
    all_items_completed = fields.Boolean(string='All Items Completed', compute='_compute_all_items_completed', store=True)
    
    @api.depends('todo_item_ids.is_completed', 'todo_item_ids')
    def _compute_all_items_completed(self):
        for record in self:
            if record.todo_item_ids:
                record.all_items_completed = all(item.is_completed for item in record.todo_item_ids)
            else:
                record.all_items_completed = False
    
    def mark_as_complete(self):
        for record in self:
            if record.all_items_completed:
                record.write({'status': 'complete'})
    
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date:
                if record.start_date > record.end_date:
                    raise ValidationError(_('End date must be after start date.'))

class TodoItem(models.Model):
    _name = 'todo.item'
    _description = 'Todo Item'
    _order = 'id desc'

    name = fields.Char(string='Item Name', required=True)
    description = fields.Text(string='Description')
    todo_list_id = fields.Many2one('todo.list', string='Todo List', required=True)
    is_completed = fields.Boolean(string='Is Completed', default=False)
    
    