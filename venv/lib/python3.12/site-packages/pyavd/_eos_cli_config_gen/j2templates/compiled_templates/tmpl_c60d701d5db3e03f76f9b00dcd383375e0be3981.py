from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/peer-filters.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_peer_filters = resolve('peer_filters')
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
    for l_1_peer_filter in t_1((undefined(name='peer_filters') if l_0_peer_filters is missing else l_0_peer_filters), 'name'):
        _loop_vars = {}
        pass
        yield '!\npeer-filter '
        yield str(environment.getattr(l_1_peer_filter, 'name'))
        yield '\n'
        for l_2_sequence in t_1(environment.getattr(l_1_peer_filter, 'sequence_numbers'), 'sequence'):
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_2_sequence, 'match')):
                pass
                yield '   '
                yield str(environment.getattr(l_2_sequence, 'sequence'))
                yield ' match '
                yield str(environment.getattr(l_2_sequence, 'match'))
                yield '\n'
        l_2_sequence = missing
    l_1_peer_filter = missing

blocks = {}
debug_info = '7=24&9=28&10=30&11=33&12=36'