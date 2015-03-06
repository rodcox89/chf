# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425404680.946546
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/administration/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


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
        __M_writer = context.writer()
        __M_writer('\n\n\n\n<div class="login">\n    <div class="row">\n        <div class="col-md-12">\n            <h3>Log In</h3>\n        </div>\n\n        <form class="form-horizontal signin-form" method="POST">\n            ')
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
{"line_map": {"33": 1, "34": 12, "35": 12, "36": 13, "37": 14, "38": 15, "39": 15, "40": 17, "41": 17, "42": 21, "48": 42, "27": 0}, "uri": "login.html", "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/administration/templates/login.html"}
__M_END_METADATA
"""
