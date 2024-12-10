from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/poe.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_namespace = resolve('namespace')
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_poe = resolve('poe')
    l_0_lldp = resolve('lldp')
    l_0_POE_CLASS_MAP = l_0_poe_global_defaults = l_0_ethernet_interfaces_poe = missing
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
        t_3 = environment.filters['float']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'float' found.")
    try:
        t_4 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    try:
        t_5 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_6 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_POE_CLASS_MAP = {0: '15.40', 1: '4.00', 2: '7.00', 3: '15.40', 4: '30.00', 5: '45.00', 6: '60.00', 7: '75.00', 8: '90.00'}
    context.vars['POE_CLASS_MAP'] = l_0_POE_CLASS_MAP
    context.exported_vars.add('POE_CLASS_MAP')
    l_0_poe_global_defaults = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), reboot_action='-', interface_shutdown_action='-', lldp_negotiate='-')
    context.vars['poe_global_defaults'] = l_0_poe_global_defaults
    context.exported_vars.add('poe_global_defaults')
    l_0_ethernet_interfaces_poe = []
    context.vars['ethernet_interfaces_poe'] = l_0_ethernet_interfaces_poe
    context.exported_vars.add('ethernet_interfaces_poe')
    for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        _loop_vars = {}
        pass
        if t_6(environment.getattr(l_1_ethernet_interface, 'poe')):
            pass
            context.call(environment.getattr((undefined(name='ethernet_interfaces_poe') if l_0_ethernet_interfaces_poe is missing else l_0_ethernet_interfaces_poe), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
    l_1_ethernet_interface = missing
    if (t_6((undefined(name='poe') if l_0_poe is missing else l_0_poe)) or (t_5((undefined(name='ethernet_interfaces_poe') if l_0_ethernet_interfaces_poe is missing else l_0_ethernet_interfaces_poe)) > 0)):
        pass
        yield '\n## Power Over Ethernet (PoE)\n\n### PoE Summary\n'
        if t_6((undefined(name='poe') if l_0_poe is missing else l_0_poe)):
            pass
            yield '\n#### PoE Global\n\n| Reboot Action | Shutdown Action | LLDP Negotiation |\n| ------------------- | -------------------- | ----------------------|\n'
            if not isinstance(l_0_poe_global_defaults, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_poe_global_defaults['reboot_action'] = t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_0_poe is missing else l_0_poe), 'reboot'), 'action'), environment.getattr((undefined(name='poe_global_defaults') if l_0_poe_global_defaults is missing else l_0_poe_global_defaults), 'reboot_action'))
            if not isinstance(l_0_poe_global_defaults, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_poe_global_defaults['interface_shutdown_action'] = t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_0_poe is missing else l_0_poe), 'interface_shutdown'), 'action'), environment.getattr((undefined(name='poe_global_defaults') if l_0_poe_global_defaults is missing else l_0_poe_global_defaults), 'interface_shutdown_action'))
            if t_6(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'tlvs')):
                pass
                def t_7(fiter):
                    for l_1_tlv in fiter:
                        if (environment.getattr(l_1_tlv, 'name') == 'power-via-mdi'):
                            yield l_1_tlv
                for l_1_tlv in t_7(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'tlvs')):
                    _loop_vars = {}
                    pass
                    if not isinstance(l_0_poe_global_defaults, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_0_poe_global_defaults['lldp_negotiate'] = environment.getattr(l_1_tlv, 'transmit')
                l_1_tlv = missing
            yield '| '
            yield str(environment.getattr((undefined(name='poe_global_defaults') if l_0_poe_global_defaults is missing else l_0_poe_global_defaults), 'reboot_action'))
            yield ' | '
            yield str(environment.getattr((undefined(name='poe_global_defaults') if l_0_poe_global_defaults is missing else l_0_poe_global_defaults), 'interface_shutdown_action'))
            yield ' | '
            yield str(environment.getattr((undefined(name='poe_global_defaults') if l_0_poe_global_defaults is missing else l_0_poe_global_defaults), 'lldp_negotiate'))
            yield ' |\n'
        if (t_5((undefined(name='ethernet_interfaces_poe') if l_0_ethernet_interfaces_poe is missing else l_0_ethernet_interfaces_poe)) > 0):
            pass
            yield '\n#### PoE Interfaces\n\n| Interface | PoE Enabled | Priority | Limit | Reboot Action | Link Down Action | Shutdown Action | LLDP Negotiation | Legacy Detection |\n| --------- | --------- | --------- | ----------- | ----------- | ----------- | ----------- | --------- | --------- |\n'
            for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces_poe') if l_0_ethernet_interfaces_poe is missing else l_0_ethernet_interfaces_poe), 'name'):
                l_1_poe = l_0_poe
                l_1_enabled = l_1_priority = l_1_limit = l_1_reboot_action = l_1_link_down_action = l_1_shutdown_action = l_1_negotiation_lldp = l_1_legacy_detect = missing
                _loop_vars = {}
                pass
                l_1_poe = environment.getattr(l_1_ethernet_interface, 'poe')
                _loop_vars['poe'] = l_1_poe
                l_1_enabled = (not t_1(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'disabled'), False))
                _loop_vars['enabled'] = l_1_enabled
                l_1_priority = t_1(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'priority'), '-')
                _loop_vars['priority'] = l_1_priority
                l_1_limit = '-'
                _loop_vars['limit'] = l_1_limit
                if t_6(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'limit')):
                    pass
                    if t_6(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'limit'), 'class')):
                        pass
                        l_1_limit = str_join((environment.getitem((undefined(name='POE_CLASS_MAP') if l_0_POE_CLASS_MAP is missing else l_0_POE_CLASS_MAP), environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'limit'), 'class')), ' watts', ))
                        _loop_vars['limit'] = l_1_limit
                    elif t_6(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'limit'), 'watts')):
                        pass
                        l_1_limit = str_join((t_4('%.2f', t_3(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'limit'), 'watts'))), ' watts', ))
                        _loop_vars['limit'] = l_1_limit
                    if (((undefined(name='limit') if l_1_limit is missing else l_1_limit) != '-') and t_6(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'limit'), 'fixed'), True)):
                        pass
                        l_1_limit = str_join(((undefined(name='limit') if l_1_limit is missing else l_1_limit), ' (fixed)', ))
                        _loop_vars['limit'] = l_1_limit
                l_1_reboot_action = t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'reboot'), 'action'), environment.getattr((undefined(name='poe_global_defaults') if l_0_poe_global_defaults is missing else l_0_poe_global_defaults), 'reboot_action'))
                _loop_vars['reboot_action'] = l_1_reboot_action
                l_1_link_down_action = t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'link_down'), 'action'), '-')
                _loop_vars['link_down_action'] = l_1_link_down_action
                if (t_6(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'link_down'), 'action'), 'power-off') and t_6(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'link_down'), 'power_off_delay'))):
                    pass
                    l_1_link_down_action = str_join(((undefined(name='link_down_action') if l_1_link_down_action is missing else l_1_link_down_action), ' (delayed ', environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'link_down'), 'power_off_delay'), ' seconds)', ))
                    _loop_vars['link_down_action'] = l_1_link_down_action
                l_1_shutdown_action = t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'shutdown'), 'action'), environment.getattr((undefined(name='poe_global_defaults') if l_0_poe_global_defaults is missing else l_0_poe_global_defaults), 'interface_shutdown_action'))
                _loop_vars['shutdown_action'] = l_1_shutdown_action
                l_1_negotiation_lldp = t_1(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'negotiation_lldp'), environment.getattr((undefined(name='poe_global_defaults') if l_0_poe_global_defaults is missing else l_0_poe_global_defaults), 'lldp_negotiate'))
                _loop_vars['negotiation_lldp'] = l_1_negotiation_lldp
                l_1_legacy_detect = t_1(environment.getattr((undefined(name='poe') if l_1_poe is missing else l_1_poe), 'legacy_detect'), '-')
                _loop_vars['legacy_detect'] = l_1_legacy_detect
                yield '| '
                yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                yield ' | '
                yield str((undefined(name='enabled') if l_1_enabled is missing else l_1_enabled))
                yield ' | '
                yield str((undefined(name='priority') if l_1_priority is missing else l_1_priority))
                yield ' | '
                yield str((undefined(name='limit') if l_1_limit is missing else l_1_limit))
                yield ' | '
                yield str((undefined(name='reboot_action') if l_1_reboot_action is missing else l_1_reboot_action))
                yield ' | '
                yield str((undefined(name='link_down_action') if l_1_link_down_action is missing else l_1_link_down_action))
                yield ' | '
                yield str((undefined(name='shutdown_action') if l_1_shutdown_action is missing else l_1_shutdown_action))
                yield ' | '
                yield str((undefined(name='negotiation_lldp') if l_1_negotiation_lldp is missing else l_1_negotiation_lldp))
                yield ' | '
                yield str((undefined(name='legacy_detect') if l_1_legacy_detect is missing else l_1_legacy_detect))
                yield ' |\n'
            l_1_ethernet_interface = l_1_poe = l_1_enabled = l_1_priority = l_1_limit = l_1_reboot_action = l_1_link_down_action = l_1_shutdown_action = l_1_negotiation_lldp = l_1_legacy_detect = missing
    if t_6((undefined(name='poe') if l_0_poe is missing else l_0_poe)):
        pass
        yield '\n### PoE Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/poe.j2', 'documentation/poe.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'POE_CLASS_MAP': l_0_POE_CLASS_MAP, 'ethernet_interfaces_poe': l_0_ethernet_interfaces_poe, 'poe_global_defaults': l_0_poe_global_defaults})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=52&8=55&9=58&10=61&11=64&12=66&15=68&20=71&27=74&28=77&30=80&31=82&32=89&35=94&37=100&43=103&44=108&45=110&46=112&47=114&48=116&49=118&50=120&51=122&52=124&54=126&55=128&58=130&59=132&60=134&61=136&63=138&64=140&65=142&66=145&70=164&75=167'