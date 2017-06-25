import frappe
from frappe import async
from frappe import msgprint, _

@frappe.whitelist()
def validate_custom_item(self, method):
	duplicate1 = frappe.db.sql("""\
			select name from `tabPurchase Receipt` where supplier_name = %s
			and makwiz_invoice_no = %s""",
			(self.supplier_name, self.makwiz_invoice_no))
	if duplicate1:
			frappe.throw(_("Duplicate Purchase Receipt {0}, for Supplier - {1} and Invoice No.- {2} already exist").format(duplicate1[0][0],self.supplier_name,self.makwiz_invoice_no))