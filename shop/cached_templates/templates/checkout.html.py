# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425788858.421305
_enable_loop = True
_template_filename = '/Users/rodneycox/chf/shop/templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['shopcontent']


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
        current_cart = context.get('current_cart', UNDEFINED)
        form = context.get('form', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def shopcontent():
            return render_shopcontent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopcontent'):
            context['self'].shopcontent(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopcontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        current_cart = context.get('current_cart', UNDEFINED)
        form = context.get('form', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def shopcontent():
            return render_shopcontent(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="checkout">\n\n\n\n\n\n\n        <div class="container">\n\n            <div id="pansky" class="panel panel-default">\n\n                <div class="panel-body">\n                    <div class="container-fluid">\n                        <div class="col-lg-8 col-lg-offset-2">\n\n\n                            <!-- Checkout page title -->\n                            <h2 class="title"><i class="fa fa-shopping-cart"></i> Order Summary</h2>\n\n                            <div class="panel panel-default">\n                                <!-- Default panel contents -->\n                                <div class="panel-heading">Panel heading</div>\n\n                                <!-- Table -->\n                                <table class="table">\n                                <tbody>\n')
        for key,value in current_cart.items():
            __M_writer('                                    ')

            grand_total = 0
            price = int(value[0].value)
            qty = value[1]
            
            sub_total = (price * qty)
            grand_total += sub_total
                                                
            
            __M_writer('\n\n\n                                        <tr>\n                                            <td>')
            __M_writer(str( value[1]))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str( value[0].name ))
            __M_writer('</td>\n                                            <td>$')
            __M_writer(str( value[0].value ))
            __M_writer('</td>\n                                            <td>$')
            __M_writer(str( sub_total ))
            __M_writer('</td>\n                                            <td><a href="#" class="red delete_button" data-pid="')
            __M_writer(str( value[0].id))
            __M_writer('"  }>Remove <i class="fa fa-minus-square"></i> </a></td>\n\n\n\n                                        </tr>\n')
        __M_writer('                                    ')

        price = int(value[0].value)
        qty = value[1]
        
        sub_total = (price * qty)
        grand_total += sub_total
                                            
        
        __M_writer('\n\n                                </tbody>\n                                </table>\n                            </div>\n\n                            <!-- Sub title -->\n                            <h5 class="title">Shipping &amp; Billing Details</h5>\n                            <!-- Address and Shipping details form -->\n                            <div class="form form-small">\n                                <form class="form-horizontal">\n')
        for field in form:
            __M_writer('                                    <div class="form-group">\n\n                                        <label class="control-label col-md-2" for="name1">\n                                            ')
            __M_writer(str( field.label ))
            __M_writer('\n\n                                        </label>\n                                        <div class="col-md-6">\n                                            ')
            __M_writer(str( field ))
            __M_writer('\n                                        </div>\n                                    </div>\n')
        __M_writer('                                </form>\n                            </div>\n                            <hr />\n                            <!-- Payment details section -->\n                            <!-- Title -->\n                            <h5 class="title">Payment Details</h5>\n\n                            <!-- Radio buttons to select payment type -->\n\n                            <label class="radio-inline">\n                                <input type="radio" name="optionsRadios" id="optionsRadios1" value="1" checked> Debit Card\n                            </label>\n                            <label class="radio-inline">\n                                <input type="radio" name="optionsRadios" id="optionsRadios2" value="2"> Credit Card\n                            </label>\n                            <label class="radio-inline">\n                                <input type="radio" name="optionsRadios" id="optionsRadios3" value="3"> Internet Banking\n                            </label>\n                            <label class="radio-inline">\n                                <input type="radio" name="optionsRadios" id="optionsRadios4" value="4"> Cash On Delivery\n                            </label>\n                            <label class="radio-inline">\n                                <input type="radio" name="optionsRadios" id="optionsRadios5" value="5"> Paypal\n                            </label>\n\n                            <hr />\n\n                            <div class="form form-small">\n                                <form class="form-horizontal">\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Name</label>\n                                        <div class="col-md-6">\n                                            <input type="text" class="form-control" id="cardnumber" placeholder="Full Name on Card">\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Card Number</label>\n                                        <div class="col-md-6">\n                                            <input type="text" class="form-control" id="cardnumber" placeholder="0000-0000-0000-0000">\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="expdate">Expiration Date</label>\n                                        <div class="col-md-4">\n                                            <input type="text" class="form-control" id="expdate" placeholder="09/19/2019">\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="expdate">CVV</label>\n                                        <div class="col-md-2">\n                                            <input type="text" class="form-control" id="expdate" placeholder="801">\n                                        </div>\n                                    </div>\n                                </form>\n                            </div>\n\n                            <!-- Confirm order button -->\n                            <div class="row">\n                                <div class="col-md-4 col-md-offset-8">\n                                    <div class="pull-right">\n                                        <a href="/shop/confirmation/" class="btn btn-danger">Confirm Order</a>\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n\n            </div>\n\n        </div>\n\n\n    </div>\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/rodneycox/chf/shop/templates/checkout.html", "uri": "checkout.html", "line_map": {"69": 39, "70": 43, "71": 43, "72": 44, "73": 44, "74": 45, "75": 45, "76": 46, "77": 46, "78": 47, "79": 47, "80": 53, "81": 53, "89": 59, "90": 70, "27": 0, "92": 74, "93": 74, "94": 78, "95": 78, "96": 82, "91": 71, "37": 1, "102": 96, "42": 163, "48": 3, "57": 3, "58": 31, "59": 32, "60": 32}}
__M_END_METADATA
"""
