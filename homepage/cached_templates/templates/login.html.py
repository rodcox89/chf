# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425405034.114128
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/login.html'
_template_uri = 'login.html'
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="login">\n    <div class="row">\n        <div class="col-md-12">\n            <h3>Log In</h3>\n        </div>\n\n        <form class="form-horizontal signin-form" method="POST">\n            ')
        __M_writer(str( form.non_field_errors() ))
        __M_writer('\n')
        for field in form:
            __M_writer('            <div class="form-group col-md-12">\n                <!-- <label class="col-md-3 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label> -->\n                <div class="col-md-12">\n                    ')
            __M_writer(str(field))
            __M_writer('\n                </div>\n            </div>\n')
        __M_writer('            <div class="form-group col-md-12">\n                <button type="submit" class="btn btn-primary">Sign In</button><br>\n                Not a user? sign up <a href="/signup/" />Here</a>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "68": 62, "40": 28, "46": 4, "59": 15, "53": 4, "54": 12, "55": 12, "56": 13, "57": 14, "58": 15, "27": 0, "60": 17, "61": 17, "62": 21}, "uri": "login.html", "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/homepage/templates/login.html"}
__M_END_METADATA
"""
