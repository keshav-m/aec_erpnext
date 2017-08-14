import frappe
from frappe import async
from frappe import msgprint, _

@frappe.whitelist()
def populate_item_tax(self, method):
	
	if self.taxes_and_charges == "SGST & CGST":		
		for d in self.get("items"):
			tax_type_sgst = frappe.db.sql("""\
				select substring_index(tax_type, '-', 1) from `tabItem Tax` where parent = %s and tax_type like %s""",(d.item_code, 'SGST%'))
			tax_type_cgst = frappe.db.sql("""\
				select substring_index(tax_type, '-', 1) from `tabItem Tax` where parent = %s and tax_type like %s""",(d.item_code, 'CGST%'))
			if tax_type_sgst or tax_type_cgst:
				tax_type = []
				tax_type = '( '+tax_type_sgst[0][0]+', '+tax_type_cgst[0][0]+' )'
				d.makwiz_item_tax_rate = tax_type

	if self.taxes_and_charges == "IGST":		
		for d in self.get("items"):
			tax_type_igst = frappe.db.sql("""\
				select substring_index(tax_type, '-', 1) from `tabItem Tax` where parent = %s and tax_type like %s""",(d.item_code, 'IGST%'))			
			if tax_type_igst:
				tax_type = []
				tax_type = '( '+tax_type_igst[0][0]+' )'
				d.makwiz_item_tax_rate = tax_type	