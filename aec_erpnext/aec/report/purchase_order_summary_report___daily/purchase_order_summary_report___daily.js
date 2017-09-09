frappe.query_reports["Purchase Order Summary Report - Daily"] = {
	"filters": [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company")
		},
		{
			"fieldname":"date",
			"label": __("Transaction Date"),
			"fieldtype": "Date",
			"width": "80",
			"default": frappe.datetime.get_today()
		}
	]
}