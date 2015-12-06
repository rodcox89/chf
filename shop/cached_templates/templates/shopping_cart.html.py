# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428343566.853475
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
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        int = context.get('int', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
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
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        int = context.get('int', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="items">\n    <h2>Products</h2>\n\n    <table class="table">\n    <thead>\n        <th>\n                Quantity\n        </th>\n        <th>\n                Name\n        </th>\n        <th>\n                Price\n        </th>\n        <th>\n                Item Total\n        </th>\n        <th>\n                Remove\n        </th>\n    </thead>\n    <tbody>\n        ')
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
            __M_writer('" data-productbool="True" }><i class="fa fa-minus-square"></i> </a></td>\n\n\n        </tr>\n')
        __M_writer('    </tbody>\n    <tfoot>\n    <tr>\n        <td>\n            <h2>Rentals</h2>\n        </td>\n        <td>\n\n        </td>\n        <td>\n\n        </td>\n        <td>\n\n        </td>\n        <td>\n\n        </td>\n    </tr>\n\n    </tfoot>\n\n</table>\n</div>\n<div class="items">\n\n\n    <table class="table">\n    <thead>\n        <th>\n            Name\n        </th>\n        <th>\n                Daily Rate\n        </th>\n        <th>\n                Monthly Price\n        </th>\n\n        <th>\n                Remove\n        </th>\n    </thead>\n    <tbody>\n        ')

        rental_total = 0
        allmonth = 0
                
        
        __M_writer('\n\n\n\n')
        for rental in rental_cart:
            __M_writer('\n        ')

            month = rental.rental_price * 30
            allmonth += month
            rental_total +=rental.rental_price
            
                    
            
            __M_writer('\n\n        <tr>\n            <td>')
            __M_writer(str( rental.name))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( rental.rental_price ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( month ))
            __M_writer('</td>\n\n            <td><a href="#" class="red delete_button" data-pid="')
            __M_writer(str( rental.id))
            __M_writer('" data-productbool="False" }><i class="fa fa-minus-square delete "></i> </a></td>\n\n\n        </tr>\n')
        __M_writer('    </tbody>\n    <tfoot>\n        <tr>\n\n            <td></td>\n            <td></td>\n            <td><h4>Purchase Total</h4></td>\n\n            <td>     <h4> $')
        __M_writer(str( purchase_total ))
        __M_writer('</h4>     </td>\n        </tr>\n        <tr>\n\n            <td></td>\n            <td></td>\n            <td><h4>Rental Total</h4></td>\n\n            <td>     <h4> $')
        __M_writer(str( allmonth ))
        __M_writer('</h4>     </td>\n        </tr>\n        <tr>\n\n            <td></td>\n            <td></td>\n            <td><h4>Grand Total</h4></td>\n            ')

        grand_total = allmonth+purchase_total
                    
        
        __M_writer('\n            <td>     <h4> $')
        __M_writer(str( grand_total ))
        __M_writer('</h4>     </td>\n        </tr>\n        <tr>\n\n            <td>\n\n            </td>\n')
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
{"source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/shopping_cart.html", "uri": "shopping_cart.html", "line_map": {"131": 125, "27": 0, "38": 1, "43": 183, "49": 3, "59": 3, "60": 27, "62": 27, "63": 30, "64": 31, "65": 32, "73": 38, "74": 41, "75": 41, "76": 42, "77": 42, "78": 43, "79": 43, "80": 44, "81": 44, "82": 45, "83": 45, "84": 50, "85": 94, "90": 97, "91": 101, "92": 102, "93": 103, "100": 108, "101": 111, "102": 111, "103": 112, "104": 112, "105": 113, "106": 113, "107": 115, "108": 115, "109": 120, "110": 128, "111": 128, "112": 136, "113": 136, "114": 143, "118": 145, "119": 146, "120": 146, "121": 153, "122": 154, "123": 158, "124": 159, "125": 163}}
__M_END_METADATA
"""
