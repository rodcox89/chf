# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423377724.765479
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/administration/templates/venues.html'
_template_uri = 'venues.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footlinks', 'headlinks', 'administrationcontent']


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
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        venues = context.get('venues', UNDEFINED)
        def administrationcontent():
            return render_administrationcontent(context._locals(__M_locals))
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
        __M_writer('\n    <script type="text/javascript" src="http://www.shieldui.com/shared/components/latest/js/shieldui-all.min.js"></script>\n    <script type="text/javascript" src="http://www.prepbootstrap.com/Content/js/gridData.js"></script>\n')
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


def render_administrationcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        venues = context.get('venues', UNDEFINED)
        def administrationcontent():
            return render_administrationcontent(context)
        __M_writer = context.writer()
        __M_writer('\n    <div id="wrapper">\n\n        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="index.html">\n                    <img class="nav-logo" src="/static/homepage/media/chflatowhite.svg">\n\n                </a>\n            </div>\n\n            <div class="collapse navbar-collapse navbar-ex1-collapse">\n                <ul id="active" class="nav navbar-nav side-nav">\n                    <li>\n')
        __M_writer('                    </li>\n                    <li>\n                        <a href="/administration/users/"><i class="fa fa-users"></i>&nbsp;&nbsp;&nbsp;&nbsp;Users</a>\n                    </li>\n                    <li>\n                        <a href="/administration/locations/"><i class="fa fa-map-marker"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Locations</a>\n                    </li>\n                    <li>\n                        <a href="/administration/events/"><i class="fa fa-calendar-o"></i>&nbsp;&nbsp;&nbsp;&nbsp; Events</a>\n                    </li>\n                    <li>\n                        <a href="/administration/items/"><i class="fa fa-list-ol"></i>&nbsp;&nbsp;&nbsp;&nbsp; Rental Items</a>\n                    </li>\n                    <li>\n                        <a href="/administration/products/"><i class="fa fa-money"></i>&nbsp;&nbsp;&nbsp;&nbsp;Products</a>\n                    </li>\n                    <li class="selected">\n                        <div class="left-bar"></div>\n                        <a href="/administration/venues/"><i class="fa fa-qrcode"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Venues\n                        <div class="arrow-left"></div>\n                        </a>\n\n                    </li>\n                </ul>\n\n                <ul class="nav navbar-nav navbar-right navbar-user">\n\n                    <li class="dropdown user-dropdown">\n                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> Rodney Cox<b class="caret"></b></a>\n                        <ul class="dropdown-menu">\n                            <li><a href="#"><i class="fa fa-user"></i> Profile</a>\n                            </li>\n                            <li><a href="#"><i class="fa fa-gear"></i> Settings</a>\n                            </li>\n                            <li class="divider"></li>\n                            <li><a href="/administration/users.logout_view/"><i class="fa fa-power-off"></i> Log Out</a>\n                            </li>\n\n                        </ul>\n                    </li>\n                    <li class="divider-vertical"></li>\n                </ul>\n            </div>\n        </nav>\n\n        <div id="page-wrapper">\n\n\n           <div class="container">\n                <div class="row">\n                    <div class=" col-lg-5 col-lg-offset-1">\n                        <h1 class="">Venues</h1>\n\n                    </div>\n                    <div class="col-lg-2 col-lg-offset-3">\n                      <a href="/administration/venues.create/" class="btn btn-default">\n                          New Venue\n                      </a>\n                    </div>\n                </div>\n\n            <div class="row">\n                <div class="col-md-12 col-sm-8 col-lg-10 col-lg-offset-1">\n\n                    <div class="table-responsive">\n                        <table id="mytable" class="table">\n                            <thead>\n                                <th></th>\n                                <th>ID</th>\n                                <th>Name</th>\n                                <th>Description</th>\n                                <th>Address</th>\n                                <th>City</th>\n                                <th>State</th>\n                                <th>Zip</th>\n                                <th>Edit</th>\n                                <th>Delete</th>\n                            </thead>\n                            <tbody>\n\n')
        for venue in venues:
            __M_writer('                                        <tr>\n\n                                            <td><input type="checkbox" class="checkthis" /></td>\n                                            <td>')
            __M_writer(str( venue.id ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( venue.name ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( venue.description ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( venue.address ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( venue.city ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( venue.state ))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( venue.zip_code ))
            __M_writer('</td>\n\n                                            <td>\n                                                <p data-placement="top" data-toggle="tooltip" title="Edit">\n                                                    <a href="/administration/venues.edit/')
            __M_writer(str( venue.id ))
            __M_writer('/" class="button btn btn-primary btn-xs" data-title="Edit" data-toggle="modal"><span class="glyphicon glyphicon-pencil"></span>\n                                                    </a>\n                                                </p>\n                                            </td>\n                                            <td>\n                                                <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                                    <a href="/administration/venues.remove/')
            __M_writer(str( venue.id ))
            __M_writer('" class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal"><span class="glyphicon glyphicon-trash"></span>\n                                                    </a>\n                                                </p>\n                                            </td>\n\n                                        </tr>\n')
        __M_writer('\n\n\n\n                            </tbody>\n\n                        </table>\n\n                    </div>\n\n\n')
        __M_writer('\n\n                    </div>\n\n                </div>\n            </div>\n\n        </div>\n\n\n    </div>\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "venues.html", "line_map": {"66": 163, "107": 119, "113": 136, "72": 3, "108": 119, "78": 3, "84": 7, "27": 0, "92": 29, "93": 109, "94": 110, "95": 113, "96": 113, "97": 114, "98": 114, "99": 115, "100": 115, "101": 116, "102": 116, "39": 1, "104": 117, "105": 118, "106": 118, "103": 117, "44": 5, "109": 123, "110": 123, "111": 129, "112": 129, "49": 161, "91": 7, "54": 166, "120": 114, "114": 148, "60": 163}, "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/administration/templates/venues.html"}
__M_END_METADATA
"""
