from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/mlag-configuration.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mlag_configuration = resolve('mlag_configuration')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration)):
        pass
        yield '\n## MLAG\n\n### MLAG Summary\n\n| Domain-id | Local-interface | Peer-address | Peer-link |\n| --------- | --------------- | ------------ | --------- |\n| '
        yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'domain_id'))
        yield ' | '
        yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'local_interface'))
        yield ' | '
        yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address'))
        yield ' | '
        yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_link'))
        yield ' |\n\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'heartbeat_interval')):
            pass
            yield 'Heartbeat Interval is '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'heartbeat_interval'))
            yield ' milliseconds.\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_detection_delay')):
            pass
            yield 'Dual primary detection is enabled. The detection delay is '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_detection_delay'))
            yield ' seconds.\n'
            if (t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_recovery_delay_mlag')) and t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_recovery_delay_non_mlag'))):
                pass
                yield 'Dual primary recovery delay for MLAG interfaces is '
                yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_recovery_delay_mlag'))
                yield ' seconds.\nDual primary recovery delay for NON-MLAG interfaces is '
                yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_recovery_delay_non_mlag'))
                yield ' seconds.\n'
        else:
            pass
            yield 'Dual primary detection is disabled.\n'
        yield '\n### MLAG Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/mlag-configuration.j2', 'documentation/mlag-configuration.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&15=21&17=29&18=32&20=34&21=37&22=39&24=42&25=44&34=50'