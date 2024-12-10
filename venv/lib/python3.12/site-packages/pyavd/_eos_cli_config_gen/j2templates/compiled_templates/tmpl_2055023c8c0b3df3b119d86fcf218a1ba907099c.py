from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/lldp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_lldp = resolve('lldp')
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
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
    if t_3((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp)):
        pass
        yield '\n## LLDP\n\n### LLDP Summary\n\n#### LLDP Global Settings\n\n| Enabled | Management Address | Management VRF | Timer | Hold-Time | Re-initialization Timer | Drop Received Tagged Packets |\n| ------- | ------------------ | -------------- | ----- | --------- | ----------------------- | ---------------------------- |\n| '
        yield str(t_1(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'run'), True))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'management_address'), '-'))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'vrf'), 'Default'))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'timer'), '30'))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'holdtime'), '120'))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'timer_reinitialization'), '2'))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'receive_packet_tagged_drop'), '-'))
        yield ' |\n'
        if t_3(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'tlvs')):
            pass
            yield '\n#### LLDP Explicit TLV Transmit Settings\n\n| TLV | Transmit |\n| --- | -------- |\n'
            for l_1_tlv in environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'tlvs'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(t_1(environment.getattr(l_1_tlv, 'name'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_tlv, 'transmit'), '-'))
                yield ' |\n'
            l_1_tlv = missing
        if t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces)):
            pass
            yield '\n#### LLDP Interface Settings\n'
            if t_3(environment.getattr((undefined(name='lldp') if l_0_lldp is missing else l_0_lldp), 'run'), False):
                pass
                yield '\nLLDP is **disabled** globally. Local interface configs will not apply.\n'
            yield '\n| Interface | Transmit | Receive |\n| --------- | -------- | ------- |\n'
            for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
                _loop_vars = {}
                pass
                if (t_3(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'transmit')) or t_3(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'receive'))):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                    yield ' | '
                    yield str(t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'transmit'), '-'))
                    yield ' | '
                    yield str(t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'receive'), '-'))
                    yield ' |\n'
            l_1_ethernet_interface = missing
        yield '\n### LLDP Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/lldp.j2', 'documentation/lldp.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=31&17=34&18=48&24=51&25=55&28=60&31=63&38=67&39=70&40=73&48=81'