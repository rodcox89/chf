# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428550796.736093
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/administration/templates/items.itemreturn.html'
_template_uri = 'items.itemreturn.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="return-modal">\n    <form class="form-horizontal signin-form"id="return-form" method="POST" action="/administration/items.return_rental/')
        __M_writer(str(rental.id))
        __M_writer('">\n')
        for field in form:
            __M_writer('        <div class="form-group">\n            <label class="col-md-3 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\n            <div class="col-md-8">\n                ')
            __M_writer(str(field))
            __M_writer('\n                <p>')
            __M_writer(str(field.errors))
            __M_writer('</p>\n            </div>\n        </div>\n')
        __M_writer('        <div class="col-md-offset-2 col-md-2 save-btn-col">\n            <button type="submit" class="btn btn-lg btn-white">Save</button>\n        </div>\n    </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 11, "65": 12, "66": 12, "27": 0, "36": 1, "37": 2, "73": 67, "42": 21, "48": 4, "67": 16, "56": 4, "57": 6, "58": 6, "59": 7, "60": 8, "61": 9, "62": 9, "63": 11}, "uri": "items.itemreturn.html", "filename": "/Users/rodneycox/chf/administration/templates/items.itemreturn.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
