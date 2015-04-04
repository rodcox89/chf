# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427949135.277062
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/products.html'
_template_uri = 'products.html'
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
        products = context.get('products', UNDEFINED)
        def shopcontent():
            return render_shopcontent(context._locals(__M_locals))
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
        products = context.get('products', UNDEFINED)
        def shopcontent():
            return render_shopcontent(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="items">\n        <div class="container">\n            <div class="row">\n                <div class="col-md-12">\n                    <h2 class="title">Products for Sale</h2>\n                </div>\n                <div id="item-loop">\n')
        for product in products:
            __M_writer('                        <!-- Item #1 -->\n                        <div class="col-md-3 col-sm-4">\n                            <div class="item">\n                                <!-- Item image -->\n                                <div class="item-image">\n                                    <a href="/shop/item_detail/')
            __M_writer(str( product.id ))
            __M_writer('">\n                                        <img src="/static/shop/media/product_images/')
            __M_writer(str( product.id ))
            __M_writer('.jpg" />\n                                    </a>\n                                </div>\n                                <!-- Item details -->\n                                <div class="item-details">\n                                    <!-- Name -->\n                                    <!-- Use the span tag with the class "ico" and icon link (hot, sale, deal, new) -->\n                                    <h5>')
            __M_writer(str( product.name ))
            __M_writer('\n                                    </h5>\n                                    <div class="clearfix"></div>\n                                    <!-- Para. Note more than 2 lines. -->\n                                    <p>')
            __M_writer(str( product.description ))
            __M_writer('</p>\n                                    <hr />\n                                    <!-- Price -->\n\n                                    <div class="item-price pull-left">$')
            __M_writer(str( product.current_price ))
            __M_writer('</div>\n                                    <!-- Add to cart -->\n                                    <button data-iid="')
            __M_writer(str( product.id ))
            __M_writer('" data-product="true" class="btn btn-default add_button pull-right">Add to Cart</button>\n                                    <div class="clearfix"></div>\n                                </div>\n                            </div>\n                        </div>\n')
        __M_writer('                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 33, "65": 33, "66": 35, "35": 1, "68": 41, "40": 45, "74": 68, "46": 3, "59": 18, "67": 35, "53": 3, "54": 11, "55": 12, "56": 17, "57": 17, "58": 18, "27": 0, "60": 25, "61": 25, "62": 29, "63": 29}, "uri": "products.html", "filename": "/Users/rodneycox/chf/shop/templates/products.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
