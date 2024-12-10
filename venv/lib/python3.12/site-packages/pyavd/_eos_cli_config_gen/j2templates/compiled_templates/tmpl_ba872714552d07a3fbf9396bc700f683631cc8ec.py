from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-internet-exit.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_internet_exit = resolve('router_internet_exit')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='router_internet_exit') if l_0_router_internet_exit is missing else l_0_router_internet_exit)):
        pass
        yield '\n### Router Internet Exit\n'
        if t_4(environment.getattr((undefined(name='router_internet_exit') if l_0_router_internet_exit is missing else l_0_router_internet_exit), 'exit_groups')):
            pass
            yield '\n#### Exit Groups\n\n| Exit Group Name | Local Connections | Fib Default |\n| --------------- | ----------------- | ----------- |\n'
            for l_1_exit_group in t_2(environment.getattr((undefined(name='router_internet_exit') if l_0_router_internet_exit is missing else l_0_router_internet_exit), 'exit_groups'), 'name'):
                l_1_local_connections = l_1_fib_default = missing
                _loop_vars = {}
                pass
                l_1_local_connections = []
                _loop_vars['local_connections'] = l_1_local_connections
                l_1_fib_default = t_1(environment.getattr(l_1_exit_group, 'fib_default'), '-')
                _loop_vars['fib_default'] = l_1_fib_default
                for l_2_local_connection in t_2(environment.getattr(l_1_exit_group, 'local_connections'), 'name'):
                    _loop_vars = {}
                    pass
                    context.call(environment.getattr((undefined(name='local_connections') if l_1_local_connections is missing else l_1_local_connections), 'append'), environment.getattr(l_2_local_connection, 'name'), _loop_vars=_loop_vars)
                l_2_local_connection = missing
                if ((undefined(name='local_connections') if l_1_local_connections is missing else l_1_local_connections) != []):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_exit_group, 'name'))
                    yield ' | '
                    yield str(t_3(context.eval_ctx, (undefined(name='local_connections') if l_1_local_connections is missing else l_1_local_connections), '<br>'))
                    yield ' | '
                    yield str((undefined(name='fib_default') if l_1_fib_default is missing else l_1_fib_default))
                    yield ' |\n'
                else:
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_exit_group, 'name'))
                    yield ' | - | '
                    yield str((undefined(name='fib_default') if l_1_fib_default is missing else l_1_fib_default))
                    yield ' |\n'
            l_1_exit_group = l_1_local_connections = l_1_fib_default = missing
        if t_4(environment.getattr((undefined(name='router_internet_exit') if l_0_router_internet_exit is missing else l_0_router_internet_exit), 'policies')):
            pass
            yield '\n#### Internet Exit Policies\n\n| Policy Name | Exit Groups |\n| ----------- | ----------- |\n'
            for l_1_policy in t_2(environment.getattr((undefined(name='router_internet_exit') if l_0_router_internet_exit is missing else l_0_router_internet_exit), 'policies'), 'name'):
                l_1_policy_exit_groups = missing
                _loop_vars = {}
                pass
                l_1_policy_exit_groups = []
                _loop_vars['policy_exit_groups'] = l_1_policy_exit_groups
                for l_2_exit_group in t_1(environment.getattr(l_1_policy, 'exit_groups'), [{'name': '-'}]):
                    _loop_vars = {}
                    pass
                    if t_4(environment.getattr(l_2_exit_group, 'name')):
                        pass
                        context.call(environment.getattr((undefined(name='policy_exit_groups') if l_1_policy_exit_groups is missing else l_1_policy_exit_groups), 'append'), environment.getattr(l_2_exit_group, 'name'), _loop_vars=_loop_vars)
                l_2_exit_group = missing
                yield '| '
                yield str(environment.getattr(l_1_policy, 'name'))
                yield ' | '
                yield str(t_3(context.eval_ctx, (undefined(name='policy_exit_groups') if l_1_policy_exit_groups is missing else l_1_policy_exit_groups), '<br>'))
                yield ' |\n'
            l_1_policy = l_1_policy_exit_groups = missing
        yield '\n#### Router Internet Exit Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-internet-exit.j2', 'documentation/router-internet-exit.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&10=39&16=42&17=46&18=48&19=50&20=53&22=55&23=58&25=67&29=72&35=75&36=79&37=81&38=84&39=86&42=89&49=95'