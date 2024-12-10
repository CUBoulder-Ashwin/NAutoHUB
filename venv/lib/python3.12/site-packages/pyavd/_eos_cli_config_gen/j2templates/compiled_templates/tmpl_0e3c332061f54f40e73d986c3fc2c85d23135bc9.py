from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ipv6-neighbors.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ipv6_neighbor = resolve('ipv6_neighbor')
    l_0_persistent_doc = resolve('persistent_doc')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor)):
        pass
        yield '\n### IPv6 Neighbors\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'persistent'), 'enabled'), True):
            pass
            l_0_persistent_doc = 'IPv6 neighbor cache persistency is enabled.'
            context.vars['persistent_doc'] = l_0_persistent_doc
            context.exported_vars.add('persistent_doc')
            if t_2(environment.getattr(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'persistent'), 'refresh_delay')):
                pass
                l_0_persistent_doc = str_join(((undefined(name='persistent_doc') if l_0_persistent_doc is missing else l_0_persistent_doc), ' The refresh-delay is ', environment.getattr(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'persistent'), 'refresh_delay'), ' seconds after reboot.', ))
                context.vars['persistent_doc'] = l_0_persistent_doc
                context.exported_vars.add('persistent_doc')
            yield '\n'
            yield str((undefined(name='persistent_doc') if l_0_persistent_doc is missing else l_0_persistent_doc))
            yield '\n'
        if t_2(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'static_entries')):
            pass
            yield '\n#### IPv6 Static Neighbors\n\n| VRF | IPv6 Address | Exit Interface | MAC Address |\n| --- | ------------ | -------------- | ----------- |\n'
            for l_1_neighbor in environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'static_entries'):
                _loop_vars = {}
                pass
                if ((t_2(environment.getattr(l_1_neighbor, 'ipv6_address')) and t_2(environment.getattr(l_1_neighbor, 'interface'))) and t_2(environment.getattr(l_1_neighbor, 'mac_address'))):
                    pass
                    yield '| '
                    yield str(t_1(environment.getattr(l_1_neighbor, 'vrf'), '-'))
                    yield ' | '
                    yield str(environment.getattr(l_1_neighbor, 'ipv6_address'))
                    yield ' | '
                    yield str(environment.getattr(l_1_neighbor, 'interface'))
                    yield ' | '
                    yield str(environment.getattr(l_1_neighbor, 'mac_address'))
                    yield ' |\n'
            l_1_neighbor = missing
        yield '\n#### IPv6 Neighbor Configuration\n\n```eos\n'
        template = environment.get_template('eos/ipv6-neighbors.j2', 'documentation/ipv6-neighbors.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'persistent_doc': l_0_persistent_doc})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=25&10=28&11=30&12=33&13=35&16=39&18=41&24=44&25=47&26=50&34=60'