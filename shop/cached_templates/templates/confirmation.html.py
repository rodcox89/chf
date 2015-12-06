# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428184035.467441
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/confirmation.html'
_template_uri = 'confirmation.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['shopcontent']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        int = context.get('int', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)
        def shopcontent():
            return render_shopcontent(context._locals(__M_locals))
        confirmation = context.get('confirmation', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopcontent'):
            context['self'].shopcontent(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        int = context.get('int', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)
        def shopcontent():
            return render_shopcontent(context)
        confirmation = context.get('confirmation', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="container">\n\n')
        if confirmation:
            __M_writer('\n<h1>Order Confirmation# ')
            __M_writer(str( confirmation["ID"] ))
            __M_writer('</h1>\n\n')
        __M_writer('<div class="items">\n    <h2></h2>\n    <div class="panel panel-default">\n        <!-- Default panel contents -->\n        <div class="panel-heading"><h3>Purchases</h3></div>\n\n        <!-- Table -->\n        <table class="table">\n            <th>\n\n                <td>\n                    Product\n                </td>\n                <td>\n                    Unit Price\n                </td>\n                <td>\n                    Extended Price\n                </td>\n            </th>\n        <tbody>\n            ')
        purchase_total = 0
        
        __M_writer('\n\n\n')
        for key,value in current_cart.items():
            __M_writer('                ')


            price = int(value[0].current_price)
            qty = value[1]
            
            product_sub_total = (price * qty)
            purchase_total += product_sub_total
                            
            
            __M_writer('\n\n\n                <tr>\n                    <td>')
            __M_writer(str( value[1]))
            __M_writer('</td>\n                    <td>')
            __M_writer(str( value[0].name ))
            __M_writer('</td>\n                    <td>$')
            __M_writer(str( price ))
            __M_writer('</td>\n                    <td>$')
            __M_writer(str( product_sub_total ))
            __M_writer('</td>\n\n\n\n                </tr>\n')
        __M_writer('\n\n        </tbody>\n        </table>\n    </div>\n    <div class="panel panel-default">\n        <!-- Default panel contents -->\n        <div class="panel-heading"><h3>Rentals</h3></div>\n\n        <!-- Table -->\n        <table class="table">\n            <th>\n                <td>\n                    Item\n                </td>\n                <td>\n                    Daily  Price\n                </td>\n                <td>\n                    30 Day Price\n                </td>\n            </th>\n        <tbody>\n            ')
        rental_total=0
        
        __M_writer('\n\n')
        for rental in rental_cart:
            __M_writer('            ')

            month = rental.rental_price * 30
            rental_total += month
                        
            
            __M_writer('\n\n\n                <tr>\n                    <td> </td>\n                    <td>')
            __M_writer(str( rental.name ))
            __M_writer('</td>\n                    <td>$')
            __M_writer(str( rental.rental_price ))
            __M_writer('</td>\n                    <td>$')
            __M_writer(str( month ))
            __M_writer('</td>\n\n\n\n                </tr>\n')
        __M_writer('\n        </tbody>\n        </table>\n\n    </div>\n    <div class="panel panel-default">\n        <!-- Default panel contents -->\n        <div class="panel-heading"><h3>Payment Summary</h3></div>\n        <table>\n            <tfoot>\n                <tr>\n\n                    <td></td>\n                    <td></td>\n                    <td><h4>Purchase Total </h4></td>\n\n                    <td>     <h4> $')
        __M_writer(str( purchase_total ))
        __M_writer('</h4>     </td>\n                </tr>\n                <tr>\n\n                    <td></td>\n                    <td></td>\n                    <td><h4>Rental Total</h4></td>\n\n                    <td>     <h4> $')
        __M_writer(str( rental_total ))
        __M_writer('</h4>     </td>\n                </tr>\n                <tr>\n\n                    <td></td>\n                    <td></td>\n                    <td><h4>Grand Total</h4></td>\n                    ')

        grand_total = rental_total+purchase_total
                            
        
        __M_writer('\n                    <td>     <h4> $')
        __M_writer(str( grand_total ))
        __M_writer('</h4>     </td>\n                </tr>\n                <tr>\n\n            </tfoot>\n        </table>\n    </div>\n</div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "38": 1, "43": 142, "49": 3, "59": 3, "60": 6, "61": 7, "62": 8, "63": 8, "64": 11, "65": 32, "67": 32, "68": 35, "69": 36, "70": 36, "79": 43, "80": 47, "81": 47, "82": 48, "83": 48, "84": 49, "85": 49, "86": 50, "87": 50, "88": 56, "89": 79, "91": 79, "92": 81, "93": 82, "94": 82, "99": 85, "100": 90, "101": 90, "102": 91, "103": 91, "104": 92, "105": 92, "106": 98, "107": 114, "108": 114, "109": 122, "110": 122, "111": 129, "115": 131, "116": 132, "117": 132, "123": 117}, "uri": "confirmation.html", "filename": "/Users/rodneycox/chf/shop/templates/confirmation.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
