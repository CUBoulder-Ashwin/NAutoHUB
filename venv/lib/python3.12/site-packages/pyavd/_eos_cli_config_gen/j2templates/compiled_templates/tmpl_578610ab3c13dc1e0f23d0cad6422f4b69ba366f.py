from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/mlag-configuration.j2'

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
        yield '!\nmlag configuration\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'domain_id')):
            pass
            yield '   domain-id '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'domain_id'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'heartbeat_interval')):
            pass
            yield '   heartbeat-interval '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'heartbeat_interval'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'local_interface')):
            pass
            yield '   local-interface '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'local_interface'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address')):
            pass
            yield '   peer-address '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address_heartbeat'), 'peer_ip')):
            pass
            if (t_1(environment.getattr(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address_heartbeat'), 'vrf')) and (environment.getattr(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address_heartbeat'), 'vrf') != 'default')):
                pass
                yield '   peer-address heartbeat '
                yield str(environment.getattr(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address_heartbeat'), 'peer_ip'))
                yield ' vrf '
                yield str(environment.getattr(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address_heartbeat'), 'vrf'))
                yield '\n'
            else:
                pass
                yield '   peer-address heartbeat '
                yield str(environment.getattr(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_address_heartbeat'), 'peer_ip'))
                yield '\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_link')):
            pass
            yield '   peer-link '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'peer_link'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_detection_delay')):
            pass
            yield '   dual-primary detection delay '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_detection_delay'))
            yield ' action errdisable all-interfaces\n'
        if (t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_recovery_delay_mlag')) and t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_recovery_delay_non_mlag'))):
            pass
            yield '   dual-primary recovery delay mlag '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_recovery_delay_mlag'))
            yield ' non-mlag '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'dual_primary_recovery_delay_non_mlag'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'reload_delay_mlag')):
            pass
            yield '   reload-delay mlag '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'reload_delay_mlag'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'reload_delay_non_mlag')):
            pass
            yield '   reload-delay non-mlag '
            yield str(environment.getattr((undefined(name='mlag_configuration') if l_0_mlag_configuration is missing else l_0_mlag_configuration), 'reload_delay_non_mlag'))
            yield '\n'

blocks = {}
debug_info = '7=18&10=21&11=24&13=26&14=29&16=31&17=34&19=36&20=39&22=41&23=43&24=46&27=53&30=55&31=58&33=60&34=63&36=65&38=68&40=72&41=75&43=77&44=80'