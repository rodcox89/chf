# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428353699.205267
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/administration/templates/items.return.html'
_template_uri = 'items.return.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['administrationcontent', 'footlinks']


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
        form = context.get('form', UNDEFINED)
        def administrationcontent():
            return render_administrationcontent(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'administrationcontent'):
            context['self'].administrationcontent(**pageargs)
        

        __M_writer('\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_administrationcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def administrationcontent():
            return render_administrationcontent(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="login">\n    <div class="row">\n\n    </div>\n</div>\n  <div class="container">\n    <div class="row">\n      <div class="col-lg-4 col-lg-offset-4">\n\n\n\n\n              <form method="POST">\n                  <table>\n                    ')
        __M_writer(str( form ))
        __M_writer('\n                  </table>\n                  <button type="submit" class="btn btn-default">Submit</button>\n              </form>\n      </div>\n    </div>\n  </div>\n\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n      <script type="text/javascript" src="http://www.shieldui.com/shared/components/latest/js/shieldui-all.min.js"></script>\n      <script type="text/javascript" src="http://www.prepbootstrap.com/Content/js/gridData.js"></script>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/administration/templates/items.return.html", "source_encoding": "ascii", "uri": "items.return.html", "line_map": {"80": 74, "74": 29, "68": 29, "53": 3, "47": 32, "42": 27, "27": 0, "60": 3, "61": 19, "62": 19, "37": 1}}
__M_END_METADATA
"""
