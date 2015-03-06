# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425578146.036197
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/index.html'
_template_uri = 'index.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div>\n    <button id="show_login_dialog" type="submit" class="btn btn-success">Login Here\n\n    </button>\n    </div>\n\n\n\n\n\n<!-- _________________________video 2_____________________________ -->\n    <!-- <div id="loginform_container">\n\n    <form id="loginform" method="POST" action="/shop/index.loginform/">\n\n        <table>\n\n        </table>\n            <input type="submit"/>\n\n\n    </form>\n    </div> -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"34": 1, "51": 3, "39": 27, "57": 51, "27": 0, "45": 3}, "filename": "/Users/rodneycox/chf/shop/templates/index.html", "uri": "index.html"}
__M_END_METADATA
"""
