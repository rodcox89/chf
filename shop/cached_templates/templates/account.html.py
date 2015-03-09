# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425768970.201622
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/account.html'
_template_uri = 'account.html'
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
        user = context.get('user', UNDEFINED)
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
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="container">\n    <table class="table-condensed col-md-10 col-offset-1"><h2>Your Account Details<a href="#" class="edit_user button btn btn-primary btn-md" id="pencilcasing" data-pid="')
        __M_writer(str( user.id ))
        __M_writer('" data-title="Edit" data-toggle="modal"><span id="edit_icon" class="glyphicon glyphicon-pencil"></span></a></h2>\n\n\n\n            <th>Current Info</th>\n\n\n        <tbody>\n            <tr>\n                <td>')
        __M_writer(str( user.first_name ))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str( user.last_name ))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str( user.username ))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str( user.email ))
        __M_writer('</td>\n            </tr>\n            <tr>\n                <td><a href="#" class="button btn btn-primary btn-sm change_password " >Change Password</a></td>\n            </tr>\n\n\n        </td>\n\n        </tbody>\n    </table>\n\n\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "account.html", "filename": "/Users/rodneycox/chf/shop/templates/account.html", "source_encoding": "ascii", "line_map": {"35": 1, "69": 63, "40": 39, "46": 3, "59": 17, "53": 3, "54": 5, "55": 5, "56": 14, "57": 14, "58": 17, "27": 0, "60": 20, "61": 20, "62": 23, "63": 23}}
__M_END_METADATA
"""
