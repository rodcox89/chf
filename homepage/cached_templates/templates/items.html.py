# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422667070.917301
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/items.html'
_template_uri = 'items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<table-responsive>\n  <table id="users_table" class="table table-bordered table-default">\n    <tr>\n      <td>ID</td>\n      <td>First</td>\n      <td>Last</td>\n      <td>Email</td>\n      <td>Actions</td>\n    </tr>\n')
        for user in users:
            __M_writer('    <tr>\n      <td>')
            __M_writer(str( user.id ))
            __M_writer('</td>\n      <td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\n      <td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\n      <td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\n      <td>Edit | Delete</td>\n    </tr>\n')
        __M_writer('  </table>\n</table-responsive>\n  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/homepage/templates/items.html", "uri": "items.html", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 13, "54": 14, "55": 15, "56": 15, "57": 16, "58": 16, "59": 17, "60": 17, "61": 18, "62": 18, "63": 22}, "source_encoding": "ascii"}
__M_END_METADATA
"""
