# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423272771.105675
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
        __M_writer = context.writer()
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="container auth">\n    <div id="big-form" class="well auth-box">\n      <form>\n        <fieldset>\n\n          <!-- Form Name -->\n          <legend>Login Here</legend>\n\n          <!-- Text input-->\n          <div class="form-group">\n\n            <div class="">\n              <input id="textinput" name="textinput" placeholder="Username" class="form-control input-md" type="text">\n\n            </div>\n          </div>\n\n          <!-- Password input-->\n          <div class="form-group">\n\n            <div class="">\n              <input id="passwordinput" name="passwordinput" placeholder="Password" class="form-control input-md" type="password">\n              <span class="help-block">help</span>\n            </div>\n          </div>\n          <!-- Button (Double) -->\n          <div class="form-group">\n            <div class="">\n              <a href="/users/" id="button1id" name="button1id" class="btn btn-success">Login</a>\n            </div>\n          </div>\n        </fieldset>\n      </form>\n    </div>\n    <div class="clearfix"></div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "login.html", "line_map": {"34": 1, "51": 3, "39": 40, "57": 51, "27": 0, "45": 3}, "source_encoding": "ascii", "filename": "/Users/rodneycox/chf/homepage/templates/login.html"}
__M_END_METADATA
"""
