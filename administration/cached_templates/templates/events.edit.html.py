# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423371573.689658
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/administration/templates/events.edit.html'
_template_uri = 'events.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['administrationcontent']


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
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'administrationcontent'):
            context['self'].administrationcontent(**pageargs)
        

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
        __M_writer('\n  <div class="container-fluid">\n    <div class="row">\n      <div class="col-lg-4 col-lg-offset-4">\n\n\n\n\n              <form method="POST">\n                  <table>\n                    ')
        __M_writer(str(form.media))
        __M_writer('\n                    ')
        __M_writer(str( form ))
        __M_writer('\n                  </table>\n                  <button type="submit" class="btn btn-default">Submit</button>\n              </form>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/rodneycox/chf/administration/templates/events.edit.html", "uri": "events.edit.html", "line_map": {"56": 14, "35": 1, "53": 3, "54": 13, "55": 13, "40": 21, "57": 14, "27": 0, "46": 3, "63": 57}}
__M_END_METADATA
"""
