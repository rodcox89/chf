# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423015147.078616
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/administration/templates/users.htm'
_template_uri = 'users.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['headlinks', 'footlinks', 'administrationcontent']


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
        users = context.get('users', UNDEFINED)
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def administrationcontent():
            return render_administrationcontent(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'administrationcontent'):
            context['self'].administrationcontent(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headlinks():
            return render_headlinks(context)
        __M_writer = context.writer()
        __M_writer('\n    \n')
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


def render_administrationcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def administrationcontent():
            return render_administrationcontent(context)
        __M_writer = context.writer()
        __M_writer('\n    <div id="wrapper">\n\n        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="index.html">\n                    <img class="nav-logo" src="/static/homepage/media/newlogowhitethe.svg">\n\n                </a>\n            </div>\n\n            <div class="collapse navbar-collapse navbar-ex1-collapse">\n                <ul id="active" class="nav navbar-nav side-nav">\n                    <li>\n')
        __M_writer('                    </li>\n                    <li class="selected">\n                        <div class="left-bar"></div>\n                        <a href="users.html"><i class="fa fa-users"></i>  Users \n                            <div class="arrow-left"></div>\n                        </a>\n\n                    </li>\n                    <li>\n                        <a href="#"><i class="fa fa-map-marker"></i>  Locations</a>\n                    </li>\n                    <li>\n                        <a href="#"><i class="fa fa-calendar-o"></i>  Events</a>\n                    </li>\n                    <li>\n                        <a href="#"><i class="fa fa-list-ol"></i>  Rental Items</a>\n                    </li>\n                    <li>\n                        <a href="#"><i class="fa fa-money"></i>  Products </a>\n                        \n                    </li>\n                </ul>\n\n                <ul class="nav navbar-nav navbar-right navbar-user">\n\n                    <li class="dropdown user-dropdown">\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> Rodney Cox<b class="caret"></b></a>\n                        <ul class="dropdown-menu">\n                            <li><a href="#"><i class="fa fa-user"></i> Profile</a>\n                            </li>\n                            <li><a href="#"><i class="fa fa-gear"></i> Settings</a>\n                            </li>\n                            <li class="divider"></li>\n                            <li><a href="#"><i class="fa fa-power-off"></i> Log Out</a>\n                            </li>\n\n                        </ul>\n                    </li>\n                    <li class="divider-vertical"></li>\n                </ul>\n            </div>\n        </nav>\n\n        <div id="page-wrapper">\n\n        \n           <div class="container">\n                <div class="row">\n                    <div class=" col-lg-10 col-lg-offset-1">\n                        <h1 class="">System Users</h1>\n                    </div>            \n                </div>\n            \n            <div class="row">   \n                <div class="col-md-12 col-sm-8 col-lg-10 col-lg-offset-1">\n\n                    <div class="table-responsive">\n                        <table id="mytable" class="table">\n                            <thead>\n                                <th></th>\n                                <th>ID</th>\n                                <th>First</th>\n                                <th>Last</th>\n                                <th>Email</th>\n                                <th>Edit</th>\n                                <th>Delete</th>\n                            </thead>\n                            <tbody>\n                                    \n')
        for user in users:  
            __M_writer('                                        <tr>\n\n                                            <td><input type="checkbox" class="checkthis" /></td>                                  \n                                            <td>')
            __M_writer(str( user.id ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\n')
            __M_writer('                                            <td>\n                                                <p data-placement="top" data-toggle="tooltip" title="Edit">\n                                                    <a href="/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/" class="button btn btn-primary btn-xs" data-title="Edit" data-toggle="modal"><span class="glyphicon glyphicon-pencil"></span>\n                                                    </a>\n                                                </p>\n                                            </td>\n                                            <td>\n                                                <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                                    <button class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal" data-target="#delete"><span class="glyphicon glyphicon-trash"></span>\n                                                    </button>\n                                                </p>\n                                            </td>\n                                            \n                                        </tr>\n')
        __M_writer('                       \n\n\n\n                            </tbody>\n\n                        </table>\n\n                    </div>\n\n')
        __M_writer('\n\n                    </div>\n\n                </div>\n            </div>\n            <div class="row">\n                <div class="col-lg-10 col-lg-offset-1" style="background-color:red;">\n\n                    \n                </div>        \n            </div>\n        </div>\n      \n      \n    </div>\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/administration/templates/users.htm", "uri": "users.htm", "source_encoding": "ascii", "line_map": {"65": 3, "71": 152, "77": 152, "112": 106, "83": 7, "90": 7, "91": 28, "92": 97, "93": 98, "94": 101, "95": 101, "96": 102, "97": 102, "98": 103, "27": 0, "100": 104, "101": 104, "102": 106, "39": 1, "104": 108, "105": 121, "106": 132, "103": 108, "44": 5, "99": 103, "49": 150, "59": 3}}
__M_END_METADATA
"""
