# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425788861.155113
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/confirmation.html'
_template_uri = 'confirmation.html'
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
        __M_writer = context.writer()
        __M_writer("\n<h1>Thanks, We'll get your stuff to you ASAP!!!</h1>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/confirmation.html", "uri": "confirmation.html", "line_map": {"34": 1, "51": 3, "39": 5, "57": 51, "27": 0, "45": 3}}
__M_END_METADATA
"""
