# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422663050.790684
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>homepage</title>\n    \n')
        __M_writer('    <!-- Latest compiled and minified CSS -->\n    <link href=\'http://fonts.googleapis.com/css?family=Lato:100,300,400,300italic\' rel=\'stylesheet\' type=\'text/css\'>\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n    \n    <!-- Optional theme -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n\n    <!-- Latest compiled and minified JavaScript -->\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n    <script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n<body>\n    <div class="navbar">\n        <!-- Static navbar -->\n        <div class=\'navbar navbar-inverse navbar-inner\'>\n            <div class=\'container-fluid\'>\n                <div class="navbar-header">\n\n                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n                        <span class="sr-only">Toggle navigation</span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>\n                    <a class="navbar-brand" href="#" style="\n                                                      padding-top: 5px;\n                                                      width: 430px;\n                                                      height: 50px;\n                                                      padding-bottom: -10;\n                                                      margin-top: -10;\n                                                      border-top-width: 10px;\n                                                      padding-bottom: 0px;\n                                                  ">\n                        <!--<img class="nav-logo" src="/static/homepage/media/chf-logo.svg"/>-->\n                        <svg width="350" height="80" viewBox="0 -24 500 100" x="5" y="0" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns" style="padding-top: 10px;">\n                            <g id="Page-1" stroke="none" stroke-width=".75" fill="none" fill-rule="evenodd" sketch:type="MSPage">\n                                <text id="Colonial-Heritage-Fo" y="15px" sketch:type="MSTextLayer" font-family="Edwardian Script ITC" font-size="55.25" font-weight="normal" fill="#FFFFFF">\n                                    <tspan x="-9" y="0">Colonial Heritage Foundation</tspan>\n                                </text>\n                            </g>\n                        </svg>\n                    </a>\n                </div>\n                <div id="navbar" class="navbar-collapse collapse">\n                    <ul class="nav navbar-nav navbar-right">\n                        <li><a href="/about/">About</a>\n                        </li>\n                        <li><a href="/festivals/">Festivals</a>\n                        </li>\n                        <li><a href="/rentals/">Rentals</a>\n                        </li>\n                        <li>\n                            <a href="/store/">Store</a>\n                        </li>\n                        <li>\n                            <a href="/users/">Users</a>\n                        </li>\n                        <li>\n                         <a href="/login/">Login</a>\n                        </li>\n                    </ul>\n                </div>\n                <!--/.nav-collapse -->\n            </div>\n        </div>\n    </div>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n      Site content goes here in sub-templates.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/homepage/templates/base.htm", "line_map": {"33": 5, "34": 15, "35": 27, "36": 27, "37": 27, "42": 87, "43": 90, "44": 90, "45": 90, "16": 4, "18": 0, "51": 85, "57": 85, "27": 2, "28": 4, "29": 5, "63": 57}, "source_encoding": "ascii", "uri": "base.htm"}
__M_END_METADATA
"""
