import frappe
from frappe import async
from frappe import msgprint, _

@frappe.whitelist()
def populate_item_tax(self, method):
	
	if self.taxes_and_charges == "SGST & CGST":		
		for d in self.get("items"):			
			gst_tax = ''
			tax_sgst = ''
			tax_cgst = ''
			tax_type_sgst = frappe.db.sql("""\
				select substring_index(tax_type, '-', 1) from `tabItem Tax` where parent = %s and tax_type like %s""",(d.item_code, 'SGST%'))
			if tax_type_sgst:
				tax_sgst = tax_type_sgst[0][0]
			tax_type_cgst = frappe.db.sql("""\
				select substring_index(tax_type, '-', 1) from `tabItem Tax` where parent = %s and tax_type like %s""",(d.item_code, 'CGST%'))
			if tax_type_cgst:
				tax_cgst = tax_type_cgst[0][0]
			if tax_sgst and tax_cgst:
				gst_tax = '('+tax_sgst+','+tax_cgst+')'			
			d.makwiz_item_tax_rate = gst_tax		

	if self.taxes_and_charges == "IGST":		
		for d in self.get("items"):			
			gst_tax = ''
			tax_igst = ''	
			tax_type_igst = frappe.db.sql("""\
				select substring_index(tax_type, '-', 1) from `tabItem Tax` where parent = %s and tax_type like %s""",(d.item_code, 'IGST%'))			
			if tax_type_igst:
				tax_igst = tax_type_igst[0][0]			
				gst_tax = '('+tax_igst+')'
			d.makwiz_item_tax_rate = gst_tax