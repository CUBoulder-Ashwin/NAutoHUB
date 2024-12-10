from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-segment-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_segment_security = resolve('router_segment_security')
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
    if t_3((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security)):
        pass
        yield '\n## Group-Based Multi-domain Segmentation Services (MSS-Group)\n'
        if t_3(environment.getattr((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security), 'enabled'), True):
            pass
            yield '\nMSS-G is enabled.\n'
        else:
            pass
            yield '\nMSS-G is disabled.\n'
        if t_3(environment.getattr((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security), 'policies')):
            pass
            yield '\n### Segmentation Policies\n'
            for l_1_policy in t_2(environment.getattr((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security), 'policies'), 'name'):
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_policy, 'name')):
                    pass
                    yield '\n#### '
                    yield str(environment.getattr(l_1_policy, 'name'))
                    yield '\n\n| Sequence Number | Application Name | Action | Next-Hop | Log | Stateless |\n| --------------- | ---------------- | ------ | -------- | --- | --------- |\n'
                    for l_2_entry in t_2(environment.getattr(l_1_policy, 'sequence_numbers'), 'sequence'):
                        _loop_vars = {}
                        pass
                        yield '| '
                        yield str(t_1(environment.getattr(l_2_entry, 'sequence'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_entry, 'application'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_entry, 'action'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_entry, 'next_hop'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_entry, 'log'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_entry, 'stateless'), '-'))
                        yield ' |\n'
                    l_2_entry = missing
            l_1_policy = missing
        if t_3(environment.getattr((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security), 'vrfs')):
            pass
            yield '\n### Segment Definitions\n'
            for l_1_vrf in t_2(environment.getattr((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security), 'vrfs'), 'name'):
                _loop_vars = {}
                pass
                yield '\n#### VRF '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' Segmentation\n'
                for l_2_segment in t_2(environment.getattr(l_1_vrf, 'segments'), 'name'):
                    _loop_vars = {}
                    pass
                    yield '\n##### Segment '
                    yield str(environment.getattr(l_2_segment, 'name'))
                    yield ' Definitions\n\n| Interface | Match-List Name | Covered Prefix-List Name | Address Family |\n| --------- |---------------- | ------------------------ | -------------- |\n'
                    if t_3(environment.getattr(environment.getattr(l_2_segment, 'definition'), 'interfaces')):
                        pass
                        for l_3_interface in t_2(environment.getattr(environment.getattr(l_2_segment, 'definition'), 'interfaces')):
                            _loop_vars = {}
                            pass
                            yield '| '
                            yield str(l_3_interface)
                            yield ' | - | - | - |\n'
                        l_3_interface = missing
                    if t_3(environment.getattr(environment.getattr(l_2_segment, 'definition'), 'match_lists')):
                        pass
                        for l_3_match_list in environment.getattr(environment.getattr(l_2_segment, 'definition'), 'match_lists'):
                            _loop_vars = {}
                            pass
                            yield '| - | '
                            yield str(t_1(environment.getattr(l_3_match_list, 'prefix'), '-'))
                            yield ' | '
                            yield str(t_1(environment.getattr(l_3_match_list, 'covered_prefix_list'), '-'))
                            yield ' | '
                            yield str(environment.getattr(l_3_match_list, 'address_family'))
                            yield ' |\n'
                        l_3_match_list = missing
                    yield '\n##### Segment '
                    yield str(environment.getattr(l_2_segment, 'name'))
                    yield ' Policies\n\n| Source Segment | Policy Applied |\n| -------------- | -------------- |\n'
                    for l_3_policy in t_2(environment.getattr(l_2_segment, 'policies'), 'from'):
                        _loop_vars = {}
                        pass
                        if (t_3(environment.getattr(l_3_policy, 'from')) and t_3(environment.getattr(l_3_policy, 'policy'))):
                            pass
                            yield '| '
                            yield str(environment.getattr(l_3_policy, 'from'))
                            yield ' | '
                            yield str(environment.getattr(l_3_policy, 'policy'))
                            yield ' |\n'
                    l_3_policy = missing
                    if t_3(environment.getattr(l_2_segment, 'fallback_policy')):
                        pass
                        yield '\nConfigured Fallback Policy: '
                        yield str(environment.getattr(l_2_segment, 'fallback_policy'))
                        yield '\n'
                l_2_segment = missing
            l_1_vrf = missing
        yield '\n### Router MSS-G Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-segment-security.j2', 'documentation/router-segment-security.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&10=33&17=39&20=42&21=45&23=48&27=50&28=54&33=68&36=71&38=75&39=77&41=81&45=83&46=85&47=89&50=92&51=94&52=98&56=106&60=108&61=111&62=114&65=119&67=122&76=127'