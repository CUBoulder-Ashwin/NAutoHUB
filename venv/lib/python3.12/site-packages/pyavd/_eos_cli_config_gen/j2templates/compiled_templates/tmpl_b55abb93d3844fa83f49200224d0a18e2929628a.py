from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/route-maps.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_route_maps = resolve('route_maps')
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
    if t_4((undefined(name='route_maps') if l_0_route_maps is missing else l_0_route_maps)):
        pass
        yield '\n### Route-maps\n\n#### Route-maps Summary\n\n'
        for l_1_route_map in t_2((undefined(name='route_maps') if l_0_route_maps is missing else l_0_route_maps), 'name'):
            _loop_vars = {}
            pass
            yield '##### '
            yield str(environment.getattr(l_1_route_map, 'name'))
            yield '\n\n| Sequence | Type | Match | Set | Sub-Route-Map | Continue |\n| -------- | ---- | ----- | --- | ------------- | -------- |\n'
            for l_2_sequence in t_2(environment.getattr(l_1_route_map, 'sequence_numbers'), 'sequence'):
                l_2_row_continue = resolve('row_continue')
                _loop_vars = {}
                pass
                if t_4(environment.getattr(environment.getattr(l_2_sequence, 'continue'), 'enabled'), True):
                    pass
                    l_2_row_continue = t_1(environment.getattr(environment.getattr(l_2_sequence, 'continue'), 'sequence_number'), 'Next Sequence')
                    _loop_vars['row_continue'] = l_2_row_continue
                yield '| '
                yield str(environment.getattr(l_2_sequence, 'sequence'))
                yield ' | '
                yield str(environment.getattr(l_2_sequence, 'type'))
                yield ' | '
                yield str(t_3(context.eval_ctx, t_1(environment.getattr(l_2_sequence, 'match'), ['-']), '<br>'))
                yield ' | '
                yield str(t_3(context.eval_ctx, t_1(environment.getattr(l_2_sequence, 'set'), ['-']), '<br>'))
                yield ' | '
                yield str(t_1(environment.getattr(l_2_sequence, 'sub_route_map'), '-'))
                yield ' | '
                yield str(t_1((undefined(name='row_continue') if l_2_row_continue is missing else l_2_row_continue), '-'))
                yield ' |\n'
            l_2_sequence = l_2_row_continue = missing
            yield '\n'
        l_1_route_map = missing
        yield '#### Route-maps Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/route-maps.j2', 'documentation/route-maps.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&13=39&14=43&18=45&19=49&20=51&22=54&29=70'