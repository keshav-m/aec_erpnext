# -*- coding: utf-8 -*-
# Copyright (c) 2017, MAKWIZ Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt, cstr, cint
from frappe.model.document import Document

class PaymentRequestVoucher(Document):
	def validate(self):
		self.set_amount_in_words()

	def calculate_amount(self):
		if (flt(self.po_amount_in_figures) !=0 and flt(self.payment_term) !=0):
			if (flt(self.po_amount_in_figures) != 0):
				self.amount_in_figures = (flt(self.po_amount_in_figures) * flt(self.payment_term))/100

		if (flt(self.po_taxes) != 0):
			self.tax = flt(self.po_taxes) 


	
	def set_amount_in_words(self):
		if (flt(self.amount_in_figures) != 0):
			from frappe.utils import money_in_words
			self.in_words = money_in_words(self.amount_in_figures)
	
	def reset_fiels(self):
		self.name_of_payee = ''
		self.amount_in_figures = ''
		self.po_amount_in_figures =''
		self.payment_term = ''
		self.payment_terms = ''
		self.po_taxes = ''
		self.tax = ''
		self.in_words = ''

