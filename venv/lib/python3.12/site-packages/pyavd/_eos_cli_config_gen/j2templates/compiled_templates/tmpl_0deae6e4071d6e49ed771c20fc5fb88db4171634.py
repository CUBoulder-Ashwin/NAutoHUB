from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/monitor-connectivity.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_connectivity = resolve('monitor_connectivity')
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
    if t_3((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity)):
        pass
        yield '\n## Monitor Connectivity\n\n### Global Configuration\n'
        if t_3(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'interface_sets')):
            pass
            yield '\n#### Interface Sets\n\n| Name | Interfaces |\n| ---- | ---------- |\n'
            for l_1_interface_set in t_2(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'interface_sets'), 'name'):
                _loop_vars = {}
                pass
                if (t_3(environment.getattr(l_1_interface_set, 'name')) and t_3(environment.getattr(l_1_interface_set, 'interfaces'))):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_interface_set, 'name'))
                    yield ' | '
                    yield str(environment.getattr(l_1_interface_set, 'interfaces'))
                    yield ' |\n'
            l_1_interface_set = missing
        yield '\n#### Probing Configuration\n\n| Enabled | Interval | Default Interface Set | Address Only |\n| ------- | -------- | --------------------- | ------------ |\n| '
        yield str((not t_1(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'shutdown'), True)))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'interval'), '-'))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'local_interfaces'), '-'))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'address_only'), True))
        yield ' |\n'
        if t_3(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'hosts')):
            pass
            yield '\n#### Host Parameters\n\n| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |\n| --------- | ----------- | ------------ | --------------------- | ------------ | --- |\n'
            for l_1_host in t_2(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'hosts'), 'name'):
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_host, 'name')):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_host, 'name'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_host, 'description'), '-'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_host, 'ip'), '-'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_host, 'local_interfaces'), '-'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_host, 'address_only'), True))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_host, 'url'), '-'))
                    yield ' |\n'
            l_1_host = missing
        if t_3(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'vrfs')):
            pass
            yield '\n### VRF Configuration\n\n| Name | Description | Default Interface Set | Address Only |\n| ---- | ----------- | --------------------- | ------------ |\n'
            for l_1_vrf in t_2(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'vrfs'), 'name'):
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_vrf, 'name')):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_vrf, 'name'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_vrf, 'description'), '-'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_vrf, 'local_interfaces'), '-'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_vrf, 'address_only'), True))
                    yield ' |\n'
            l_1_vrf = missing
            for l_1_vrf in t_2(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'vrfs'), 'name'):
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_vrf, 'name')):
                    pass
                    yield '\n#### Vrf '
                    yield str(environment.getattr(l_1_vrf, 'name'))
                    yield ' Configuration\n'
                    if t_3(environment.getattr(l_1_vrf, 'interface_sets')):
                        pass
                        yield '\n##### Interface Sets\n\n| Name | Interfaces |\n| ---- | ---------- |\n'
                        for l_2_interface_set in t_2(environment.getattr(l_1_vrf, 'interface_sets'), 'name'):
                            _loop_vars = {}
                            pass
                            if (t_3(environment.getattr(l_2_interface_set, 'name')) and t_3(environment.getattr(l_2_interface_set, 'interfaces'))):
                                pass
                                yield '| '
                                yield str(environment.getattr(l_2_interface_set, 'name'))
                                yield ' | '
                                yield str(environment.getattr(l_2_interface_set, 'interfaces'))
                                yield ' |\n'
                        l_2_interface_set = missing
                    if t_3(environment.getattr(l_1_vrf, 'hosts')):
                        pass
                        yield '\n##### Host Parameters\n\n| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |\n| --------- | ----------- | ------------ | --------------------- | ------------ | --- |\n'
                        for l_2_host in t_2(environment.getattr(l_1_vrf, 'hosts'), 'name'):
                            _loop_vars = {}
                            pass
                            if t_3(environment.getattr(l_2_host, 'name')):
                                pass
                                yield '| '
                                yield str(environment.getattr(l_2_host, 'name'))
                                yield ' | '
                                yield str(t_1(environment.getattr(l_2_host, 'description'), '-'))
                                yield ' | '
                                yield str(t_1(environment.getattr(l_2_host, 'ip'), '-'))
                                yield ' | '
                                yield str(t_1(environment.getattr(l_2_host, 'local_interfaces'), '-'))
                                yield ' | '
                                yield str(t_1(environment.getattr(l_2_host, 'address_only'), True))
                                yield ' | '
                                yield str(t_1(environment.getattr(l_2_host, 'url'), '-'))
                                yield ' |\n'
                        l_2_host = missing
            l_1_vrf = missing
        yield '\n### Monitor Connectivity Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/monitor-connectivity.j2', 'documentation/monitor-connectivity.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&18=36&19=39&20=42&29=48&30=56&36=59&37=62&38=65&42=78&48=81&49=84&50=87&53=96&54=99&56=102&57=104&63=107&64=110&65=113&69=118&75=121&76=124&77=127&88=142'