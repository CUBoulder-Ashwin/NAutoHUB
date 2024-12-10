from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/mac-address-table.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mac_address_table = resolve('mac_address_table')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table)):
        pass
        yield '\n## MAC Address Table\n\n### MAC Address Table Summary\n'
        if t_1(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'aging_time')):
            pass
            yield '\n- MAC address table entry maximum age: '
            yield str(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'aging_time'))
            yield ' seconds\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'logging'), False):
            pass
            yield '\n- Logging MAC address interface flapping is Disabled\n'
        elif t_1(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'logging'), True):
            pass
            yield '\n- Logging MAC address interface flapping is Enabled\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'detection'), 'moves')):
            pass
            yield '\n- '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'detection'), 'moves'))
            yield ' MAC moves are considered as one flap\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'detection'), 'window')):
            pass
            yield '\n- Size of the flap detection time window: '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'detection'), 'window'))
            yield ' seconds\n'
        yield '\n### MAC Address Table Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/mac-address-table-aging-time.j2', 'documentation/mac-address-table.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('eos/mac-address-table-notification.j2', 'documentation/mac-address-table.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&12=21&14=24&16=26&19=29&23=32&25=35&27=37&29=40&35=43&36=46'