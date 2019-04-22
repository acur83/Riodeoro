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


class ResUsers(models.Model):
    """
    Res Users model customization.

    """
    _inherit = 'res.users'

    point_of_sale_id = fields.Many2one('pos.config')


class PosConfig(models.Model):
    """
    Pos Config model customization.

    """
    _inherit = 'pos.config'

    related_user_ids = fields.One2many('res.users', 'point_of_sale_id')
