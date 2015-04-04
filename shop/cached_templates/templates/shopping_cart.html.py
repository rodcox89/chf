# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428026389.455581
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/shopping_cart.html'
_template_uri = 'shopping_cart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rental_cart = context.get('rental_cart', UNDEFINED)
        request = context.get('request', UNDEFINED)
        int = context.get('int', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rental_cart = context.get('rental_cart', UNDEFINED)
        request = context.get('request', UNDEFINED)
        int = context.get('int', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="items">\n    <h2>Your Cart</h2>\n    <table class="table">\n    <thead>\n        <th>\n                Quantity\n        </th>\n        <th>\n                Name\n        </th>\n        <th>\n                Price\n        </th>\n        <th>\n                Item Total\n        </th>\n        <th>\n                Remove\n        </th>\n    </thead>\n    <tbody>\n        ')
        purchase_total = 0
        
        __M_writer('\n\n\n')
        for key,value in current_cart.items():
            __M_writer('\n        ')

            price = int(value[0].current_price)
            qty = value[1]
            
            product_sub_total = (price * qty)
            purchase_total += product_sub_total
                    
            
            __M_writer('\n\n        <tr>\n            <td>')
            __M_writer(str( value[1]))
            __M_writer('</td>\n            <td>')
            __M_writer(str( value[0].name ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( value[0].current_price ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( product_sub_total ))
            __M_writer('</td>\n            <td><a href="#" class="red delete_button" data-pid="')
            __M_writer(str( value[0].id))
            __M_writer('"  }><i class="fa fa-minus-square"></i> </a></td>\n\n\n        </tr>\n')
        __M_writer('    </tbody>\n    <tfoot>\n    <tr>\n            <td></td>\n            <td></td>\n            <td> </td>\n            <td><h3>Purchase Total</h3></td>\n            <td><h3>$')
        __M_writer(str( purchase_total ))
        __M_writer('</h3></td>\n        </tr>\n\n    </tfoot>\n\n</table>\n</div>\n<div class="items">\n\n\n    <table class="table">\n    <thead>\n        <th>\n            Name\n        </th>\n        <th>\n                Daily Rate\n        </th>\n        <th>\n                Monthly Price\n        </th>\n\n        <th>\n                Remove\n        </th>\n    </thead>\n    <tbody>\n        ')
        rental_total = 0
        
        __M_writer('\n\n\n\n')
        for rental in rental_cart:
            __M_writer('\n        ')

            month = rental.rental_price * 30
            rental_total +=rental.rental_price
                    
            
            __M_writer('\n\n        <tr>\n            <td>')
            __M_writer(str( rental.name))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( rental.rental_price ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( month ))
            __M_writer('</td>\n\n            <td><a href="#" class="red delete_button" data-pid="')
            __M_writer(str( rental.id))
            __M_writer('"  }><i class="fa fa-minus-square delete "></i> </a></td>\n\n\n        </tr>\n')
        __M_writer('    </tbody>\n    <tfoot>\n        <tr>\n\n            <td></td>\n            <td></td>\n            <td><h3>Rental Total</h3></td>\n\n            <td>     <h3> $')
        __M_writer(str( rental_total ))
        __M_writer('</h3>     </td>\n        </tr>\n        <tr>\n\n            <td>\n\n            </td>\n')
        if request.user.is_authenticated():
            __M_writer('            <td>\n                <a href="/shop/checkout/" class="btn btn-primary checkout_button">Proceed to Checkout</a>\n            </td>\n\n')
        else:
            __M_writer('            <td>\n                <h3>Please <a href="#" class="show_login_dialog" >Login</a>  to Checkout</h3>\n            </td>\n')
        __M_writer('            <td>\n\n            </td>\n            <td>\n\n            </td>\n            <td>\n\n            </td>\n        </tr>\n    </tfoot>\n\n</table>\n\n</div>\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "38": 1, "43": 149, "49": 3, "59": 3, "60": 26, "62": 26, "63": 29, "64": 30, "65": 31, "73": 37, "74": 40, "75": 40, "76": 41, "77": 41, "78": 42, "79": 42, "80": 43, "81": 43, "82": 44, "83": 44, "84": 49, "85": 56, "86": 56, "87": 83, "89": 83, "90": 87, "91": 88, "92": 89, "97": 92, "98": 95, "99": 95, "100": 96, "101": 96, "102": 97, "103": 97, "104": 99, "105": 99, "106": 104, "107": 112, "108": 112, "109": 119, "110": 120, "111": 124, "112": 125, "113": 129, "119": 113}, "uri": "shopping_cart.html", "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/shopping_cart.html"}
__M_END_METADATA
"""
