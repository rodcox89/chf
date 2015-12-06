# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428526530.510371
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/administration/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'administrationcontent', 'footlinks', 'appheadlinks']


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
        request = context.get('request', UNDEFINED)
        def appheadlinks():
            return render_appheadlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def administrationcontent():
            return render_administrationcontent(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'appheadlinks'):
            context['self'].appheadlinks(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def administrationcontent():
            return render_administrationcontent(context)
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n    <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand" href="/homepage/index/">\n            <img class="nav-logo" src="/static/homepage/media/chflatowhite.svg">\n\n        </a>\n    </div>\n\n    <div class="collapse navbar-collapse navbar-ex1-collapse">\n        <ul id="active" class="nav navbar-nav side-nav">\n            <li>\n')
        __M_writer('            </li>\n            <li class="selected">\n                <div class="left-bar"></div>\n                <a href="/administration/users/"><i class="fa fa-users"></i>&nbsp;&nbsp;&nbsp;&nbsp;Users\n                    <div class="arrow-left"></div>\n                </a>\n\n            </li>\n            <li>\n                <a href="/administration/locations/"><i class="fa fa-map-marker"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Locations</a>\n            </li>\n            <li>\n                <a href="/administration/events/"><i class="fa fa-calendar-o"></i>&nbsp;&nbsp;&nbsp;&nbsp; Events</a>\n            </li>\n            <li>\n                <a href="/administration/items/"><i class="fa fa-list-ol"></i>&nbsp;&nbsp;&nbsp;&nbsp; Rental Items</a>\n            </li>\n            <li>\n                <a href="/administration/products/"><i class="fa fa-money"></i>&nbsp;&nbsp;&nbsp;&nbsp;Products </a>\n\n            </li>\n            <li>\n                <a href="/administration/venues/"><i class="fa fa-qrcode"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Venues</a>\n            </li>\n            <li>\n                <a href="/administration/overdue/"><i class="fa fa-exchange"></i></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Overdue Rentals</a>\n            </li>\n            <li>\n                <a href="/administration/users.logout_view/"><i class="fa fa-sign-out"></i></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Logout</a>\n            </li>\n        </ul>\n        <ul class="nav navbar-nav navbar-right navbar-user">\n            <ul class="nav navbar-nav navbar-right navbar-user">\n')
        if request.user.is_authenticated():
            __M_writer('                    <li class="dropdown user-dropdown">\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i>')
            __M_writer(str( user.get_short_name() ))
            __M_writer('<b class="caret"></b></a>\n                        <ul class="dropdown-menu">\n                            <li><a href="/shop/account/"><i class="fa fa-user"></i> Profile</a>\n                            </li>\n                            <li><a href="#"><i class="fa fa-gear"></i> Settings</a>\n                            </li>\n                            <li class="divider"></li>\n                            <li><a href="/administration/users.logout_view/"><i class="fa fa-power-off"></i> Log Out</a>\n                            </li>\n\n                        </ul>\n                    </li>\n')
        else:
            __M_writer('                    <li class="dropdown user-dropdown">\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> Login or Signup<b class="caret"></b></a>\n                        <ul class="dropdown-menu">\n                            <li>\n                                <a href="#" id="show_login_dialog">Login</a>\n                            </li>\n\n                            <li>\n                                <a href="/homepage/signup/">Signup</a>\n                            </li>\n\n                        </ul>\n')
        __M_writer('\n\n\n                    </ul>\n                </li>\n                <li class="divider-vertical"></li>\n            </ul>\n        </ul>\n\n    </div>\n</nav>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'administrationcontent'):
            context['self'].administrationcontent(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_administrationcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def administrationcontent():
            return render_administrationcontent(context)
        __M_writer = context.writer()
        __M_writer('\n    <!-- _________________________The content of the admin will be here _____________________________ -->\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n    <script type="text/javascript" src="http://www.shieldui.com/shared/components/latest/js/shieldui-all.min.js"></script>\n    <script type="text/javascript" src="http://www.prepbootstrap.com/Content/js/gridData.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_appheadlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def appheadlinks():
            return render_appheadlinks(context)
        __M_writer = context.writer()
        __M_writer('\n    <link rel="stylesheet" type="text/css" href="/static/administration/styles/thirdpartystylesheets/massive.css">\n    <link rel="stylesheet" type="text/css" href="/static/administration/styles/thirdpartystylesheets/font-awesome/css/font-awesome.min.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 122, "73": 7, "74": 27, "75": 60, "76": 61, "77": 62, "78": 62, "79": 74, "80": 75, "81": 88, "86": 102, "57": 108, "27": 0, "92": 100, "98": 100, "104": 105, "42": 1, "110": 105, "47": 6, "116": 3, "52": 103, "122": 3, "63": 7}, "source_encoding": "ascii", "uri": "base.htm", "filename": "/Users/rodneycox/chf/administration/templates/base.htm"}
__M_END_METADATA
"""
