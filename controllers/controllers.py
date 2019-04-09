# -*- coding: utf-8 -*-
from openerp import http

# class PriceList(http.Controller):
#     @http.route('/price_list/price_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/price_list/price_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('price_list.listing', {
#             'root': '/price_list/price_list',
#             'objects': http.request.env['price_list.price_list'].search([]),
#         })

#     @http.route('/price_list/price_list/objects/<model("price_list.price_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('price_list.object', {
#             'object': obj
#         })