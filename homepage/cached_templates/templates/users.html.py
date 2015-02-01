# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422787942.172678
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'headlinks', 'footlinks']


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
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div id="wrapper">\n\n        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="index.html">\n                    <img class="nav-logo" src="/static/homepage/media/newlogowhitethe.svg">\n\n                </a>\n            </div>\n\n            <div class="collapse navbar-collapse navbar-ex1-collapse">\n                <ul id="active" class="nav navbar-nav side-nav">\n                    <li class="selected"><a href="users.html"><i class="fa fa-users"></i>  Users</a>\n                    </li>\n                    <li><a href="#"><i class="fa fa-map-marker"></i>  Locations</a>\n                    </li>\n                    <li><a href="#"><i class="fa fa-calendar-o"></i>  Events</a>\n                    </li>\n                    <li><a href="#"><i class="fa fa-list-ol"></i>  Rental Items</a>\n                    </li>\n                    <li><a href="#"><i class="fa fa-money"></i>  Products </a>\n                        <div class="arrow-right"></div>\n                    </li>\n                </ul>\n\n                <ul class="nav navbar-nav navbar-right navbar-user">\n\n                    <li class="dropdown user-dropdown">\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> Rodney Cox<b class="caret"></b></a>\n                        <ul class="dropdown-menu">\n                            <li><a href="#"><i class="fa fa-user"></i> Profile</a>\n                            </li>\n                            <li><a href="#"><i class="fa fa-gear"></i> Settings</a>\n                            </li>\n                            <li class="divider"></li>\n                            <li><a href="#"><i class="fa fa-power-off"></i> Log Out</a>\n                            </li>\n\n                        </ul>\n                    </li>\n                    <li class="divider-vertical"></li>\n                </ul>\n            </div>\n        </nav>\n\n        <div id="page-wrapper">\n            <div class="row">\n                <h1 class="col-md-8 pull-left">System Users</h1>\n                <div class="col-md-2"> <img class="nav-logo" src="/static/homepage/media/svgflag.svg"></div>              \n            </div>\n            <div class="row">   \n                <div class="col-md-12 col-sm-8 col-lg-12">\n\n                    <div class="table-responsive">\n\n\n                        <table id="mytable" class="table table-bordred ">\n\n                            <thead>\n\n                                <th></th>\n                                <th>First Name</th>\n                                <th>Last Name</th>\n                                <th>Address</th>\n                                <th>Email</th>\n                                <th>Contact</th>\n                                <th>Edit</th>\n\n                                <th>Delete</th>\n                            </thead>\n                            <tbody>\n\n                                <tr>\n                                    <td>\n                                        <input type="checkbox" class="checkthis" />\n                                    </td>\n                                    <td>Mohsin</td>\n                                    <td>Irshad</td>\n                                    <td>CB 106/107 Street # 11 Wah Cantt Islamabad Pakistan</td>\n                                    <td>isometric.mohsin@gmail.com</td>\n                                    <td>+923335586757</td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Edit">\n                                            <button class="btn btn-primary btn-xs" data-title="Edit" data-toggle="modal" data-target="#edit"><span class="glyphicon glyphicon-pencil"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                            <button class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal" data-target="#delete"><span class="glyphicon glyphicon-trash"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                </tr>\n\n                                <tr>\n                                    <td>\n                                        <input type="checkbox" class="checkthis" />\n                                    </td>\n                                    <td>Mohsin</td>\n                                    <td>Irshad</td>\n                                    <td>CB 106/107 Street # 11 Wah Cantt Islamabad Pakistan</td>\n                                    <td>isometric.mohsin@gmail.com</td>\n                                    <td>+923335586757</td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Edit">\n                                            <button class="btn btn-primary btn-xs" data-title="Edit" data-toggle="modal" data-target="#edit"><span class="glyphicon glyphicon-pencil"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                            <button class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal" data-target="#delete"><span class="glyphicon glyphicon-trash"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                </tr>\n\n\n                                <tr>\n                                    <td>\n                                        <input type="checkbox" class="checkthis" />\n                                    </td>\n                                    <td>Mohsin</td>\n                                    <td>Irshad</td>\n                                    <td>CB 106/107 Street # 11 Wah Cantt Islamabad Pakistan</td>\n                                    <td>isometric.mohsin@gmail.com</td>\n                                    <td>+923335586757</td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Edit">\n                                            <button class="btn btn-primary btn-xs" data-title="Edit" data-toggle="modal" data-target="#edit"><span class="glyphicon glyphicon-pencil"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                            <button class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal" data-target="#delete"><span class="glyphicon glyphicon-trash"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                </tr>\n\n\n\n                                <tr>\n                                    <td>\n                                        <input type="checkbox" class="checkthis" />\n                                    </td>\n                                    <td>Mohsin</td>\n                                    <td>Irshad</td>\n                                    <td>CB 106/107 Street # 11 Wah Cantt Islamabad Pakistan</td>\n                                    <td>isometric.mohsin@gmail.com</td>\n                                    <td>+923335586757</td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Edit">\n                                            <button class="btn btn-primary btn-xs" data-title="Edit" data-toggle="modal" data-target="#edit"><span class="glyphicon glyphicon-pencil"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                            <button class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal" data-target="#delete"><span class="glyphicon glyphicon-trash"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                </tr>\n\n\n                                <tr>\n                                    <td>\n                                        <input type="checkbox" class="checkthis" />\n                                    </td>\n                                    <td>Mohsin</td>\n                                    <td>Irshad</td>\n                                    <td>CB 106/107 Street # 11 Wah Cantt Islamabad Pakistan</td>\n                                    <td>isometric.mohsin@gmail.com</td>\n                                    <td>+923335586757</td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Edit">\n                                            <button class="btn btn-primary btn-xs" data-title="Edit" data-toggle="modal" data-target="#edit"><span class="glyphicon glyphicon-pencil"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                    <td>\n                                        <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                            <button class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal" data-target="#delete"><span class="glyphicon glyphicon-trash"></span>\n                                            </button>\n                                        </p>\n                                    </td>\n                                </tr>\n\n\n\n\n\n                            </tbody>\n\n                        </table>\n\n                        <div class="clearfix"></div>\n\n\n                    </div>\n\n                </div>\n            </div>\n        </div>\n        <div class="container text-center">\n    <hr />\n  <div class="row">\n    <div class="col-MD-12">\n      <div class="col-md-2">\n        <ul class="nav nav-pills nav-stacked">\n          <li><a href="#">About us</a></li>\n          <li><a href="#">Blog</a></li>\n        </ul>\n      </div>\n      <div class="col-md-2">\n        <ul class="nav nav-pills nav-stacked">\n          <li><a href="#">Product for Mac</a></li>\n          <li><a href="#">Product for Windows</a></li>\n        </ul>\n      </div>\n      <div class="col-md-2">\n        <ul class="nav nav-pills nav-stacked">\n          <li><a href="#">Web analytics</a></li>\n          <li><a href="#">Presentations</a></li>          \n        </ul>\n      </div>\n      <div class="col-md-2">\n        <ul class="nav nav-pills nav-stacked">\n          <li><a href="#">Product Help</a></li>\n          <li><a href="#">Developer API</a></li>\n        </ul>\n      </div>  \n    </div>\n  </div>\n  <hr>\n    <div class="row">\n        <div class="col-md-10-12">\n            <ul class="nav nav-pills nav-justified">\n                <li><a href="/"> 2013 Company Name.</a></li>\n                <li><a href="#">Terms of Service</a></li>\n                <li><a href="#">Privacy</a></li>\n            </ul>\n        </div>\n    </div>\n</div>\n    </div>\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headlinks():
            return render_headlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"48": 265, "64": 7, "82": 267, "27": 0, "70": 3, "38": 1, "88": 267, "58": 7, "43": 5, "76": 3, "94": 88}, "uri": "users.html", "filename": "/Users/rodneycox/chf/homepage/templates/users.html"}
__M_END_METADATA
"""
