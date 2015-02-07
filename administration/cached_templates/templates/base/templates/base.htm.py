# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423014332.483363
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/base/templates/base.htm'
_template_uri = '/base/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['appfooterlinks', 'content', 'appheadlinks']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def appheadlinks():
            return render_appheadlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def appfooterlinks():
            return render_appfooterlinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  \n  <head>\n    <meta charset="UTF-8">\n    <title>base</title>\n    \n')
        __M_writer('    <!-- Latest compiled and minified CSS -->\n    \n    <link href=\'http://fonts.googleapis.com/css?family=Lato:100,300,400,300italic\' rel=\'stylesheet\' type=\'text/css\'>\n    <link rel="stylesheet" type="text/css" href="http://www.shieldui.com/shared/components/latest/css/dark-bootstrap/all.min.css">\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n    <link rel="stylesheet" href="http://www.shieldui.com/shared/components/latest/css/shieldui-all.min.css">\n    <link rel="stylesheet" href="http://www.shieldui.com/shared/components/latest/css/light-bootstrap/all.min.css">\n    <link rel="stylesheet" type="text/css" href="http://www.shieldui.com/shared/components/latest/css/dark-bootstrap/all.min.css">\n    \n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'appheadlinks'):
            context['self'].appheadlinks(**pageargs)
        

        __M_writer('\n\n    \n    \n    <script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n     ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n')
        __M_writer('    \n  \n    </head>\n    <body>\n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n    \n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'appfooterlinks'):
            context['self'].appfooterlinks(**pageargs)
        

        __M_writer('\n     ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n    </body>\n \n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_appfooterlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def appfooterlinks():
            return render_appfooterlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n      \n    \n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_appheadlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def appheadlinks():
            return render_appheadlinks(context)
        __M_writer = context.writer()
        __M_writer('\n        \n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/base/templates/base.htm", "filename": "/Users/rodneycox/chf/base/templates/base.htm", "line_map": {"67": 49, "97": 25, "73": 49, "79": 42, "16": 4, "18": 0, "85": 42, "91": 25, "31": 2, "32": 4, "33": 5, "37": 5, "38": 15, "39": 25, "103": 97, "44": 27, "45": 35, "46": 35, "47": 37, "48": 42, "53": 46, "54": 49, "59": 51, "60": 52, "61": 52}, "source_encoding": "ascii"}
__M_END_METADATA
"""
