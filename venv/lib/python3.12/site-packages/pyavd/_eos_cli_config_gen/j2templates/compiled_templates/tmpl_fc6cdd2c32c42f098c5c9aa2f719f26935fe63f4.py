from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/agents.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_agents = resolve('agents')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_1_loop = missing
    for l_1_agent, l_1_loop in LoopContext(t_1((undefined(name='agents') if l_0_agents is missing else l_0_agents), 'name'), undefined):
        l_1_env_list = resolve('env_list')
        _loop_vars = {}
        pass
        if environment.getattr(l_1_loop, 'first'):
            pass
            yield '!\n'
        if t_3(environment.getattr(l_1_agent, 'environment_variables')):
            pass
            l_1_env_list = []
            _loop_vars['env_list'] = l_1_env_list
            for l_2_envvar in environment.getattr(l_1_agent, 'environment_variables'):
                _loop_vars = {}
                pass
                context.call(environment.getattr((undefined(name='env_list') if l_1_env_list is missing else l_1_env_list), 'append'), str_join((environment.getattr(l_2_envvar, 'name'), '=', environment.getattr(l_2_envvar, 'value'), )), _loop_vars=_loop_vars)
            l_2_envvar = missing
            yield 'agent '
            yield str(environment.getattr(l_1_agent, 'name'))
            yield ' environment '
            yield str(t_2(context.eval_ctx, (undefined(name='env_list') if l_1_env_list is missing else l_1_env_list), ':'))
            yield '\n'
    l_1_loop = l_1_agent = l_1_env_list = missing

blocks = {}
debug_info = '7=31&8=35&11=38&12=40&13=42&14=45&16=48'