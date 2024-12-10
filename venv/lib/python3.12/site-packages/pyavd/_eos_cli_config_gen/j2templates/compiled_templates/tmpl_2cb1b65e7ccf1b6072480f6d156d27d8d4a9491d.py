from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/priority-flow-control.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_priority_flow_control = resolve('priority_flow_control')
    l_0_action = resolve('action')
    l_0_timeout = resolve('timeout')
    l_0_recovery = resolve('recovery')
    l_0_polling = resolve('polling')
    l_0_override = resolve('override')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control)):
        pass
        yield '\n### Priority Flow Control\n\n#### Global Settings\n'
        if t_2(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'all_off'), True):
            pass
            yield '\nPriority Flow Control is **Off** on all interfaces.\n'
        if t_2(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog')):
            pass
            l_0_action = t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'action'), 'errdisable')
            context.vars['action'] = l_0_action
            context.exported_vars.add('action')
            l_0_timeout = t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'timeout'), '-')
            context.vars['timeout'] = l_0_timeout
            context.exported_vars.add('timeout')
            l_0_recovery = t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'recovery_time'), '-')
            context.vars['recovery'] = l_0_recovery
            context.exported_vars.add('recovery')
            l_0_polling = t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'polling_interval'), '-')
            context.vars['polling'] = l_0_polling
            context.exported_vars.add('polling')
            l_0_override = t_1(environment.getattr(environment.getattr((undefined(name='priority_flow_control') if l_0_priority_flow_control is missing else l_0_priority_flow_control), 'watchdog'), 'override_action_drop'), 'false')
            context.vars['override'] = l_0_override
            context.exported_vars.add('override')
            yield '\n##### Priority Flow Control Watchdog Settings\n\n| Action | Timeout | Recovery | Polling | Override Action Drop |\n| ------ | ------- | -------- | ------- |\n| '
            yield str((undefined(name='action') if l_0_action is missing else l_0_action))
            yield ' | '
            yield str((undefined(name='timeout') if l_0_timeout is missing else l_0_timeout))
            yield ' | '
            yield str((undefined(name='recovery') if l_0_recovery is missing else l_0_recovery))
            yield ' | '
            yield str((undefined(name='polling') if l_0_polling is missing else l_0_polling))
            yield ' | '
            yield str((undefined(name='override') if l_0_override is missing else l_0_override))
            yield ' |\n'
        yield '\n```eos\n'
        template = environment.get_template('eos/priority-flow-control.j2', 'documentation/priority-flow-control.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'action': l_0_action, 'override': l_0_override, 'polling': l_0_polling, 'recovery': l_0_recovery, 'timeout': l_0_timeout})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=29&12=32&16=35&17=37&18=40&19=43&20=46&21=49&27=53&31=64'