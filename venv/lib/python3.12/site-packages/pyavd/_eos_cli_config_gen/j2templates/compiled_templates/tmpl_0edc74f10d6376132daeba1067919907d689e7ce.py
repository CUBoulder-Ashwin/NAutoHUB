from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/roles.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_roles = resolve('roles')
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
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='roles') if l_0_roles is missing else l_0_roles)):
        pass
        yield '\n### Roles\n\n#### Roles Summary\n'
        for l_1_role in t_2((undefined(name='roles') if l_0_roles is missing else l_0_roles)):
            _loop_vars = {}
            pass
            yield '\n##### Role '
            yield str(environment.getattr(l_1_role, 'name'))
            yield '\n\n| Sequence | Action | Mode | Command |\n| -------- | ------ | ---- | ------- |\n'
            for l_2_sequence in t_1(environment.getattr(l_1_role, 'sequence_numbers'), []):
                _loop_vars = {}
                pass
                if (t_3(environment.getattr(l_2_sequence, 'action')) and t_3(environment.getattr(l_2_sequence, 'command'))):
                    pass
                    yield '| '
                    yield str(t_1(environment.getattr(l_2_sequence, 'sequence'), '-'))
                    yield ' | '
                    yield str(environment.getattr(l_2_sequence, 'action'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_2_sequence, 'mode'), '-'))
                    yield ' | '
                    yield str(environment.getattr(l_2_sequence, 'command'))
                    yield ' |\n'
            l_2_sequence = missing
        l_1_role = missing
        yield '\n#### Roles Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/roles.j2', 'documentation/roles.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&14=37&18=39&19=42&20=45&28=56'