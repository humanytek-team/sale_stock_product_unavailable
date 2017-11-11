# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, models
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_confirm(self):

        for order in self:

            products_unavailable = list()

            for line in order.order_line:

                product = line.product_id

                if product.type == 'product':

                    product_qty = self.env['product.uom']._compute_qty_obj(
                        line.product_uom,
                        line.product_uom_qty,
                        line.product_id.uom_id)

                    if product_qty > (product.qty_available -
                        product.outgoing_qty):

                        products_unavailable.append(product.display_name)

            if products_unavailable:
                raise ValidationError(
                    _(
                        'The following products has not availability: %s' %
                        ', '.join(products_unavailable))
                    )

        return super(SaleOrder, self).action_confirm()
