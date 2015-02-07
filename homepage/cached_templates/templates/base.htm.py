# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423010191.001332
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footlinks', 'userheadlinks']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def userheadlinks():
            return render_userheadlinks(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  \n  <head>\n    <meta charset="UTF-8">\n    <title>homepage</title>\n    \n')
        __M_writer('    <!-- Latest compiled and minified CSS -->\n    \n    <link href=\'http://fonts.googleapis.com/css?family=Lato:100,300,400,300italic\' rel=\'stylesheet\' type=\'text/css\'>\n    <link rel="stylesheet" type="text/css" href="http://www.shieldui.com/shared/components/latest/css/dark-bootstrap/all.min.css">\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n    <link rel="stylesheet" href="http://www.shieldui.com/shared/components/latest/css/shieldui-all.min.css">\n    <link rel="stylesheet" href="http://www.shieldui.com/shared/components/latest/css/light-bootstrap/all.min.css">\n    <link rel="stylesheet" type="text/css" href="http://www.shieldui.com/shared/components/latest/css/dark-bootstrap/all.min.css">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'userheadlinks'):
            context['self'].userheadlinks(**pageargs)
        

        __M_writer('\n\n    <!-- Latest compiled and minified JavaScript -->\n\n    <script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n     ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n')
        __M_writer('    \n  \n  </head>\n  <body>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n  \n    \n   \n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n     ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  </body>\n \n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n      \n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_userheadlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def userheadlinks():
            return render_userheadlinks(context)
        __M_writer = context.writer()
        __M_writer('\n     <link rel="stylesheet" type="text/css" href="http://www.shieldui.com/shared/components/latest/css/dark-bootstrap/all.min.css">   \n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "ascii", "line_map": {"64": 39, "70": 39, "76": 45, "16": 4, "82": 45, "88": 23, "94": 23, "31": 2, "32": 4, "33": 5, "18": 0, "100": 94, "37": 5, "38": 15, "43": 25, "44": 33, "45": 33, "46": 35, "51": 41, "56": 47, "57": 48, "58": 48}}
__M_END_METADATA
"""
