/// Copyright (c) 2021, Yasser Elbana and contributors
// For license information, please see license.txt

// {% include 'erpnext/selling/sales_common.js' %}

frappe.ui.form.on("Shipping", {
  refresh: function (frm) {
    frm.add_custom_button("Delivery Trip", () => {
      frappe.new_doc("Delivery Trip", {
        shipping: frm.doc.name,
      });
    });
  },
});

// Make Sales invoice

frappe.ui.form.on("Shipping", {
  refresh: function (frm) {
    frm.add_custom_button("Sales Invoice", () => {
      frappe.model.open_mapped_doc({
        method:
          "logistic.logistic.doctype.shipping.shipping.make_sales_invoice",
        frm: cur_frm,
      });
    });
  },
});

// frappe.ui.form.on("shipping", "refresh", function (frm) {
//   frm.add_custom_button(__("Sales Invoice"), function () {
//     frappe.model.open_mapped_doc({
//       method: "shipping.make_sales_invoice",
//       frm: cur_frm,
//     });
//   });
// });
