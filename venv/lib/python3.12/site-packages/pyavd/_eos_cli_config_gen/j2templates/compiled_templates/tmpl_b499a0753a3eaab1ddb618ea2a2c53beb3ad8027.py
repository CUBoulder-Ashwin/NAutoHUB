from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/mpls.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mpls = resolve('mpls')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ip'), True):
        pass
        yield '!\nmpls ip\n'
    if t_1(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp')):
        pass
        yield '!\nmpls ldp\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'router_id')):
            pass
            yield '   router-id '
            yield str(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'router_id'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'transport_address_interface')):
            pass
            yield '   transport-address interface '
            yield str(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'transport_address_interface'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'interface_disabled_default'), True):
            pass
            yield '   interface disabled default\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'shutdown'), False):
            pass
            yield '   no shutdown\n'
    if (t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'icmp'), 'fragmentation_needed_tunneling'), True) or t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'icmp'), 'ttl_exceeded_tunneling'), True)):
        pass
        yield '!\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'icmp'), 'fragmentation_needed_tunneling'), True):
            pass
            yield 'mpls icmp fragmentation-needed tunneling\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'icmp'), 'ttl_exceeded_tunneling'), True):
            pass
            yield 'mpls icmp ttl-exceeded tunneling\n'

blocks = {}
debug_info = '7=18&11=21&14=24&15=27&17=29&18=32&20=34&23=37&25=40&29=43&31=46&34=49'