# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Pexego All Rights Reserved
#    $Jesús Ventosinos Mayor <jesus@pexego.es>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Document customizations",
    'version': '1.0',
    'category': '',
    'description': """""",
    'author': 'Pexego',
    'website': '',
    "depends": ['report', 'sale', 'stock', 'sale_layout', 'delivery',
                'stock_picking_invoice_link'],
    "data": [
             'custom_reports.xml',
             #'views/ir_qweb.xml',
             'views/layouts.xml',  # Comentado para no poner pie a la izquierda
             'views/report_proforma.xml',
             'views/report_saleorder.xml',
             # 'views/report_stockpicking.xml',
             #'views/valued_picking_report.xml',
             'views/report_purchase_order.xml',
             #'views/report_header.xml',
             'views/report_invoice.xml',
             'data/paperformat_data.xml',
             #'views/purchase_quotation.xml'
             ],
    "installable": True
}
