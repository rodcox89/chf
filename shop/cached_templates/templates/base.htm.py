# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425433942.319223
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footlinks', 'shopcontent', 'appheadlinks', 'content']


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
        def shopcontent():
            return render_shopcontent(context._locals(__M_locals))
        def appheadlinks():
            return render_appheadlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopcontent():
            return render_shopcontent(context)
        __M_writer = context.writer()
        __M_writer('\n    <!-- _________________________The content of the shop will be here _____________________________ -->\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_appheadlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def appheadlinks():
            return render_appheadlinks(context)
        __M_writer = context.writer()
        __M_writer('\n<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\n<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopcontent():
            return render_shopcontent(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopcontent'):
            context['self'].shopcontent(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"97": 9, "110": 13, "67": 16, "40": 1, "73": 11, "45": 8, "91": 3, "79": 11, "50": 14, "105": 9, "85": 3, "55": 18, "116": 110, "27": 0, "61": 16}, "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
