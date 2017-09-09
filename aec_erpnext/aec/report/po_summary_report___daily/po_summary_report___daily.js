frappe.query_reports["PO Summary Report - Daily"] = {
	"filters": [
		{
			"fieldname":"date",
			"label": __("Transaction Date"),
			"fieldtype": "Date",
			"width": "80",
			"default": frappe.datetime.get_today()
		}
	]
}