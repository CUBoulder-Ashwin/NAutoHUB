from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/l2-protocol-forwarding.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_l2_protocol = resolve('l2_protocol')
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
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    pass
    if (t_3(t_1(environment.getattr((undefined(name='l2_protocol') if l_0_l2_protocol is missing else l_0_l2_protocol), 'forwarding_profiles'), [])) > 0):
        pass
        yield '\n## L2 Protocol Forwarding\n\n### Forwarding Profiles\n'
        for l_1_profile in t_2(environment.getattr((undefined(name='l2_protocol') if l_0_l2_protocol is missing else l_0_l2_protocol), 'forwarding_profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '\n#### '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n\n| Protocol | Forward | Tagged Forward | Untagged Forward |\n| -------- | ------- | -------------- | ---------------- |\n'
            for l_2_protocol in environment.getattr(l_1_profile, 'protocols'):
                l_2_proto_forward = l_2_proto_tagged_forward = l_2_proto_untagged_forward = missing
                _loop_vars = {}
                pass
                l_2_proto_forward = t_1(environment.getattr(l_2_protocol, 'forward'), '-')
                _loop_vars['proto_forward'] = l_2_proto_forward
                l_2_proto_tagged_forward = t_1(environment.getattr(l_2_protocol, 'tagged_forward'), '-')
                _loop_vars['proto_tagged_forward'] = l_2_proto_tagged_forward
                l_2_proto_untagged_forward = t_1(environment.getattr(l_2_protocol, 'untagged_forward'), '-')
                _loop_vars['proto_untagged_forward'] = l_2_proto_untagged_forward
                yield '| '
                yield str(environment.getattr(l_2_protocol, 'name'))
                yield ' | '
                yield str((undefined(name='proto_forward') if l_2_proto_forward is missing else l_2_proto_forward))
                yield ' | '
                yield str((undefined(name='proto_tagged_forward') if l_2_proto_tagged_forward is missing else l_2_proto_tagged_forward))
                yield ' | '
                yield str((undefined(name='proto_untagged_forward') if l_2_proto_untagged_forward is missing else l_2_proto_untagged_forward))
                yield ' |\n'
            l_2_protocol = l_2_proto_forward = l_2_proto_tagged_forward = l_2_proto_untagged_forward = missing
        l_1_profile = missing
        yield '\n### L2 Protocol Forwarding Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/l2-protocol-forwarding.j2', 'documentation/l2-protocol-forwarding.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&14=37&18=39&19=43&20=45&21=47&22=50&29=61'