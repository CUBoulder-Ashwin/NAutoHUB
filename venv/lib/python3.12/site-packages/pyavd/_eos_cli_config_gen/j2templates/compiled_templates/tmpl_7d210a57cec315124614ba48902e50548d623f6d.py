from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/match-list-input.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_match_list_input = resolve('match_list_input')
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
    if t_2((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input)):
        pass
        if t_2(environment.getattr((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input), 'string')):
            pass
            yield '!\n'
            for l_1_match_list in t_1(environment.getattr((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input), 'string'), 'name'):
                _loop_vars = {}
                pass
                yield 'match-list input string '
                yield str(environment.getattr(l_1_match_list, 'name'))
                yield '\n'
                for l_2_sequence in t_1(environment.getattr(l_1_match_list, 'sequence_numbers'), 'sequence'):
                    _loop_vars = {}
                    pass
                    if t_2(environment.getattr(l_2_sequence, 'match_regex')):
                        pass
                        yield '   '
                        yield str(environment.getattr(l_2_sequence, 'sequence'))
                        yield ' match regex '
                        yield str(environment.getattr(l_2_sequence, 'match_regex'))
                        yield '\n'
                l_2_sequence = missing
            l_1_match_list = missing
        if t_2(environment.getattr((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input), 'prefix_ipv4')):
            pass
            yield '!\n'
            for l_1_match_list in t_1(environment.getattr((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input), 'prefix_ipv4'), 'name'):
                _loop_vars = {}
                pass
                yield 'match-list input prefix-ipv4 '
                yield str(environment.getattr(l_1_match_list, 'name'))
                yield '\n'
                for l_2_entry in environment.getattr(l_1_match_list, 'prefixes'):
                    _loop_vars = {}
                    pass
                    yield '   match prefix-ipv4 '
                    yield str(l_2_entry)
                    yield '\n'
                l_2_entry = missing
            l_1_match_list = missing
        if t_2(environment.getattr((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input), 'prefix_ipv6')):
            pass
            yield '!\n'
            for l_1_match_list in t_1(environment.getattr((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input), 'prefix_ipv6'), 'name'):
                _loop_vars = {}
                pass
                yield 'match-list input prefix-ipv6 '
                yield str(environment.getattr(l_1_match_list, 'name'))
                yield '\n'
                for l_2_entry in environment.getattr(l_1_match_list, 'prefixes'):
                    _loop_vars = {}
                    pass
                    yield '   match prefix-ipv6 '
                    yield str(l_2_entry)
                    yield '\n'
                l_2_entry = missing
            l_1_match_list = missing

blocks = {}
debug_info = '7=24&8=26&10=29&11=33&12=35&13=38&14=41&19=47&21=50&22=54&23=56&24=60&28=64&30=67&31=71&32=73&33=77'