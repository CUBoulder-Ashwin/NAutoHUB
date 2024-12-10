from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dot1x_part2.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dot1x = resolve('dot1x')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (((t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'system_auth_control'), True) or t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'protocol_lldp_bypass'), True)) or t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'protocol_bpdu_bypass'), True)) or t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'dynamic_authorization'), True)):
        pass
        yield '!\n'
    if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'system_auth_control'), True):
        pass
        yield 'dot1x system-auth-control\n'
    if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'protocol_lldp_bypass'), True):
        pass
        yield 'dot1x protocol lldp bypass\n'
    if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'protocol_bpdu_bypass'), True):
        pass
        yield 'dot1x protocol bpdu bypass\n'
    if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'dynamic_authorization'), True):
        pass
        yield 'dot1x dynamic-authorization\n'

blocks = {}
debug_info = '7=18&11=21&14=24&17=27&20=30'