import frappe
from frappe import async
from frappe import msgprint, _

@frappe.whitelist()
def populate_item_code(self, method):
	from frappe.model.naming import getseries
	parent_group_code = frappe.db.sql("""\
			select makwiz_item_group_code from `tabItem Group` where item_group_name = ( select parent_item_group
from `tabItem Group` where item_group_name = %s)""",(self.item_group))
	if (parent_group_code[0][0] == 'C' or parent_group_code[0][0] == 'R'):
		Item_code = str(parent_group_code[0][0])+str(self.makwiz_item_group_code)+str(getseries("item_series_number",4))			
	else:		
		Item_code = self.item_code
		
	self.item_code=Item_code
	self.name=self.item_code