// Copyright (c) 2017, MAKWIZ Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payment Request Voucher', {
	refresh: function(frm) {
		

	},
payment_term:function(frm){	
	return frappe.call({
		doc: frm.doc,
		method: "calculate_amount",		
		callback: function(r) {
			if(!r.exc) frm.refresh_fields("po_amount_in_figures");
		}
	})
},

po_no:function(frm){
	return frappe.call({
		doc: frm.doc,
		method: "reset_fiels",		
		callback: function(r) {
			if(!r.exc) 
				frm.refresh_fields("name_of_payee");
				frm.refresh_fields("amount_in_figures");
				frm.refresh_fields("po_amount_in_figures");
				frm.refresh_fields("payment_term");
				frm.refresh_fields("payment_terms");
				frm.refresh_fields("po_taxes");
				frm.refresh_fields("tax");
				frm.refresh_fields("in_words");
				
		}
	})
}

});
