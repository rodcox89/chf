# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428460979.796266
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/homepage/templates/festivals.html'
_template_uri = 'festivals.html'
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
        days = context.get('days', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        months = context.get('months', UNDEFINED)
        events = context.get('events', UNDEFINED)
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
        days = context.get('days', UNDEFINED)
        def content():
            return render_content(context)
        months = context.get('months', UNDEFINED)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="festival-container">\n    <div class="section section-breadcrumbs">\n        <div class="container">\n            <div class="row">\n                <div class="col-md-12">\n                    <h1>Upcoming Events</h1>\n                </div>\n            </div>\n        </div>\n    </div>\n\n    <div class="section">\n        <div class="container">\n            <div class="row">\n                <div class="col-md-12">\n                    <table class="events-list">\n                        ')

        counter = 0
                                
        
        __M_writer('\n')
        for event in events:
            __M_writer('                        <tr>\n                            <td>\n                                <div class="event-date">\n                                    <div class="event-day">')
            __M_writer(str(days[counter]))
            __M_writer('</div>\n                                    <div class="event-month">')
            __M_writer(str(months[counter]))
            __M_writer('</div>\n                                </div>\n                            </td>\n                            <td>\n                                ')
            __M_writer(str(event.description))
            __M_writer('\n                            </td>\n                            <td class="event-venue hidden-xs">')
            __M_writer(str(event.location))
            __M_writer('</td>\n                            <td class="event-price hidden-xs">FREE</td>\n                            <td><a href="/event/')
            __M_writer(str(event.id))
            __M_writer('" class="btn btn-grey btn-sm event-more">Read More</a></td>\n                        </tr>\n                        ')

            counter += 1
                                    
            
            __M_writer('\n')
        __M_writer('                    </table>\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/rodneycox/chf/homepage/templates/festivals.html", "line_map": {"64": 24, "65": 27, "66": 27, "67": 28, "68": 28, "69": 32, "70": 32, "71": 34, "72": 34, "73": 36, "74": 36, "75": 38, "79": 40, "80": 42, "86": 80, "27": 0, "37": 1, "42": 48, "48": 3, "57": 3, "58": 20, "62": 22, "63": 23}, "uri": "festivals.html"}
__M_END_METADATA
"""
