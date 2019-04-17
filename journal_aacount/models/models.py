# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------
# 
# ---------------------------------------------------------------------
# Copyright (c) 2017 BDC International Develop Team and Contributors
# All rights reserved.
#
# This is free software; you can redistribute it and/or modify it under
# the terms of the LICENCE attached (see LICENCE file) in the distribution
# package.
#
# Created on 11-04-19

from openerp import models, fields, api
from openerp.tools.translate import _
from odoo import exceptions
from openerp.osv.orm import except_orm

class AccountJournal(models.Model):
    """
    Account Journal model customization.
    
    """
    _inherit = 'account.journal'

    analytic_account_id = fields.Many2one('account.analytic.account')


class AccountMoveLine(models.Model):
    """
    Account Move model customization.
    
    """
    _inherit = 'account.move.line'

    @api.model
    def create(self, vals):
        ''' Redefined for check is exist an analytic related with the journal,
        if we can find it analyce and depending of the journal select the
        analytic account line who must be related with this analytic account.

        '''
        move_line = super(AccountMoveLine,self).create(vals)
        AccountJournal = self.env['account.journal']
        journal = move_line.move_id.journal_id
        if journal.analytic_account_id:
            if journal.type in ('sale', 'cash'):
                if move_line.credit > 0:
                    move_line.analytic_account_id = journal.analytic_account_id
            elif journal.type in ('purchase'):
                if move_line.debit > 0:
                    move_line.analytic_account_id = journal.analytic_account_id
        return move_line
