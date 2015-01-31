# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422668386.014453
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/index.html'
_template_uri = 'index.html'
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
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n      <div class="navbar">\n        <!-- Static navbar -->\n        <div class=\'navbar navbar-inverse navbar-inner\'>\n            <div class=\'container-fluid\'>\n                <div class="navbar-header">\n\n                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n                        <span class="sr-only">Toggle navigation</span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>\n                    <a class="navbar-brand" href="#" style="\n                                                      padding-top: 5px;\n                                                      width: 430px;\n                                                      height: 50px;\n                                                      padding-bottom: -10;\n                                                      margin-top: -10;\n                                                      border-top-width: 10px;\n                                                      padding-bottom: 0px;\n                                                  ">\n                        <img class="nav-logo" src="/static/homepage/media/chf-logo.svg"/>\n                       \n                    </a>\n                </div>\n                <div id="navbar" class="navbar-collapse collapse">\n                    <ul class="nav navbar-nav navbar-right">\n                        <li><a href="/about/">About</a>\n                        </li>\n                        <li><a href="/festivals/">Festivals</a>\n                        </li>\n                        <li><a href="/rentals/">Rentals</a>\n                        </li>\n                        <li>\n                            <a href="/store/">Store</a>\n                        </li>\n                        <li>\n                            <a href="/users/">Users</a>\n                        </li>\n                        <li>\n                         <a href="/login/">Login</a>\n                        </li>\n                    </ul>\n                </div>\n                <!--/.nav-collapse -->\n            </div>\n        </div>\n    </div>\n\n\n\n  <div class="container auth">\n    <div id="big-form" class="well auth-box">\n      <form>\n        <fieldset>\n\n          <!-- Form Name -->\n          <legend>Nice form example</legend>\n\n          <div class="btn-group">\n            <a href="index.html" class="btn btn-default">All</a>\n            <a href="example1.html" class="btn btn-default">example 1</a>\n            <a href="example2.html" class="btn btn-default">example 2</a>\n          </div>\n\n\n          <!-- Text input-->\n          <div class="form-group">\n            <label class=" control-label" for="textinput">Username</label>  \n            <div class="">\n              <input id="textinput" name="textinput" placeholder="Username" class="form-control input-md" type="text">\n              <span class="help-block">help</span>  \n            </div>\n          </div>\n\n          <!-- Password input-->\n          <div class="form-group">\n            <label class=" control-label" for="passwordinput">Password</label>\n            <div class="">\n              <input id="passwordinput" name="passwordinput" placeholder="Password" class="form-control input-md" type="password">\n              <span class="help-block">help</span>\n            </div>\n          </div>\n\n          <!-- Select Basic -->\n          <div class="form-group">\n            <label class=" control-label" for="selectbasic">Country</label>\n            <div class="">\n              <select id="selectbasic" name="selectbasic" class="form-control">\n                <option value="1">Option one</option>\n                <option value="2">Option two</option>\n              </select>\n            </div>\n          </div>\n\n          <!-- Multiple Radios -->\n          <div class="form-group">\n            <label class=" control-label" for="radios">Are you awesome</label>\n            <div class="">\n              <div class="radio">\n                <label for="radios-0">\n                  <input name="radios" id="radios-0" value="1" checked="checked" type="radio">\n                  Yes\n                </label>\n              </div>\n              <div class="radio">\n                <label for="radios-1">\n                  <input name="radios" id="radios-1" value="2" type="radio">\n                  No\n                </label>\n              </div>\n            </div>\n          </div>\n\n          <!-- Button -->\n          <div class="form-group">\n            <label class=" control-label" for="singlebutton">Do you like this button</label>\n            <div class="">\n              <button id="singlebutton" name="singlebutton" class="btn btn-primary">Button</button>\n            </div>\n          </div>\n          <div class="form-group">\n            <label class=" control-label" for="singlebutton">And this?</label>\n            <div class="">\n              <button id="singlebutton" name="singlebutton" class="btn btn-default">Button</button>\n            </div>\n          </div>\n\n\n          <!-- Button (Double) -->\n          <div class="form-group">\n            <label class=" control-label" for="button1id">Double the action</label>\n            <div class="">\n              <button id="button1id" name="button1id" class="btn btn-success">Good Button</button>\n              <button id="button2id" name="button2id" class="btn btn-danger">Scary Button</button>\n            </div>\n          </div>\n\n          <!-- File Button --> \n          <div class="form-group">\n            <label class=" control-label" for="filebutton">Avatar</label>\n            <div class="">\n              <input id="filebutton" name="filebutton" class="input-file" type="file">\n            </div>\n          </div>\n\n          <!-- Select Multiple -->\n          <div class="form-group">\n            <label class=" control-label" for="selectmultiple">Category</label>\n            <div class="">\n              <select id="selectmultiple" name="selectmultiple" class="form-control" multiple="multiple">\n                <option value="1">Option one</option>\n                <option value="2">Option two</option>\n              </select>\n            </div>\n          </div>\n\n          <!-- Multiple Radios (inline) -->\n          <div class="form-group">\n            <label class=" control-label" for="radios">Do you like pie?</label>\n            <div class=""> \n              <label class="radio-inline" for="radios-0">\n                <input name="radios" id="radios-0" value="1" checked="checked" type="radio">\n                yes\n              </label> \n              <label class="radio-inline" for="radios-1">\n                <input name="radios" id="radios-1" value="2" type="radio">\n                No\n              </label> \n              <label class="radio-inline" for="radios-2">\n                <input name="radios" id="radios-2" value="3" type="radio">\n                what is pie?\n              </label> \n              <label class="radio-inline" for="radios-3">\n                <input name="radios" id="radios-3" value="4" type="radio">\n                I hate it!\n              </label>\n            </div>\n          </div>\n\n          <!-- Multiple Checkboxes -->\n          <div class="form-group">\n            <label class=" control-label" for="checkboxes">Extra features</label>\n            <div class="">\n              <div class="checkbox">\n                <label for="checkboxes-0">\n                  <input name="checkboxes" id="checkboxes-0" value="1" type="checkbox">\n                  Paper plains\n                </label>\n              </div>\n              <div class="checkbox">\n                <label for="checkboxes-1">\n                  <input name="checkboxes" id="checkboxes-1" value="2" type="checkbox">\n                  Iron man\n                </label>\n              </div>\n            </div>\n          </div>\n\n          <!-- Multiple Checkboxes (inline) -->\n          <div class="form-group">\n            <label class=" control-label" for="checkboxes">Any more?</label>\n            <div class="">\n              <label class="checkbox-inline" for="checkboxes-0">\n                <input name="checkboxes" id="checkboxes-0" value="1" type="checkbox">\n                One\n              </label>\n              <label class="checkbox-inline" for="checkboxes-1">\n                <input name="checkboxes" id="checkboxes-1" value="2" type="checkbox">\n                Two\n              </label>\n              <label class="checkbox-inline" for="checkboxes-2">\n                <input name="checkboxes" id="checkboxes-2" value="3" type="checkbox">\n                Drum and bass\n              </label>\n              <label class="checkbox-inline" for="checkboxes-3">\n                <input name="checkboxes" id="checkboxes-3" value="4" type="checkbox">\n                Dub\n              </label>\n            </div>\n          </div>\n\n          <!-- Search input-->\n          <div class="form-group">\n            <label class=" control-label" for="searchinput">Search Input</label>\n            <div class="">\n              <input id="searchinput" name="searchinput" placeholder="placeholder" class="form-control input-md" type="search">\n              <p class="help-block">help</p>\n            </div>\n          </div>\n\n          <!-- Textarea -->\n          <div class="form-group">\n            <label class=" control-label" for="textarea">Text Area</label>\n            <div class="">                     \n              <textarea class="form-control" id="textarea" name="textarea">default text</textarea>\n            </div>\n          </div>\n\n        </fieldset>\n      </form>\n    </div>\n    <div class="clearfix"></div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/homepage/templates/index.html", "uri": "index.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
