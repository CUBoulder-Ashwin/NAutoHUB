from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/agents.j2'

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
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='agents') if l_0_agents is missing else l_0_agents)):
        pass
        yield '\n### Agents\n'
        for l_1_agent in t_1((undefined(name='agents') if l_0_agents is missing else l_0_agents), 'name'):
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_agent, 'environment_variables')):
                pass
                yield '\n#### Agent '
                yield str(environment.getattr(l_1_agent, 'name'))
                yield '\n\n##### Environment Variables\n\n| Name | Value |\n| ---- | ----- |\n'
                for l_2_envvar in environment.getattr(l_1_agent, 'environment_variables'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_2_envvar, 'name'))
                    yield ' | '
                    yield str(environment.getattr(l_2_envvar, 'value'))
                    yield ' |\n'
                l_2_envvar = missing
        l_1_agent = missing
        yield '\n#### Agents Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/agents.j2', 'documentation/agents.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&10=27&12=30&14=33&20=35&21=39&29=46'