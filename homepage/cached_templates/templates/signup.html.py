# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426729750.523786
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/signup.html'
_template_uri = 'signup.html'
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
        __M_writer('\n<div class="login">\n    <div class="row">\n        <div class="col-lg-4 col-lg-offset-4">\n            <h3>Signup</h3>\n\n        <form class="form-horizontal signup-form" method="POST">\n')
        for error in form.non_field_errors():
            __M_writer('                ')
            __M_writer(str( error ))
            __M_writer('\n')
        __M_writer('\n')
        for field in form:
            __M_writer('            <div class="form-group col-lg-12">\n                <label class="col-md-3 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\n                <div class="col-lg-12">\n                    ')
            __M_writer(str(field))
            __M_writer('\n')
            if field.errors != "":
                __M_writer('                        ')
                __M_writer(str( field.errors ))
                __M_writer('\n')
            __M_writer('                </div>\n            </div>\n')
        __M_writer('            <div class="form-group col-md-12">\n                <button type="submit" class="btn btn-primary">Signup</button><br>\n            </div>\n        </form>\n    </div>\n\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 19, "65": 20, "66": 21, "67": 21, "68": 21, "69": 23, "70": 26, "76": 70, "27": 0, "35": 1, "40": 34, "46": 4, "53": 4, "54": 11, "55": 12, "56": 12, "57": 12, "58": 14, "59": 15, "60": 16, "61": 17, "62": 17, "63": 19}, "uri": "signup.html", "filename": "/Users/rodneycox/chf/homepage/templates/signup.html"}
__M_END_METADATA
"""
