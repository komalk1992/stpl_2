from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
        {
                "label": _("stpl_2"),
                "icon": "octicon octicon-briefcase",
                "items": [
                {
                        "type": "doctype",
                        "name": "Second Doctype",
                        "label": _("Second Doctype"),
                },
               
                ]
        }
]

