{
    'name': 'Todo List Management',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Manage your todo lists efficiently',
    'description': """
Todo List Management
===================
This module allows users to create and manage todo lists.
Features include:
- Todo list creation with title, description, and dates
- Todo items management with completion tracking
- Status tracking (draft, incomplete, complete)
- Tag management
- Attendee assignment
- Dashboard views for all, incomplete, and complete todo lists
""",
    'author': 'Sawat Lapprasertlum',
    'website': 'https://roots.tech/',
    'depends': ['base'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/todolist_view.xml",
        "views/todolist_menu.xml"
        ],
    'demo': [],
    'installable': True,
    'application': True,
    'assests': {},
    'license': 'LGPL-3',
}