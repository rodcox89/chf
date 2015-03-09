# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425693569.521433
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/item_detail.html'
_template_uri = 'item_detail.html'
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
        def shopcontent():
            return render_shopcontent(context._locals(__M_locals))
        item = context.get('item', UNDEFINED)
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
        def shopcontent():
            return render_shopcontent(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container">\n\n\n        <div class="panel panel-default">\n          <div class="panel-heading">\n            <h3 class="panel-title">')
        __M_writer(str( item.name ))
        __M_writer('</h3>\n          </div>\n          <div class="panel-body">\n              <img src="/static/shop/media/product_images/')
        __M_writer(str( item.id ))
        __M_writer('.jpg"  />\n          </div>\n          <div class="panel-footer">\n            <div class="row">\n\n            <p>\n                $')
        __M_writer(str( item.value ))
        __M_writer('\n            </p>\n            <button data-iid="')
        __M_writer(str( item.id ))
        __M_writer('"  class="btn btn-default add_button pull-right">Add to Cart</button>\n            <select id="quantity" name="Item Quantity">\n                <option value="1">1</option>\n                <option value="2">2</option>\n                <option value="3">3</option>\n                <option value="4">4</option>\n                <option value="5">5</option>\n\n            </select>\n            </div>\n            <p>\n                ')
        __M_writer(str( item.description ))
        __M_writer('\n            </p>\n          </div>\n        </div>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/item_detail.html", "line_map": {"35": 1, "69": 63, "40": 38, "46": 3, "59": 19, "53": 3, "54": 10, "55": 10, "56": 13, "57": 13, "58": 19, "27": 0, "60": 21, "61": 21, "62": 32, "63": 32}, "uri": "item_detail.html"}
__M_END_METADATA
"""
