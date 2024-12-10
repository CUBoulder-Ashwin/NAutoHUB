from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/switchport-port-security.j2'

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
        yield '!\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'mac_address'), 'aging'), True):
            pass
            yield 'switchport port-security mac-address aging\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'mac_address'), 'moveable'), True):
            pass
            yield 'switchport port-security mac-address moveable\n'
        if t_1(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'persistence_disabled'), True):
            pass
            yield 'switchport port-security persistence disabled\n'
        if t_1(environment.getattr((undefined(name='switchport_port_security') if l_0_switchport_port_security is missing else l_0_switchport_port_security), 'violation_protect_chip_based'), True):
            pass
            yield 'switchport port-security violation protect chip-based\n'

blocks = {}
debug_info = '7=18&9=21&12=24&15=27&18=30'