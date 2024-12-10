from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-routing.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_routing = resolve('ip_routing')
    l_0_vrfs = resolve('vrfs')
    l_0_default_ip_routing = resolve('default_ip_routing')
    l_0_ip_routing_ipv6_interfaces = resolve('ip_routing_ipv6_interfaces')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.filters['rejectattr']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'rejectattr' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_4((undefined(name='ip_routing') if l_0_ip_routing is missing else l_0_ip_routing)) or t_4((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs))):
        pass
        yield '\n### IP Routing\n\n#### IP Routing Summary\n\n| VRF | Routing Enabled |\n| --- | --------------- |\n'
        l_0_default_ip_routing = t_1((undefined(name='ip_routing') if l_0_ip_routing is missing else l_0_ip_routing), False)
        context.vars['default_ip_routing'] = l_0_default_ip_routing
        context.exported_vars.add('default_ip_routing')
        if t_1((undefined(name='ip_routing_ipv6_interfaces') if l_0_ip_routing_ipv6_interfaces is missing else l_0_ip_routing_ipv6_interfaces), False):
            pass
            l_0_default_ip_routing = 'True (ipv6 interfaces)'
            context.vars['default_ip_routing'] = l_0_default_ip_routing
            context.exported_vars.add('default_ip_routing')
        yield '| default | '
        yield str((undefined(name='default_ip_routing') if l_0_default_ip_routing is missing else l_0_default_ip_routing))
        yield ' |\n'
        for l_1_vrf in t_2(t_3(context, t_1((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs), []), 'name', 'arista.avd.defined', 'default'), 'name'):
            l_1_ip_routing = l_0_ip_routing
            _loop_vars = {}
            pass
            l_1_ip_routing = t_1(environment.getattr(l_1_vrf, 'ip_routing'), '-')
            _loop_vars['ip_routing'] = l_1_ip_routing
            if t_1(environment.getattr(l_1_vrf, 'ip_routing_ipv6_interfaces'), False):
                pass
                l_1_ip_routing = 'True (ipv6 interfaces)'
                _loop_vars['ip_routing'] = l_1_ip_routing
            yield '| '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield ' | '
            yield str((undefined(name='ip_routing') if l_1_ip_routing is missing else l_1_ip_routing))
            yield ' |\n'
        l_1_vrf = l_1_ip_routing = missing
        yield '\n#### IP Routing Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-routing.j2', 'documentation/ip-routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'default_ip_routing': l_0_default_ip_routing})):
            yield event
        template = environment.get_template('eos/ip-icmp-redirect.j2', 'documentation/ip-routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'default_ip_routing': l_0_default_ip_routing})):
            yield event
        template = environment.get_template('eos/ip-hardware.j2', 'documentation/ip-routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'default_ip_routing': l_0_default_ip_routing})):
            yield event
        template = environment.get_template('eos/ip-routing-vrfs.j2', 'documentation/ip-routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'default_ip_routing': l_0_default_ip_routing})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=39&16=42&17=45&18=47&20=51&21=53&22=57&23=59&24=61&26=64&32=70&33=73&34=76&35=79'