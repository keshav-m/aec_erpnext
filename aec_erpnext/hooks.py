# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "aec_erpnext"
app_title = "AEC"
app_publisher = "MAKWIZ Technologies"
app_description = "ERPNext extension for AEC"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kmanoj@makwiz.com"
app_license = "MIT"

fixtures = ["Custom Field","Custom Script","Print Format"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aec_erpnext/css/aec_erpnext.css"
# app_include_js = "/assets/aec_erpnext/js/aec_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/aec_erpnext/css/aec_erpnext.css"
# web_include_js = "/assets/aec_erpnext/js/aec_erpnext.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "aec_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "aec_erpnext.install.before_install"
# after_install = "aec_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aec_erpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Purchase Receipt": {
	"validate": "aec_erpnext.hooks_call.purchase_receipt.validate_custom_item"
	},
	"Item": {
	"autoname": "aec_erpnext.hooks_call.item.populate_item_code"
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aec_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"aec_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"aec_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aec_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"aec_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "aec_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "aec_erpnext.event.get_events"
# }

