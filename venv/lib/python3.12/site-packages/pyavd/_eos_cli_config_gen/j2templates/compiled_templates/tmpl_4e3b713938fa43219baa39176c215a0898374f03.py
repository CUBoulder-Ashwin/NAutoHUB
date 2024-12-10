from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/switchport-default.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_switchport_default = resolve('switchport_default')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'mode'), 'routed'):
        pass
        yield '!\nswitchport default mode routed\n'
    elif t_1(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'mode'), 'access'):
        pass
        yield '!\nswitchport default mode access\n'
    if t_1(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'cos')):
        pass
        yield '!\nswitchport default phone cos '
        yield str(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'cos'))
        yield '\n'
    if (t_1(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'trunk')) and (environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'trunk') == 'untagged')):
        pass
        yield '!\nswitchport default phone trunk untagged\n'
    if (t_1(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'vlan')) and environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'vlan')):
        pass
        yield '!\nswitchport default phone vlan '
        yield str(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'vlan'))
        yield '\n'

blocks = {}
debug_info = '7=18&10=21&15=24&17=27&19=29&23=32&25=35'