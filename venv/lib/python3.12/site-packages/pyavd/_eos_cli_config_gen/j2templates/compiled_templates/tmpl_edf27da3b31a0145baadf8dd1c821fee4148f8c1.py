from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/monitor-session-default-encapsulation-gre.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_session_default_encapsulation_gre = resolve('monitor_session_default_encapsulation_gre')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='monitor_session_default_encapsulation_gre') if l_0_monitor_session_default_encapsulation_gre is missing else l_0_monitor_session_default_encapsulation_gre), 'payload')):
        pass
        yield '!\nmonitor session default encapsulation gre payload '
        yield str(environment.getattr((undefined(name='monitor_session_default_encapsulation_gre') if l_0_monitor_session_default_encapsulation_gre is missing else l_0_monitor_session_default_encapsulation_gre), 'payload'))
        yield '\n'

blocks = {}
debug_info = '7=18&9=21'