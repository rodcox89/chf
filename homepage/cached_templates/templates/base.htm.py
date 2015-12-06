# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428526318.008389
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footlinks', 'userheadlinks']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def userheadlinks():
            return render_userheadlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n\n  <head>\n    <meta charset="UTF-8">\n    <title>homepage</title>\n\n')
        __M_writer('    <!-- Latest compiled and minified CSS -->\n\n    <link href=\'http://fonts.googleapis.com/css?family=Lato:100,300,400,300italic\' rel=\'stylesheet\' type=\'text/css\'>\n    <link rel="stylesheet" type="text/css" href="http://www.shieldui.com/shared/components/latest/css/dark-bootstrap/all.min.css">\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n    <link rel="stylesheet" href="http://www.shieldui.com/shared/components/latest/css/shieldui-all.min.css">\n    <link rel="stylesheet" href="http://www.shieldui.com/shared/components/latest/css/light-bootstrap/all.min.css">\n    <link rel="stylesheet" type="text/css" href="http://www.shieldui.com/shared/components/latest/css/dark-bootstrap/all.min.css">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'userheadlinks'):
            context['self'].userheadlinks(**pageargs)
        

        __M_writer('\n\n    <!-- Latest compiled and minified JavaScript -->\n\n    <script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n    <script src="/static/base/media/jquery.form.js"></script>\n    <script src="/static/base/media/jquery.loadmodal.js"></script>\n\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n     ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n')
        __M_writer('\n\n  </head>\n  <body>\n      <div class="navbar">\n        <!-- Static navbar -->\n        <div class=\'navbar navbar-inverse navbar-inner\'>\n            <div class=\'container-fluid\'>\n                <div class="navbar-header">\n\n                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n                        <span class="sr-only">Toggle navigation</span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>\n                    <a class="navbar-brand" href="/homepage/festivals/" style="\n                                                      padding-top: 5px;\n                                                      width: 430px;\n                                                      height: 50px;\n                                                      padding-bottom: -10;\n                                                      margin-top: -10;\n                                                      border-top-width: 10px;\n                                                      padding-bottom: 0px;\n                                                  ">\n                        <img class="nav-logo" src="/static/homepage/media/newLogowhitethe.svg"/>\n\n                    </a>\n                </div>\n                <div id="navbar" class="navbar-collapse collapse">\n                    <ul class="nav navbar-nav">\n                        <li><a href="/festivals/">Festivals</a>\n                        </li>\n                        <li><a href="/shop/items">Rental Shop</a>\n                        </li>\n                        <li>\n                            <a href="/shop/products/">Products</a>\n                        </li>\n                        <li>\n                            <a href="/administration/users/">Admin</a>\n                        </li>\n                    </ul>\n                    <ul class="nav navbar-nav navbar-right navbar-user">\n                        <ul class="nav navbar-nav navbar-right navbar-user">\n')
        if request.user.is_authenticated():
            __M_writer('                                <li class="dropdown user-dropdown">\n                                    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i>')
            __M_writer(str( user.get_short_name() ))
            __M_writer('<b class="caret"></b></a>\n                                    <ul class="dropdown-menu">\n                                        <li><a href="/shop/account/"><i class="fa fa-user"></i> Profile</a>\n                                        </li>\n                                        <li><a href="#"><i class="fa fa-gear"></i> Settings</a>\n                                        </li>\n                                        <li class="divider"></li>\n                                        <li><a href="/administration/users.logout_view/"><i class="fa fa-power-off"></i> Log Out</a>\n                                        </li>\n\n                                    </ul>\n                                </li>\n')
        else:
            __M_writer('                                <li class="dropdown user-dropdown">\n                                    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> Login or Signup<b class="caret"></b></a>\n                                    <ul class="dropdown-menu">\n                                        <li>\n                                            <a href="#" id="show_login_dialog">Login</a>\n                                        </li>\n\n                                        <li>\n                                            <a href="/homepage/signup/">Signup</a>\n                                        </li>\n\n                                    </ul>\n')
        __M_writer('\n\n\n                                </ul>\n                            </li>\n                            <li class="divider-vertical"></li>\n                        </ul>\n                    </ul>\n                </div>\n                <!--/.nav-collapse -->\n            </div>\n        </div>\n    </div>\n    <div class="content">\n\n        <div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n                <h4 class="modal-title" id="myModalLabel">Modal title</h4>\n              </div>\n              <div class="modal-body">\n                ...\n              </div>\n              <div class="modal-footer">\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                <button type="button" class="btn btn-primary">Save changes</button>\n              </div>\n            </div>\n          </div>\n        </div>\n\n    </div>\n    <div class="content">\n\n        <div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n                <h4 class="modal-title" id="myModalLabel">Modal title</h4>\n              </div>\n              <div class="modal-body">\n                ...\n              </div>\n              <div class="modal-footer">\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                <button type="button" class="btn btn-primary">Save changes</button>\n              </div>\n            </div>\n          </div>\n        </div>\n\n    </div>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n     ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  </body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_userheadlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def userheadlinks():
            return render_userheadlinks(context)
        __M_writer = context.writer()
        __M_writer('\n     <link rel="stylesheet" type="text/css" href="http://www.shieldui.com/shared/components/latest/css/dark-bootstrap/all.min.css">\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 174, "65": 175, "66": 175, "72": 166, "96": 23, "78": 166, "108": 102, "16": 4, "18": 0, "84": 172, "90": 172, "32": 2, "33": 4, "34": 5, "102": 23, "38": 5, "39": 15, "44": 25, "45": 36, "46": 36, "47": 38, "48": 82, "49": 83, "50": 84, "51": 84, "52": 96, "53": 97, "54": 110, "59": 168}, "source_encoding": "ascii", "uri": "base.htm", "filename": "/Users/rodneycox/chf/homepage/templates/base.htm"}
__M_END_METADATA
"""
