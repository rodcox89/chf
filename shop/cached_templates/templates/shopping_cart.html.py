# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425614028.453146
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
        item = context.get('item', UNDEFINED)
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
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="">\n\n</div>\n\n<!-- for item in items:\n<div class="item_container">\n    <img src="http://merzantiques.com/img/feature/Colt-Gatling-Gun.jpg" />\n    <a href="/shop/index2/')
        __M_writer(str( item.id ))
        __M_writer('"> ')
        __M_writer(str( item.name ))
        __M_writer(' ')
        __M_writer(str( item.id ))
        __M_writer('</a>\n<button data-pid="')
        __M_writer(str( item.id ))
        __M_writer('" class="add_button" >Add to Cart</button>\n</div>\n\nendfor -->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "40": 18, "46": 3, "59": 12, "67": 61, "53": 3, "54": 12, "55": 12, "56": 12, "57": 12, "58": 12, "27": 0, "60": 13, "61": 13}, "source_encoding": "ascii", "uri": "shopping_cart.html", "filename": "/Users/rodneycox/chf/shop/templates/shopping_cart.html"}
__M_END_METADATA
"""
