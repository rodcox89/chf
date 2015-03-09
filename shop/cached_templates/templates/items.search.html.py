# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425757688.535404
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/items.search.html'
_template_uri = 'items.search.html'
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
        __M_writer('\n    \n')
        for item in items:
            __M_writer('        <!-- Item #1 -->\n        <div class="col-md-3 col-sm-4">\n            <div class="item">\n                <!-- Item image -->\n                <div class="item-image">\n                    <a href="/shop/item_detail/')
            __M_writer(str( item.id ))
            __M_writer('">\n                        <img src="/static/shop/media/product_images/')
            __M_writer(str( item.id ))
            __M_writer('.jpg" />\n                    </a>\n                </div>\n                <!-- Item details -->\n                <div class="item-details">\n                    <!-- Name -->\n                    <!-- Use the span tag with the class "ico" and icon link (hot, sale, deal, new) -->\n                    <h5>')
            __M_writer(str( item.name ))
            __M_writer('\n                    </h5>\n                    <div class="clearfix"></div>\n                    <!-- Para. Note more than 2 lines. -->\n                    <p>')
            __M_writer(str( item.description ))
            __M_writer('</p>\n                    <hr />\n                    <!-- Price -->\n\n                    <div class="item-price pull-left">$')
            __M_writer(str( item.value ))
            __M_writer('</div>\n                    <!-- Add to cart -->\n                    <button data-iid="')
            __M_writer(str( item.id ))
            __M_writer('"  class="btn btn-default add_button pull-right">Add to Cart</button>\n                    <div class="clearfix"></div>\n                </div>\n            </div>\n        </div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/shop/templates/items.search.html", "uri": "items.search.html", "line_map": {"64": 27, "65": 27, "66": 29, "35": 1, "68": 35, "40": 36, "74": 68, "46": 3, "59": 12, "67": 29, "53": 3, "54": 5, "55": 6, "56": 11, "57": 11, "58": 12, "27": 0, "60": 19, "61": 19, "62": 23, "63": 23}, "source_encoding": "ascii"}
__M_END_METADATA
"""
