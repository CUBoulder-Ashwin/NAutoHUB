from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/peer-filters.j2'

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
    if t_2((undefined(name='peer_filters') if l_0_peer_filters is missing else l_0_peer_filters)):
        pass
        yield '\n### Peer Filters\n\n#### Peer Filters Summary\n'
        for l_1_peer_filter in t_1((undefined(name='peer_filters') if l_0_peer_filters is missing else l_0_peer_filters), 'name'):
            _loop_vars = {}
            pass
            yield '\n##### '
            yield str(environment.getattr(l_1_peer_filter, 'name'))
            yield '\n\n| Sequence | Match |\n| -------- | ----- |\n'
            for l_2_sequence in t_1(environment.getattr(l_1_peer_filter, 'sequence_numbers'), 'sequence'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_2_sequence, 'sequence'))
                yield ' | '
                yield str(environment.getattr(l_2_sequence, 'match'))
                yield ' |\n'
            l_2_sequence = missing
        l_1_peer_filter = missing
        yield '\n#### Peer Filters Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/peer-filters.j2', 'documentation/peer-filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&12=27&14=31&18=33&19=37&26=44'