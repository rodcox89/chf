# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428613852.251973
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/items.html'
_template_uri = 'items.html'
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="items">\n        <div class="container">\n            <div class="row">\n                <div class="col-md-12">\n                    <h2 class="title">Rentable Items</h2>\n                </div>\n                <div id="item-loop">\n')
        for item in items:
            __M_writer('                        <!-- Item #1 -->\n                        <div class="col-md-3 col-sm-4">\n                            <div class="item">\n                                <!-- Item image -->\n                                <div class="item-image">\n                                    <a href="/shop/item_detail/')
            __M_writer(str( item.id ))
            __M_writer('">\n                                        <img src="/static/shop/media/product_images/')
            __M_writer(str( item.id ))
            __M_writer('.jpg" alt="')
            __M_writer(str( item.id))
            __M_writer('.jpg image" />\n                                    </a>\n                                </div>\n                                <!-- Item details -->\n                                <div class="item-details">\n                                    <!-- Name -->\n                                    <!-- Use the span tag with the class "ico" and icon link (hot, sale, deal, new) -->\n                                    <h5>')
            __M_writer(str( item.name ))
            __M_writer('\n                                    </h5>\n                                    <div class="clearfix"></div>\n                                    <!-- Para. Note more than 2 lines. -->\n                                    <p>')
            __M_writer(str( item.description ))
            __M_writer('</p>\n                                    <hr />\n                                    <!-- Price -->\n\n                                    <div class="item-price pull-left">Daily Rental<br> Price:$')
            __M_writer(str( item.rental_price ))
            __M_writer('</div>\n                                    <!-- Add to cart -->\n                                    <button data-iid="')
            __M_writer(str( item.id ))
            __M_writer('" data-product="false"  class="btn btn-default add_button pull-right">Add to Cart</button>\n                                    <div class="clearfix"></div>\n                                </div>\n                            </div>\n                        </div>\n')
        __M_writer('                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 29, "65": 29, "66": 33, "67": 33, "68": 35, "69": 35, "70": 41, "76": 70, "27": 0, "35": 1, "40": 45, "46": 3, "53": 3, "54": 11, "55": 12, "56": 17, "57": 17, "58": 18, "59": 18, "60": 18, "61": 18, "62": 25, "63": 25}, "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/items.html", "uri": "items.html"}
__M_END_METADATA
"""
