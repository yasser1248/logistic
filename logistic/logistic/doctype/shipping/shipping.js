/// Copyright (c) 2021, Yasser Elbana and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shipping', {
    refresh: function(frm) {
        frm.add_custom_button('Sales Invoice', ()=> {
            frappe.new_doc('Sales Invoice', {
                Shipping: frm.doc.name
            })
        })
        frm.add_custom_button('Delivery Trip', ()=> {
            frappe.new_doc('Delivery Trip', {
                Shipping: frm.doc.name
            })
        })
    }
})
