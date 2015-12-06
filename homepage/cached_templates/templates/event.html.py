# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428460560.490788
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/event.html'
_template_uri = 'event.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        event = context.get('event', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        import datetime 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        event = context.get('event', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="festiv-event">\n        <!-- Page Title -->\n\t\t<div class="section section-breadcrumbs">\n\t\t\t<div class="container">\n\t\t\t\t<div class="row">\n\t\t\t\t\t<div class="col-sm-12">\n\t\t\t\t\t\t<h1>Event Description</h1>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\n        <div class="section">\n\t    \t<div class="container">\n\t\t\t\t<div class="row">\n\t\t\t\t\t<!-- Image Column -->\n\t\t\t\t\t<div class="col-sm-6">\n\t\t\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t\t\t<div class="portfolio-image">\n\t\t\t\t\t\t\t\t<a href="#"><img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/event')
        __M_writer(str(event.id))
        __M_writer('.jpg" alt="')
        __M_writer(str(event.name))
        __M_writer('"></a>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<!-- End Image Column -->\n\t\t\t\t\t<!-- Project Info Column -->\n\t\t\t\t\t<div class="portfolio-item-description col-sm-6">\n\t\t\t\t\t\t<h3>')
        __M_writer(str(event.name))
        __M_writer('</h3>\n\t\t\t\t\t\t<p>\n                            ')
        __M_writer(str(event.description))
        __M_writer('\n\t\t\t\t\t\t</p>\n\t\t\t\t\t\t<p>\n\n\t\t\t\t\t\t</p>\n\t\t\t\t\t\t<ul class="no-list-style">\n\t\t\t\t\t\t\t<li><b>Location:</b> ')
        __M_writer(str(event.location))
        __M_writer('</li>\n\t\t\t\t\t\t\t<li><b>Date:</b> ')
        __M_writer(str(event.start_date.strftime('%A, %B %d, %Y')))
        __M_writer(' - ')
        __M_writer(str(event.end_date.strftime('%A, %B %d, %Y')))
        __M_writer('</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\t\t\t\t\t<!-- End Project Info Column -->\n\t\t\t\t</div>\n\t\t\t\t<!-- Related Projects -->\n\t\t\t\t<h3>Items For Sale</h3>\n\t\t\t\t<div class="row">\n')
        for item in items:
            __M_writer('\t\t\t\t\t<div class="col-md-4 col-sm-6">\n\n\t\t\t\t\t\t<div class="portfolio-item">\n\t\t\t\t\t\t\t<div class="portfolio-image">\n\t\t\t\t\t\t\t\t<a href="#"><img id="saleitem" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('/shop/media/product_images/')
            __M_writer(str(item.id))
            __M_writer('.jpg" alt="')
            __M_writer(str(item.name))
            __M_writer('"></a>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="portfolio-info-fade">\n\t\t\t\t\t\t\t\t<ul>\n\t\t\t\t\t\t\t\t\t<li class="portfolio-project-name">')
            __M_writer(str(item.name))
            __M_writer('</li>\n\t\t\t\t\t\t\t\t\t<li>')
            __M_writer(str(item.description))
            __M_writer('</li>\n\t\t\t\t\t\t\t\t\t<li>Price: $')
            __M_writer(str(item.value))
            __M_writer('</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\n\t\t\t\t\t</div>\n')
        __M_writer('\t\t\t\t</div>\n\t\t\t\t<!-- End Related Projects -->\n\t\t\t</div>\n\t\t</div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/rodneycox/chf/homepage/templates/event.html", "line_map": {"64": 23, "65": 23, "66": 23, "67": 23, "68": 23, "69": 30, "70": 30, "71": 32, "72": 32, "73": 38, "74": 38, "75": 39, "76": 39, "77": 39, "78": 39, "79": 47, "80": 48, "81": 52, "82": 52, "83": 52, "84": 52, "85": 52, "86": 52, "87": 56, "88": 56, "89": 57, "90": 57, "27": 0, "92": 58, "93": 65, "91": 58, "37": 1, "38": 2, "42": 2, "47": 70, "99": 93, "53": 3, "62": 3, "63": 23}, "uri": "event.html"}
__M_END_METADATA
"""
