# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428196645.084919
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
        def shopcontent():
            return render_shopcontent(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)
        checkout_form = context.get('checkout_form', UNDEFINED)
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
        def shopcontent():
            return render_shopcontent(context)
        int = context.get('int', UNDEFINED)
        current_cart = context.get('current_cart', UNDEFINED)
        rental_cart = context.get('rental_cart', UNDEFINED)
        checkout_form = context.get('checkout_form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="checkout">\n\n\n\n\n\n\n        <div class="container">\n\n            <div id="pansky" class="panel panel-default">\n\n                <div class="panel-body">\n                    <div class="container-fluid">\n                        <div class="col-lg-8 col-lg-offset-2">\n\n\n                            <!-- Checkout page title -->\n                            <h2 class="title"><i class="fa fa-shopping-cart"></i> Order Summary</h2>\n\n                            <div class="panel panel-default">\n                                <!-- Default panel contents -->\n                                <div class="panel-heading">Purchase Summary</div>\n\n                                <!-- Table -->\n                                <table class="table">\n                                    <th>\n\n                                        <td>\n                                            Product\n                                        </td>\n                                        <td>\n                                            Unit Price\n                                        </td>\n                                        <td>\n                                            Extended Price\n                                        </td>\n                                    </th>\n                                <tbody>\n')
        for key,value in current_cart.items():
            __M_writer('                                    ')

            grand_total = 0
            price = int(value[0].current_price)
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
            __M_writer('</td>\n\n\n\n                                        </tr>\n')
        __M_writer('\n\n                                </tbody>\n                                </table>\n                            </div>\n                            <div class="panel panel-default">\n                                <!-- Default panel contents -->\n                                <div class="panel-heading">Rental Summary</div>\n\n                                <!-- Table -->\n                                <table class="table">\n                                    <th>\n                                        <td>\n                                            Item\n                                        </td>\n                                        <td>\n                                            Daily  Price\n                                        </td>\n                                        <td>\n                                            30 Day Price\n                                        </td>\n                                    </th>\n                                <tbody>\n                                    ')
        rental_total=0
        
        __M_writer('\n')
        for rental in rental_cart:
            __M_writer('                                    ')

            month = rental.rental_price * 30
            rental_total +=rental.rental_price
            
            
            __M_writer('\n\n\n                                        <tr>\n                                            <td> </td>\n                                            <td>')
            __M_writer(str( rental.name ))
            __M_writer('</td>\n                                            <td>$')
            __M_writer(str( rental.rental_price ))
            __M_writer('</td>\n                                            <td>$')
            __M_writer(str( month ))
            __M_writer('</td>\n\n\n\n                                        </tr>\n')
        __M_writer('\n                                </tbody>\n                                </table>\n                            </div>\n\n                            <hr />\n                            <!-- Payment details section -->\n                            <!-- Title -->\n\n                            <!-- Radio buttons to select payment type -->\n\n\n\n\n                             <div class="form form-small">\n                                <form class="form-horizontal" method="POST">\n                                    <!-- Sub title -->\n                                    <h4 class="title">Shipping &amp; Billing Details</h4>\n                                    <br>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">First</label>\n                                        <div class="col-md-8">\n                                            ')
        __M_writer(str( checkout_form['First']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['First'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Last</label>\n                                        <div class="col-md-8">\n                                            ')
        __M_writer(str( checkout_form['Last']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['Last'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Address</label>\n                                        <div class="col-md-8">\n                                            ')
        __M_writer(str( checkout_form['Address']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['Address'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">City</label>\n                                        <div class="col-md-6">\n                                            ')
        __M_writer(str( checkout_form['City']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['City'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">State</label>\n                                        <div class="col-md-6">\n                                            ')
        __M_writer(str( checkout_form['State']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['State'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Zip</label>\n                                        <div class="col-md-4">\n                                            ')
        __M_writer(str( checkout_form['Zip']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['Zip'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <!-- Address and Shipping details form -->\n                                    <div class="form form-small">\n                                            <!-- for field in shipping_form: -->\n                                            <div class="form-group">\n\n                                                <label class="control-label col-md-2" for="name1">\n                                                    <!-- { field.label } -->\n\n                                                </label>\n                                                <div class="col-md-6">\n                                                    <!-- { field } -->\n                                                </div>\n                                            </div>\n                                            <!-- endfor -->\n                                    </div>\n\n                                    <hr />\n                                    <h4 class="title">Payment Details</h4>\n                                    <br>\n\n\n                                    <!-- _________________________all form data goes below here_____________________________ -->\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Name</label>\n                                        <div class="col-md-9">\n                                            ')
        __M_writer(str( checkout_form['Name']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['Name'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Card Number</label>\n                                        <div class="col-md-9">\n                                            ')
        __M_writer(str( checkout_form['CardNumber']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['CardNumber'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Expiration Month</label>\n                                        <div class="col-md-3">\n                                            ')
        __M_writer(str( checkout_form['ExpirationMonth']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['ExpirationMonth'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Expiration Month</label>\n                                        <div class="col-md-2">\n                                            ')
        __M_writer(str( checkout_form['ExpirationYear']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['ExpirationYear'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n                                    <div class="form-group">\n                                        <label class="control-label col-md-2" for="cardnumber">Card Number</label>\n                                        <div class="col-md-3">\n                                            ')
        __M_writer(str( checkout_form['Cvv']))
        __M_writer('\n                                            ')
        __M_writer(str( checkout_form['Cvv'].errors))
        __M_writer('\n                                        </div>\n                                    </div>\n\n\n                            <!-- Confirm order button -->\n                            <div class="row">\n                                <div class="col-md-4 col-md-offset-8">\n                                    <div class="pull-right">\n                                        <button type="submit" class="btn btn-danger">Confirm Order</button>\n                                        <!-- <a href="/shop/confirmation/" class="btn btn-danger">Confirm Order</a> -->\n                                    </div>\n                                </div>\n                            </div>\n                        </form>\n                    </div>\n\n                        </div>\n                    </div>\n                </div>\n\n            </div>\n\n        </div>\n\n\n    </div>\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/rodneycox/chf/shop/templates/checkout.html", "uri": "checkout.html", "line_map": {"128": 198, "129": 199, "130": 199, "131": 205, "132": 205, "133": 206, "134": 206, "135": 212, "136": 212, "137": 213, "138": 213, "139": 219, "140": 219, "141": 220, "142": 220, "148": 142, "27": 0, "38": 1, "43": 254, "49": 3, "59": 3, "60": 43, "61": 44, "62": 44, "71": 51, "72": 55, "73": 55, "74": 56, "75": 56, "76": 57, "77": 57, "78": 58, "79": 58, "80": 64, "81": 87, "83": 87, "84": 88, "85": 89, "86": 89, "91": 92, "92": 97, "93": 97, "94": 98, "95": 98, "96": 99, "97": 99, "98": 105, "99": 127, "100": 127, "101": 128, "102": 128, "103": 134, "104": 134, "105": 135, "106": 135, "107": 141, "108": 141, "109": 142, "110": 142, "111": 148, "112": 148, "113": 149, "114": 149, "115": 155, "116": 155, "117": 156, "118": 156, "119": 162, "120": 162, "121": 163, "122": 163, "123": 191, "124": 191, "125": 192, "126": 192, "127": 198}, "source_encoding": "ascii"}
__M_END_METADATA
"""
