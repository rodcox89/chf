# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428550202.098673
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/administration/templates/items.html'
_template_uri = 'items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['administrationcontent', 'headlinks', 'footlinks']


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
        def administrationcontent():
            return render_administrationcontent(context._locals(__M_locals))
        sixties = context.get('sixties', UNDEFINED)
        items = context.get('items', UNDEFINED)
        nineties = context.get('nineties', UNDEFINED)
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        overdue_items = context.get('overdue_items', UNDEFINED)
        thirties = context.get('thirties', UNDEFINED)
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


def render_administrationcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def administrationcontent():
            return render_administrationcontent(context)
        sixties = context.get('sixties', UNDEFINED)
        items = context.get('items', UNDEFINED)
        nineties = context.get('nineties', UNDEFINED)
        overdue_items = context.get('overdue_items', UNDEFINED)
        thirties = context.get('thirties', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="wrapper">\n        <div id="page-wrapper">\n            <div class="container">\n                <div class="row">\n                    <div class=" col-lg-5 col-lg-offset-1">\n                        <h1 class="">Rental Items</h1>\n                    </div>\n                    <!-- _________________________hiding new Item button_____________________________ -->\n                    <div class="col-lg-2 col-lg-offset-3">\n                        <a href="/administration/items.create/" class="btn btn-default">\n                          New Item\n                      </a>\n                    </div>\n                </div>\n                <ul id="tabs" class="nav nav-tabs" data-tabs="tabs">\n                    <li class="active tabitha" id="in"><a href="#tabone" class="tabithamiddle" data-toggle="tab"> In </a></li>\n                    <li class="tabitha"><a href="#tabtwo" class="tabithamiddle" data-toggle="tab">Out</a></li>\n                    <li class="tabitha"><a href="#tabthree" class="tabithamiddle" data-toggle="tab">Overdue</a></li>\n                </ul>\n                <div id="my-tab-content" class="tab-content">\n                    <div class="tab-pane active" id="tabone">\n                        <!-- _________________________in_____________________________ -->\n                        <div class="row">\n                            <div class=" col-lg-5 col-lg-offset-1">\n                                <h2 class="">In</h2>\n                            </div>\n                        </div>\n                        <div class="row">\n                            <div class="col-md-12 col-sm-8 col-lg-10 col-lg-offset-1">\n                                <div class="table-responsive">\n                                    <table id="mytable" class="table">\n                                        <thead>\n                                            <th></th>\n                                            <th>ID</th>\n                                            <th>Name</th>\n                                            <th>Description</th>\n                                            <th>Value</th>\n                                            <th>Edit</th>\n                                            <th>Delete</th>\n                                            <th>Rent</th>\n                                        </thead>\n                                        <tbody>\n')
        for item in items:
            if item.is_available == True:
                __M_writer('                                                <tr>\n                                                    <td>\n                                                        <input type="checkbox" class="checkthis" />\n                                                    </td>\n                                                    <td>')
                __M_writer(str( item.id ))
                __M_writer('</td>\n                                                    <td>')
                __M_writer(str( item.name ))
                __M_writer('</td>\n                                                    <td>')
                __M_writer(str( item.description ))
                __M_writer('</td>\n                                                    <td>')
                __M_writer(str( item.value ))
                __M_writer('</td>\n                                                    <!-- _________________________if item is available do_____________________________ -->\n                                                    <td>\n                                                        <p data-placement="top" data-toggle="tooltip" title="Edit">\n                                                            <a href="/administration/items.edit/')
                __M_writer(str( item.id ))
                __M_writer('/" class="button btn btn-primary btn-xs" data-title="Edit" data-toggle="modal">\n                                                                <span class="glyphicon glyphicon-pencil"></span>\n                                                            </a>\n                                                        </p>\n                                                    </td>\n                                                    <td>\n                                                        <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                                            <a href="/administration/items.remove/')
                __M_writer(str( item.id ))
                __M_writer('" class="btn btn-danger btn-xs" data-title="Delete" data-toggle="modal">\n                                                                <span class="glyphicon glyphicon-trash"></span>\n                                                            </a>\n                                                        </p>\n                                                    </td>\n                                                    <td>\n                                                        <p data-placement="top" data-toggle="tooltip" title="Delete">\n                                                            <a href="/administration/items.rent/')
                __M_writer(str( item.id ))
                __M_writer('" class="button btn btn-primary btn-xs" data-title="Delete" data-toggle="modal">\n                                                                Rent\n                                                            </a>\n                                                        </p>\n                                                    </td>\n                                                </tr>\n')
        __M_writer('                                        </tbody>\n                                    </table>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                    <div class="tab-pane" id="tabtwo">\n                        <!-- _________________________out_____________________________ -->\n                        <div class="row">\n                            <div class=" col-lg-5 col-lg-offset-1">\n                                <h2 class="">Out</h2>\n                            </div>\n                        </div>\n                        <div class="row">\n                            <div class="col-md-12 col-sm-8 col-lg-10 col-lg-offset-1">\n                                <div class="table-responsive">\n                                    <table id="mytable" class="table">\n                                        <thead>\n                                            <th></th>\n                                            <th>ID</th>\n                                            <th>Item</th>\n                                            <th>Customer</th>\n                                            <th>Date Rented</th>\n                                            <th>Due Date</th>\n                                            <th>Return</th>\n                                        </thead>\n                                        <tbody>\n')
        for rental in overdue_items:
            __M_writer('                                            <tr>\n                                                <td><input type="checkbox" class="checkthis" /></td>\n                                                <td>')
            __M_writer(str( rental.id ))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str( rental.name ))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str( rental.customer ))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str( rental.rental_date ))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str( rental.due_date ))
            __M_writer('</td>\n                                                <td>\n                                                    <p data-placement="top" title="Delete">\n                                                        <a href="#" class="button btn btn-primary btn-xs return" data-rid="')
            __M_writer(str( rental.id ))
            __M_writer('">\n                                                            <span>Return</span>\n                                                        </a>\n                                                    </p>\n                                                </td>\n                                            </tr>\n')
        __M_writer('                                        </tbody>\n                                    </table>\n                                </div>\n                                <div class="clearfix"></div>\n                            </div>\n                        </div>\n                    </div>\n                    <div class="tab-pane" id="tabthree">\n                        <div class="row">\n                            <br>\n                            <div class="col-md-10 col-md-offset-1 col-sm-4">\n                                <ul id="tabs" class="nav nav-tabs" data-tabs="tabs">\n                                    <li class="tabitha mini" id="in"><a href="#thirty" class="tabithamiddle" data-toggle="tab"> 30 Days </a></li>\n                                    <li class="tabitha mini"><a href="#sixty" class="tabithamiddle" data-toggle="tab">60 Days</a></li>\n                                    <li class="tabitha mini"><a href="#ninety" class="tabithamiddle" data-toggle="tab">90 Days</a></li>\n                                </ul>\n                                <div id="my-tab-content" class="tab-content">\n\n                                    <!-- Over Thirty -->\n                                    <div class="tab-pane active" id="thirty">\n                                        <div class="row">\n                                            <div class="col-md-10 col-md-offset-1 col-sm-4">\n                                                <div class="table-responsive">\n                                                    <table id="mytable" class="table">\n                                                        <thead>\n                                                            <th></th>\n                                                            <th>ID</th>\n                                                            <th>Name</th>\n                                                            <th>Rental Date</th>\n                                                            <th>Due Date </th>\n                                                        </thead>\n                                                        <tbody>\n')
        for item in thirties:
            __M_writer('                                                            <tr>\n                                                                <td>\n                                                                    <input type="checkbox" class="checkthis" />\n                                                                </td>\n                                                                <td>')
            __M_writer(str( item.id ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.customer ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.rental_date ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.due_date ))
            __M_writer('</td>\n                                                            </tr>\n')
        __M_writer('                                                        </tbody>\n                                                    </table>\n                                                    <a href = "administration/items.sendmail/" data-batch="30" type="button" class="btn btn-medium btn-email btn-default">\n                                                        Send Batch Email\n                                                    </a>\n                                                </div>\n                                            </div>\n                                        </div>\n                                    </div>\n\n                                    <!-- Over Sixty -->\n                                    <div class="tab-pane active" id="sixty">\n                                        <div class="row">\n                                            <div class="col-md-10 col-md-offset-1 col-sm-4">\n                                                <div class="table-responsive">\n                                                    <table id="mytable" class="table">\n                                                        <thead>\n                                                            <th></th>\n                                                            <th>ID</th>\n                                                            <th>Name</th>\n                                                            <th>Rental Date</th>\n                                                            <th>Due Date </th>\n                                                        </thead>\n                                                        <tbody>\n')
        for item in sixties:
            __M_writer('                                                            <tr>\n                                                                <td>\n                                                                    <input type="checkbox" class="checkthis" />\n                                                                </td>\n                                                                <td>')
            __M_writer(str( item.id ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.customer ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.rental_date ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.due_date ))
            __M_writer('</td>\n                                                            </tr>\n')
        __M_writer('                                                        </tbody>\n                                                    </table>\n                                                    <a href = "administration/items.sendmail/" data-batch="60" type="button" class="btn btn-medium btn-email btn-default">\n                                                        Send Batch Email\n                                                    </a>\n                                                </div>\n                                            </div>\n                                        </div>\n                                    </div>\n\n\n                                    <!-- Over Ninety -->\n                                    <div class="tab-pane active" id="ninety">\n                                        <div class="row">\n                                            <div class="col-md-10 col-md-offset-1 col-sm-4">\n                                                <div class="table-responsive">\n                                                    <table id="mytable" class="table">\n                                                        <thead>\n                                                            <th></th>\n                                                            <th>ID</th>\n                                                            <th>Name</th>\n                                                            <th>Rental Date</th>\n                                                            <th>Due Date </th>\n                                                        </thead>\n                                                        <tbody>\n')
        for item in nineties:
            __M_writer('                                                            <tr>\n                                                                <td>\n                                                                    <input type="checkbox" class="checkthis" />\n                                                                </td>\n                                                                <td>')
            __M_writer(str( item.id ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.customer ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.rental_date ))
            __M_writer('</td>\n                                                                <td>')
            __M_writer(str( item.due_date ))
            __M_writer('</td>\n                                                            </tr>\n')
        __M_writer('                                                        </tbody>\n                                                    </table>\n                                                    <a href = "administration/items.sendmail/" data-batch="90" type="button" class="btn btn-medium btn-email btn-default">\n                                                        Send Batch Email\n                                                    </a>\n                                                </div>\n                                            </div>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
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
{"line_map": {"128": 204, "129": 204, "130": 207, "131": 232, "132": 233, "133": 237, "134": 237, "135": 238, "136": 238, "137": 239, "138": 239, "139": 240, "140": 240, "141": 243, "147": 3, "171": 165, "153": 3, "27": 0, "159": 262, "165": 262, "43": 1, "48": 5, "53": 260, "58": 265, "64": 7, "75": 7, "76": 50, "77": 51, "78": 52, "79": 56, "80": 56, "81": 57, "82": 57, "83": 58, "84": 58, "85": 59, "86": 59, "87": 63, "88": 63, "89": 70, "90": 70, "91": 77, "92": 77, "93": 85, "94": 112, "95": 113, "96": 115, "97": 115, "98": 116, "99": 116, "100": 117, "101": 117, "102": 118, "103": 118, "104": 119, "105": 119, "106": 122, "107": 122, "108": 129, "109": 161, "110": 162, "111": 166, "112": 166, "113": 167, "114": 167, "115": 168, "116": 168, "117": 169, "118": 169, "119": 172, "120": 196, "121": 197, "122": 201, "123": 201, "124": 202, "125": 202, "126": 203, "127": 203}, "uri": "items.html", "filename": "/Users/rodneycox/chf/administration/templates/items.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
