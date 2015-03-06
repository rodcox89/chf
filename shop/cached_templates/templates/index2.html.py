# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425617658.575726
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/index2.html'
_template_uri = 'index2.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        for item in items:
            __M_writer('<div class="item_container">\n    <img src="http://merzantiques.com/img/feature/Colt-Gatling-Gun.jpg" />\n    <a href="/shop/index2/')
            __M_writer(str( item.id ))
            __M_writer('"> ')
            __M_writer(str( item.name ))
            __M_writer(' ')
            __M_writer(str( item.id ))
            __M_writer('</a>\n<button data-iid="')
            __M_writer(str( item.id ))
            __M_writer('" class="add_button" >Add to Cart</button>\n</div>\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index2.html", "line_map": {"64": 14, "35": 1, "70": 64, "40": 15, "46": 3, "59": 9, "53": 3, "54": 6, "55": 7, "56": 9, "57": 9, "58": 9, "27": 0, "60": 9, "61": 9, "62": 10, "63": 10}, "filename": "/Users/rodneycox/chf/shop/templates/index2.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
