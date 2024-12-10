from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/virtual-source-nat-vrfs.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_virtual_source_nat_vrfs = resolve('virtual_source_nat_vrfs')
    l_0_ipv4_address_list = resolve('ipv4_address_list')
    l_0_ipv6_address_list = resolve('ipv6_address_list')
    l_0_ip_addresses = resolve('ip_addresses')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='virtual_source_nat_vrfs') if l_0_virtual_source_nat_vrfs is missing else l_0_virtual_source_nat_vrfs)):
        pass
        yield '!\n'
        l_0_ipv4_address_list = []
        context.vars['ipv4_address_list'] = l_0_ipv4_address_list
        context.exported_vars.add('ipv4_address_list')
        l_0_ipv6_address_list = []
        context.vars['ipv6_address_list'] = l_0_ipv6_address_list
        context.exported_vars.add('ipv6_address_list')
        for l_1_vrf in t_1((undefined(name='virtual_source_nat_vrfs') if l_0_virtual_source_nat_vrfs is missing else l_0_virtual_source_nat_vrfs), 'name'):
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_vrf, 'ip_address')):
                pass
                context.call(environment.getattr((undefined(name='ipv4_address_list') if l_0_ipv4_address_list is missing else l_0_ipv4_address_list), 'append'), ((('ip address virtual source-nat vrf ' + environment.getattr(l_1_vrf, 'name')) + ' address ') + environment.getattr(l_1_vrf, 'ip_address')), _loop_vars=_loop_vars)
            if t_2(environment.getattr(l_1_vrf, 'ipv6_address')):
                pass
                context.call(environment.getattr((undefined(name='ipv6_address_list') if l_0_ipv6_address_list is missing else l_0_ipv6_address_list), 'append'), ((('ipv6 address virtual source-nat vrf ' + environment.getattr(l_1_vrf, 'name')) + ' address ') + environment.getattr(l_1_vrf, 'ipv6_address')), _loop_vars=_loop_vars)
        l_1_vrf = missing
        l_0_ip_addresses = ((undefined(name='ipv4_address_list') if l_0_ipv4_address_list is missing else l_0_ipv4_address_list) + (undefined(name='ipv6_address_list') if l_0_ipv6_address_list is missing else l_0_ipv6_address_list))
        context.vars['ip_addresses'] = l_0_ip_addresses
        context.exported_vars.add('ip_addresses')
        for l_1_ip_address in (undefined(name='ip_addresses') if l_0_ip_addresses is missing else l_0_ip_addresses):
            _loop_vars = {}
            pass
            yield str(l_1_ip_address)
            yield '\n'
        l_1_ip_address = missing

blocks = {}
debug_info = '7=27&9=30&10=33&11=36&12=39&13=41&15=42&16=44&19=46&20=49&21=52'