from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/switchport-port-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_switchport_port_security = resolve('switchport_port_security')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security)):
        pass
        yield '\n## Switchport Port-security\n\n### Switchport Port-security Summary\n\n| Settings | Value |\n| -------- | ----- |\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'mac_address'), 'aging'), True):
            pass
            yield '| Mac-address Aging | '
            yield str(environment.getattr(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'mac_address'), 'aging'))
            yield ' |\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'mac_address'), 'moveable'), True):
            pass
            yield '| Mac-address Moveable | '
            yield str(environment.getattr(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'mac_address'), 'moveable'))
            yield ' |\n'
        if t_1(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'persistence_disabled'), True):
            pass
            yield '| Disable Persistence | '
            yield str(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'persistence_disabled'))
            yield ' |\n'
        if t_1(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'violation_protect_chip_based'), True):
            pass
            yield '| Violation Protect Chip-based | '
            yield str(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'violation_protect_chip_based'))
            yield ' |\n'
        yield '\n### Switchport Port-security Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/switchport-port-security.j2', 'documentation/switchport-port-security.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&15=21&16=24&18=26&19=29&21=31&22=34&24=36&25=39&31=42'