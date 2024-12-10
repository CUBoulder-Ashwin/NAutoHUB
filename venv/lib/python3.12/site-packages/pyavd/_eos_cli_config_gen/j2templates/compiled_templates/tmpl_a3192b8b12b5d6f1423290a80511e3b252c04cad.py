from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ipv6-neighbors.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ipv6_neighbor = resolve('ipv6_neighbor')
    l_0_persistent_cli = resolve('persistent_cli')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_1(environment.getattr(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'persistent'), 'enabled'), True) or t_1(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'static_entries'))):
        pass
        yield '!\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'persistent'), 'enabled'), True):
            pass
            l_0_persistent_cli = 'ipv6 neighbor persistent'
            context.vars['persistent_cli'] = l_0_persistent_cli
            context.exported_vars.add('persistent_cli')
            if t_1(environment.getattr(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'persistent'), 'refresh_delay')):
                pass
                l_0_persistent_cli = str_join(((undefined(name='persistent_cli') if l_0_persistent_cli is missing else l_0_persistent_cli), ' refresh-delay ', environment.getattr(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'persistent'), 'refresh_delay'), ))
                context.vars['persistent_cli'] = l_0_persistent_cli
                context.exported_vars.add('persistent_cli')
            yield str((undefined(name='persistent_cli') if l_0_persistent_cli is missing else l_0_persistent_cli))
            yield '\n'
        if t_1(environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'static_entries')):
            pass
            for l_1_neighbor in environment.getattr((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor), 'static_entries'):
                l_1_neighbor_cli = resolve('neighbor_cli')
                _loop_vars = {}
                pass
                if ((t_1(environment.getattr(l_1_neighbor, 'ipv6_address')) and t_1(environment.getattr(l_1_neighbor, 'interface'))) and t_1(environment.getattr(l_1_neighbor, 'mac_address'))):
                    pass
                    l_1_neighbor_cli = str_join((environment.getattr(l_1_neighbor, 'ipv6_address'), ' ', environment.getattr(l_1_neighbor, 'interface'), ' ', environment.getattr(l_1_neighbor, 'mac_address'), ))
                    _loop_vars['neighbor_cli'] = l_1_neighbor_cli
                    if t_1(environment.getattr(l_1_neighbor, 'vrf')):
                        pass
                        l_1_neighbor_cli = str_join(('ipv6 neighbor vrf ', environment.getattr(l_1_neighbor, 'vrf'), ' ', (undefined(name='neighbor_cli') if l_1_neighbor_cli is missing else l_1_neighbor_cli), ))
                        _loop_vars['neighbor_cli'] = l_1_neighbor_cli
                    else:
                        pass
                        l_1_neighbor_cli = str_join(('ipv6 neighbor ', (undefined(name='neighbor_cli') if l_1_neighbor_cli is missing else l_1_neighbor_cli), ))
                        _loop_vars['neighbor_cli'] = l_1_neighbor_cli
                    yield str((undefined(name='neighbor_cli') if l_1_neighbor_cli is missing else l_1_neighbor_cli))
                    yield '\n'
            l_1_neighbor = l_1_neighbor_cli = missing

blocks = {}
debug_info = '7=19&9=22&10=24&11=27&12=29&14=32&16=34&17=36&18=40&19=42&20=44&21=46&23=50&25=52'