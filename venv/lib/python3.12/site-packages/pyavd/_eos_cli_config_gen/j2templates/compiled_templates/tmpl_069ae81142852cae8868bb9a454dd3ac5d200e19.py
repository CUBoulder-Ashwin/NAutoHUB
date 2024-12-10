from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/route-maps.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_route_maps = resolve('route_maps')
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
    for l_1_route_map in t_1((undefined(name='route_maps') if l_0_route_maps is missing else l_0_route_maps), 'name'):
        _loop_vars = {}
        pass
        for l_2_sequence in t_1(environment.getattr(l_1_route_map, 'sequence_numbers'), 'sequence'):
            l_2_continue_cli = resolve('continue_cli')
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_2_sequence, 'type')):
                pass
                yield '!\nroute-map '
                yield str(environment.getattr(l_1_route_map, 'name'))
                yield ' '
                yield str(environment.getattr(l_2_sequence, 'type'))
                yield ' '
                yield str(environment.getattr(l_2_sequence, 'sequence'))
                yield '\n'
            if t_2(environment.getattr(l_2_sequence, 'description')):
                pass
                yield '   description '
                yield str(environment.getattr(l_2_sequence, 'description'))
                yield '\n'
            for l_3_match_rule in t_1(environment.getattr(l_2_sequence, 'match')):
                _loop_vars = {}
                pass
                yield '   match '
                yield str(l_3_match_rule)
                yield '\n'
            l_3_match_rule = missing
            if t_2(environment.getattr(l_2_sequence, 'sub_route_map')):
                pass
                yield '   sub-route-map '
                yield str(environment.getattr(l_2_sequence, 'sub_route_map'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(l_2_sequence, 'continue'), 'enabled'), True):
                pass
                l_2_continue_cli = 'continue'
                _loop_vars['continue_cli'] = l_2_continue_cli
                if t_2(environment.getattr(environment.getattr(l_2_sequence, 'continue'), 'sequence_number')):
                    pass
                    l_2_continue_cli = str_join(((undefined(name='continue_cli') if l_2_continue_cli is missing else l_2_continue_cli), ' ', environment.getattr(environment.getattr(l_2_sequence, 'continue'), 'sequence_number'), ))
                    _loop_vars['continue_cli'] = l_2_continue_cli
                yield '   '
                yield str((undefined(name='continue_cli') if l_2_continue_cli is missing else l_2_continue_cli))
                yield '\n'
            for l_3_set_rule in t_1(environment.getattr(l_2_sequence, 'set')):
                _loop_vars = {}
                pass
                yield '   set '
                yield str(l_3_set_rule)
                yield '\n'
            l_3_set_rule = missing
        l_2_sequence = l_2_continue_cli = missing
    l_1_route_map = missing

blocks = {}
debug_info = '7=24&8=27&9=31&11=34&13=40&14=43&16=45&17=49&19=52&20=55&22=57&23=59&24=61&25=63&27=66&29=68&30=72'