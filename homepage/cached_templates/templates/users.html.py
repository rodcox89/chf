# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422761508.182613
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footlinks', 'headlinks']


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
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n  \n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div id="wrapper">\n\n    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n        <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="index.html">Admin Panel</a>\n        </div>\n\n        <div class="collapse navbar-collapse navbar-ex1-collapse">\n            <ul id="active" class="nav navbar-nav side-nav">\n                <li class="selected"><a href="users.html"><i class="fa fa-bullseye"></i> Users</a>\n                </li>\n                <li><a href="#"><i class="fa fa-tasks"></i> Events</a>\n                </li>\n                <li><a href="#"><i class="fa fa-globe"></i></a>\n                </li>\n                <li><a href="#"><i class="fa fa-list-ol"></i> Rental Items</a>\n                </li>\n                <li><a href="#"><i class="fa fa-font"></i> Products</a>\n                </li>\n                <li><a href="#"><i class="fa fa-font"></i> Timeline</a>\n                </li>\n                <li><a href="#"><i class="fa fa-list-ol"></i> Forms</a>\n                </li>\n                <li><a href="#"><i class="fa fa-font"></i> Typography</a>\n                </li>\n                <li><a href="#"><i class="fa fa-list-ul"></i> Bootstrap Elements</a>\n                </li>\n                <li><a href="#"><i class="fa fa-table"></i> Bootstrap Grid</a>\n                </li>\n            </ul>\n\n            <ul class="nav navbar-nav navbar-right navbar-user">\n              \n                <li class="dropdown user-dropdown">\n                    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> Rodney Cox<b class="caret"></b></a>\n                    <ul class="dropdown-menu">\n                        <li><a href="#"><i class="fa fa-user"></i> Profile</a>\n                        </li>\n                        <li><a href="#"><i class="fa fa-gear"></i> Settings</a>\n                        </li>\n                        <li class="divider"></li>\n                        <li><a href="#"><i class="fa fa-power-off"></i> Log Out</a>\n                        </li>\n\n                    </ul>\n                </li>\n                <li class="divider-vertical"></li>\n                           </ul>\n        </div>\n    </nav>\n\n    <div id="page-wrapper">\n\n        <div class="row">\n            <div class="col-lg-12">\n                <h1>Dashboard <small>Statistics and more</small></h1>\n                \n            </div>\n        </div>\n\n    </div>\n\n</div>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n    <script type="text/javascript" src="http://www.shieldui.com/shared/components/latest/js/shieldui-all.min.js"></script>\n    <script type="text/javascript" src="http://www.prepbootstrap.com/Content/js/gridData.js"></script>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headlinks():
            return render_headlinks(context)
        __M_writer = context.writer()
        __M_writer('\n    \n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/homepage/templates/users.html", "uri": "users.html", "source_encoding": "ascii", "line_map": {"65": 7, "27": 0, "38": 1, "71": 79, "43": 5, "77": 79, "48": 77, "83": 3, "53": 82, "89": 3, "59": 7, "95": 89}}
__M_END_METADATA
"""
