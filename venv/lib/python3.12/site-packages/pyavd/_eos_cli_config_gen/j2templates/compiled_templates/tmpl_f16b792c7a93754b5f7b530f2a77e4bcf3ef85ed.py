from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/tap-aggregation.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tap_aggregation = resolve('tap_aggregation')
    l_0_mode_cli = resolve('mode_cli')
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
    if t_2((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation)):
        pass
        yield '!\ntap aggregation\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive')):
            pass
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'enabled'), True):
                pass
                l_0_mode_cli = 'mode exclusive'
                context.vars['mode_cli'] = l_0_mode_cli
                context.exported_vars.add('mode_cli')
                if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'profile')):
                    pass
                    l_0_mode_cli = str_join(((undefined(name='mode_cli') if l_0_mode_cli is missing else l_0_mode_cli), ' profile ', environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'profile'), ))
                    context.vars['mode_cli'] = l_0_mode_cli
                    context.exported_vars.add('mode_cli')
                yield '   '
                yield str((undefined(name='mode_cli') if l_0_mode_cli is missing else l_0_mode_cli))
                yield '\n'
        if t_2(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'encapsulation_dot1br_strip'), True):
            pass
            yield '   encapsulation dot1br strip\n'
        if t_2(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'encapsulation_vn_tag_strip'), True):
            pass
            yield '   encapsulation vn-tag strip\n'
        if t_2(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'protocol_lldp_trap'), True):
            pass
            yield '   protocol lldp trap\n'
        for l_1_interface in t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mode'), 'exclusive'), 'no_errdisable')):
            _loop_vars = {}
            pass
            yield '   mode exclusive no-errdisable '
            yield str(l_1_interface)
            yield '\n'
        l_1_interface = missing
        if t_2(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'truncation_size')):
            pass
            yield '   truncation size '
            yield str(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'truncation_size'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'replace_source_mac'), True):
            pass
            yield '   mac timestamp replace source-mac\n'
        elif t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header')):
            pass
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header'), 'format')):
                pass
                yield '   mac timestamp header format '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header'), 'format'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header'), 'eth_type')):
                pass
                yield '   mac timestamp header eth-type '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'timestamp'), 'header'), 'eth_type'))
                yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'fcs_append'), True):
            pass
            yield '   mac fcs append\n'
        elif t_2(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'fcs_error')):
            pass
            yield '   mac fcs-error '
            yield str(environment.getattr(environment.getattr((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation), 'mac'), 'fcs_error'))
            yield '\n'

blocks = {}
debug_info = '7=25&10=28&11=30&12=32&13=35&14=37&16=41&19=43&22=46&25=49&28=52&29=56&31=59&32=62&34=64&36=67&37=69&38=72&40=74&41=77&44=79&46=82&47=85'