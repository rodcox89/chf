# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425433942.315214
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/shop.html'
_template_uri = 'shop.html'
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
        __M_writer = context.writer()
        __M_writer('\n')
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
        __M_writer = context.writer()
        __M_writer('\n<nav class="navbar navbar-default" role="navigation">\n  <div class="container-fluid">\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="#">ohh baby</a>\n    </div>\n\n    <!-- Collect the nav links, forms, and other content for toggling -->\n    <div class="collapse navbar-collapse" id="navbar">\n      <ul class="nav navbar-nav">\n        <li class="active"><a href="#">Home</a></li>\n        <li><a href="#"></a></li>\n\n      </ul>\n      <form class="navbar-form navbar-left" role="search">\n        <div class="form-group">\n          <input type="text" class="form-control" placeholder="Search">\n        </div>\n        <button type="submit" class="btn btn-default">Submit</button>\n      </form>\n      <ul class="nav navbar-nav navbar-right">\n        <li><a href="#"></a></li>\n\n      </ul>\n      <ul class="nav navbar-nav navbar-right navbar-user">\n\n              <li><a href="#" id="cart_button"><i class="fa fa-shopping-cart"></i> Cart () </a></li>\n\n\n\n\n      </ul>\n\n    </div><!-- /.navbar-collapse -->\n  </div><!-- /.container-fluid -->\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"34": 1, "51": 2, "39": 44, "57": 51, "27": 0, "45": 2}, "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/shop.html", "uri": "shop.html"}
__M_END_METADATA
"""
