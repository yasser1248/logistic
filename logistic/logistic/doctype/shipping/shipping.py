# -*- coding: utf-8 -*-
# Copyright (c) 2021, Yasser Elbana and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import sys
sys.path.append(r"/home/erpnext/frappe-bench/apps/erpnext")
sys.path.append(r"/home/erpnext/frappe-bench/apps/frappe")
sys.path.append(r"/home/erpnext/frappe-bench/apps/logistic")
import frappe
import frappe.model.mapper
from frappe.model.document import Document
from erpnext.accounts.party import set_taxes
from erpnext.controllers.selling_controller import SellingController
from frappe import _
from frappe.contacts.address_and_contact import load_address_and_contact
from frappe.email.inbox import link_communication_to_document




class Shipping(Document):
    pass


@frappe.whitlist()
def make_sales_invoice(source_name, target_doc=None):
    def set_missing_values(source, target):
        _set_missing_values(source, target)

    target_doc = get_mapped_doc("shipping", source_name,
                                {"shipping": {
                                    "doctype": "Sales Invoice",
                                    "field_map": {
                                        "campaign_name": "campaign",
                                        "doctype": "opportunity_from",
                                        "name": "party_name",
                                        "lead_name": "contact_display",
                                        "company_name": "customer_name",
                                        "email_id": "contact_email",
                                        "mobile_no": "contact_mobile"
                                    }

                                }},	target_doc, set_missing_values)

    return target_doc
