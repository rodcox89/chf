# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427945148.669725
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footlinks', 'content', 'appheadlinks', 'shopcontent']


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
    return runtime._inherit_from(context, '/base/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def shopcontent():
            return render_shopcontent(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def appheadlinks():
            return render_appheadlinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'appheadlinks'):
            context['self'].appheadlinks(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        def shopcontent():
            return render_shopcontent(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n<nav class="navbar " role="navigation">\n  <div class="container-fluid">\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="#"><img src="/static/homepage/media/newLogoBlackthe.svg" alt="" /></a>\n    </div>\n\n    <!-- Collect the nav links, forms, and other content for toggling -->\n    <div class="collapse navbar-collapse" id="navbar">\n      <ul class="nav navbar-nav">\n        <li class="active"><a href="/homepage/">Home</a></li>\n        <li><a href="/festivals/">Festivals</a>\n        </li>\n        <li><a href="/shop/items/">Rental Shop</a>\n        </li>\n        <li>\n            <a href="/shop/products/">Products</a>\n        </li>\n        <li>\n            <a href="/administration/users/">Admin</a>\n        </li>\n        <li><a href="#"></a></li>\n\n      </ul>\n      <form id="search_go" class="navbar-form navbar-right" method="POST" action="/shop/index.search/" role="search">\n        <div class="form-group">\n          <input type="text" id="search_input" class="form-control" placeholder="Search">\n        </div>\n        <button type="submit" id="search_button" class="btn btn-default">Submit</button>\n      </form>\n      <ul class="nav navbar-nav navbar-right">\n        <li><a href="#"></a></li>\n\n      </ul>\n      <ul class="nav navbar-nav navbar-right navbar-user">\n\n              <li><a href="#" id="cart"><i class="fa fa-shopping-cart"></i> Cart  </a></li>\n              <li>\n                  <ul class="nav navbar-nav navbar-right navbar-user">\n                      <ul class="nav navbar-nav navbar-right navbar-user">\n')
        if request.user.is_authenticated():
            __M_writer('                              <li class="dropdown user-dropdown">\n                                  <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i>')
            __M_writer(str( user.get_short_name() ))
            __M_writer('<b class="caret"></b></a>\n                                  <ul class="dropdown-menu">\n                                      <li><a href="/shop/account/"><i class="fa fa-user"></i> Profile</a>\n                                      </li>\n                                      <li><a href="#"><i class="fa fa-gear"></i> Settings</a>\n                                      </li>\n                                      <li class="divider"></li>\n                                      <li><a href="/administration/users.logout_view/"><i class="fa fa-power-off"></i> Log Out</a>\n                                      </li>\n\n                                  </ul>\n                              </li>\n')
        else:
            __M_writer('                              <li class="dropdown user-dropdown">\n                                  <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> Login or Signup<b class="caret"></b></a>\n                                  <ul class="dropdown-menu">\n                                      <li>\n                                           <a href="#" id="show_login_dialog">Login</a>\n                                      </li>\n\n                                      <li>\n                                          <a href="/homepage/signup/">Signup</a>\n                                      </li>\n\n                                  </ul>\n')
        __M_writer('\n\n\n                              </ul>\n                          </li>\n                          <li class="divider-vertical"></li>\n                      </ul>\n                  </ul>\n\n              </li>\n\n\n\n      </ul>\n\n    </div><!-- /.navbar-collapse -->\n  </div><!-- /.container-fluid -->\n</nav>\n\n\n\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopcontent'):
            context['self'].shopcontent(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_appheadlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def appheadlinks():
            return render_appheadlinks(context)
        __M_writer = context.writer()
        __M_writer('\n<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\n<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopcontent():
            return render_shopcontent(context)
        __M_writer = context.writer()
        __M_writer('\n    <!-- _________________________The content of the shop will be here _____________________________ -->\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/shop/templates/base.htm", "uri": "base.htm", "source_encoding": "ascii", "line_map": {"69": 114, "75": 10, "85": 10, "86": 59, "87": 60, "88": 61, "89": 61, "90": 73, "91": 74, "92": 87, "97": 111, "27": 0, "103": 3, "42": 1, "109": 3, "47": 8, "115": 109, "52": 112, "57": 116, "121": 109, "127": 121, "63": 114}}
__M_END_METADATA
"""
