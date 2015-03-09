# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425796992.647731
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
        int = context.get('int', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        int = context.get('int', UNDEFINED)
        request = context.get('request', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="items">\n    <h2>Your Cart</h2>\n    <table class="table">\n    <thead>\n        <th>\n                Quantity\n        </th>\n        <th>\n                Name\n        </th>\n        <th>\n                Price\n        </th>\n        <th>\n                Item Total\n        </th>\n        <th>\n                Remove\n        </th>\n    </thead>\n    <tbody>\n        ')
        grand_total = 0
        
        __M_writer('\n\n\n')
        for key,value in current_cart.items():
            __M_writer('\n        ')

            price = int(value[0].value)
            qty = value[1]
            
            sub_total = (price * qty)
            grand_total += sub_total
                    
            
            __M_writer('\n\n        <tr>\n            <td>')
            __M_writer(str( value[1]))
            __M_writer('</td>\n            <td>')
            __M_writer(str( value[0].name ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( value[0].value ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( sub_total ))
            __M_writer('</td>\n            <td><a href="#" class="red delete_button" data-pid="')
            __M_writer(str( value[0].id))
            __M_writer('"  }><i class="fa fa-minus-square"></i> </a></td>\n\n\n        </tr>\n')
        __M_writer('    </tbody>\n    <tfoot>\n        <tr>\n            <td></td>\n            <td></td>\n            <td><h3>Grand Total</h3> </td>\n            <td></td>\n            <td>     <h3> $')
        __M_writer(str( grand_total ))
        __M_writer('</h3>     </td>\n        </tr>\n        <tr>\n            <td>\n\n            </td>\n            <td>\n\n            </td>\n')
        if request.user.is_authenticated():
            __M_writer('            <td>\n                <a href="/shop/checkout/" class="btn btn-primary checkout_button">Proceed to Checkout</a>\n            </td>\n')
        else:
            __M_writer('            <td>\n                <h3>Please <a href="#" class="show_login_dialog" >Login</a>  to Checkout</h3>\n            </td>\n')
        __M_writer('            <td>\n\n            </td>\n            <td>\n\n            </td>\n            <td>\n\n            </td>\n        </tr>\n    </tfoot>\n\n</table>\n\n</div>\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"71": 37, "72": 40, "73": 40, "74": 41, "75": 41, "76": 42, "77": 42, "78": 43, "79": 43, "80": 44, "81": 44, "82": 49, "83": 56, "84": 56, "85": 65, "86": 66, "87": 69, "88": 70, "89": 74, "27": 0, "95": 89, "37": 1, "42": 94, "48": 3, "57": 3, "58": 26, "60": 26, "61": 29, "62": 30, "63": 31}, "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/shopping_cart.html", "uri": "shopping_cart.html"}
__M_END_METADATA
"""
