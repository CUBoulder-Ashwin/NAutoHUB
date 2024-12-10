from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ipv6-unicast-routing.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ipv6_unicast_routing = resolve('ipv6_unicast_routing')
    l_0_vrfs = resolve('vrfs')
    l_0_ipv6_configured_in_vrf = resolve('ipv6_configured_in_vrf')
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
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_3((undefined(name='ipv6_unicast_routing') if l_0_ipv6_unicast_routing is missing else l_0_ipv6_unicast_routing)) or t_3((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs))):
        pass
        yield '\n### IPv6 Routing\n\n#### IPv6 Routing Summary\n\n| VRF | Routing Enabled |\n| --- | --------------- |\n| default | '
        yield str(t_1((undefined(name='ipv6_unicast_routing') if l_0_ipv6_unicast_routing is missing else l_0_ipv6_unicast_routing), False))
        yield ' |\n'
        l_0_ipv6_configured_in_vrf = False
        context.vars['ipv6_configured_in_vrf'] = l_0_ipv6_configured_in_vrf
        context.exported_vars.add('ipv6_configured_in_vrf')
        for l_1_vrf in t_2((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs), 'name'):
            l_1_ipv6_configured_in_vrf = l_0_ipv6_configured_in_vrf
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_vrf, 'ipv6_routing'), True):
                pass
                l_1_ipv6_configured_in_vrf = True
                _loop_vars['ipv6_configured_in_vrf'] = l_1_ipv6_configured_in_vrf
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | true |\n'
            else:
                pass
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | false |\n'
        l_1_vrf = l_1_ipv6_configured_in_vrf = missing
        if (t_3((undefined(name='ipv6_unicast_routing') if l_0_ipv6_unicast_routing is missing else l_0_ipv6_unicast_routing), True) or ((undefined(name='ipv6_configured_in_vrf') if l_0_ipv6_configured_in_vrf is missing else l_0_ipv6_configured_in_vrf) == True)):
            pass
            yield '\n#### IPv6 Routing Device Configuration\n\n```eos\n'
            template = environment.get_template('eos/ipv6-unicast-routing.j2', 'documentation/ipv6-unicast-routing.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'ipv6_configured_in_vrf': l_0_ipv6_configured_in_vrf})):
                yield event
            template = environment.get_template('eos/ipv6-unicast-routing-vrfs.j2', 'documentation/ipv6-unicast-routing.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'ipv6_configured_in_vrf': l_0_ipv6_configured_in_vrf})):
                yield event
            template = environment.get_template('eos/ipv6-icmp-redirect.j2', 'documentation/ipv6-unicast-routing.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'ipv6_configured_in_vrf': l_0_ipv6_configured_in_vrf})):
                yield event
            template = environment.get_template('eos/ipv6-hardware.j2', 'documentation/ipv6-unicast-routing.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'ipv6_configured_in_vrf': l_0_ipv6_configured_in_vrf})):
                yield event
            yield '```\n'

blocks = {}
debug_info = '7=32&15=35&16=37&17=40&18=44&19=46&20=49&22=54&25=57&30=60&31=63&32=66&33=69'