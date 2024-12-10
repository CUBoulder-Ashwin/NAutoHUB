from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/priority-flow-control.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_priority_flow_control = resolve('priority_flow_control')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control)):
        pass
        yield '!\n'
        if t_1(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'all_off'), True):
            pass
            yield 'priority-flow-control all off\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'timeout')):
            pass
            yield 'priority-flow-control pause watchdog default timeout '
            yield str(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'timeout'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'recovery_time')):
            pass
            yield 'priority-flow-control pause watchdog default recovery-time '
            yield str(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'recovery_time'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'polling_interval')):
            pass
            yield 'priority-flow-control pause watchdog default polling-interval '
            yield str(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'polling_interval'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'action')):
            pass
            yield 'priority-flow-control pause watchdog action '
            yield str(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'action'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'override_action_drop'), True):
            pass
            yield 'priority-flow-control pause watchdog override action drop\n'

blocks = {}
debug_info = '7=18&9=21&12=24&13=27&15=29&16=32&18=34&19=37&21=39&22=42&24=44'