from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/tap-aggregation.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tap_aggregation = resolve('tap_aggregation')
    try:
        t_1 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_2((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation)) and t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'enabled'), True)):
        pass
        yield '\n### Tap Aggregation\n\n#### Tap Aggregation Summary\n\n| Settings | Values |\n| -------- | ------ |\n| Mode Exclusive | '
        yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'enabled'))
        yield ' |\n'
        if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'profile')):
            pass
            yield '| Mode Exclusive Profile | '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'profile'))
            yield ' |\n'
        if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'no_errdisable')):
            pass
            yield '| Mode Exclusive No-Errdisable | '
            yield str(t_1(context.eval_ctx, environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'no_errdisable'), ', '))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'encapsulation_dot1br_strip'), True):
            pass
            yield '| Encapsulation Dot1br Strip | '
            yield str(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'encapsulation_dot1br_strip'))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'encapsulation_vn_tag_strip'), True):
            pass
            yield '| Encapsulation Vn Tag Strip | '
            yield str(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'encapsulation_vn_tag_strip'))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'protocol_lldp_trap'), True):
            pass
            yield '| Protocol LLDP Trap | '
            yield str(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'protocol_lldp_trap'))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'truncation_size')):
            pass
            yield '| Truncation Size | '
            yield str(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'truncation_size'))
            yield ' |\n'
        if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'replace_source_mac'), True):
            pass
            yield '| Mac Timestamp | Replace Source-Mac |\n'
        elif t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header')):
            pass
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header'), 'format')):
                pass
                yield '| Mac Timestamp | Header Format '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header'), 'format'))
                yield ' |\n'
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header'), 'eth_type')):
                pass
                yield '| Mac Timestamp | Header eth-type '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header'), 'eth_type'))
                yield ' |\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'fcs_append'), True):
            pass
            yield '| Mac FCS Append | '
            yield str(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'fcs_append'))
            yield ' |\n'
        elif t_2(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'fcs_error')):
            pass
            yield '| Mac FCS Error | '
            yield str(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'fcs_error'))
            yield ' |\n'
        yield '\n#### Tap Aggregation Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/tap-aggregation.j2', 'documentation/tap-aggregation.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&15=27&16=29&17=32&19=34&20=37&22=39&23=42&25=44&26=47&28=49&29=52&31=54&32=57&34=59&36=62&37=64&38=67&40=69&41=72&44=74&45=77&46=79&47=82&53=85'