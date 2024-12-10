from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/qos-profiles.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_qos_profiles = resolve('qos_profiles')
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
    for l_1_profile in t_2((undefined(name='qos_profiles') if l_0_qos_profiles is missing else l_0_qos_profiles), 'name'):
        l_1_pfc_command = resolve('pfc_command')
        _loop_vars = {}
        pass
        yield '!\nqos profile '
        yield str(environment.getattr(l_1_profile, 'name'))
        yield '\n'
        if t_3(environment.getattr(l_1_profile, 'trust')):
            pass
            if (environment.getattr(l_1_profile, 'trust') == 'disabled'):
                pass
                yield '   no qos trust\n'
            else:
                pass
                yield '   qos trust '
                yield str(environment.getattr(l_1_profile, 'trust'))
                yield '\n'
        if t_3(environment.getattr(l_1_profile, 'cos')):
            pass
            yield '   qos cos '
            yield str(environment.getattr(l_1_profile, 'cos'))
            yield '\n'
        if t_3(environment.getattr(l_1_profile, 'dscp')):
            pass
            yield '   qos dscp '
            yield str(environment.getattr(l_1_profile, 'dscp'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(l_1_profile, 'shape'), 'rate')):
            pass
            yield '   shape rate '
            yield str(environment.getattr(environment.getattr(l_1_profile, 'shape'), 'rate'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'service_policy'), 'type'), 'qos_input')):
            pass
            yield '   service-policy type qos input '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'service_policy'), 'type'), 'qos_input'))
            yield '\n'
        for l_2_tx_queue in t_2(environment.getattr(l_1_profile, 'tx_queues'), 'id'):
            _loop_vars = {}
            pass
            template = environment.get_template('eos/ethernet-interface-tx-queues.j2', 'eos/qos-profiles.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'tx_queue': l_2_tx_queue, 'pfc_command': l_1_pfc_command, 'profile': l_1_profile})):
                yield event
        l_2_tx_queue = missing
        for l_2_uc_tx_queue in t_2(environment.getattr(l_1_profile, 'uc_tx_queues'), 'id'):
            _loop_vars = {}
            pass
            template = environment.get_template('eos/ethernet-interface-uc-tx-queues.j2', 'eos/qos-profiles.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'uc_tx_queue': l_2_uc_tx_queue, 'pfc_command': l_1_pfc_command, 'profile': l_1_profile})):
                yield event
        l_2_uc_tx_queue = missing
        for l_2_mc_tx_queue in t_2(environment.getattr(l_1_profile, 'mc_tx_queues'), 'id'):
            _loop_vars = {}
            pass
            yield '   !\n   mc-tx-queue '
            yield str(environment.getattr(l_2_mc_tx_queue, 'id'))
            yield '\n'
            if t_3(environment.getattr(l_2_mc_tx_queue, 'comment')):
                pass
                for l_3_comment_line in t_1(context.call(environment.getattr(environment.getattr(l_2_mc_tx_queue, 'comment'), 'splitlines'), _loop_vars=_loop_vars), []):
                    _loop_vars = {}
                    pass
                    yield '      !! '
                    yield str(l_3_comment_line)
                    yield '\n'
                l_3_comment_line = missing
            if t_3(environment.getattr(l_2_mc_tx_queue, 'priority')):
                pass
                yield '      '
                yield str(environment.getattr(l_2_mc_tx_queue, 'priority'))
                yield '\n'
            if t_3(environment.getattr(l_2_mc_tx_queue, 'bandwidth_percent')):
                pass
                yield '      bandwidth percent '
                yield str(environment.getattr(l_2_mc_tx_queue, 'bandwidth_percent'))
                yield '\n'
            elif t_3(environment.getattr(l_2_mc_tx_queue, 'bandwidth_guaranteed_percent')):
                pass
                yield '      bandwidth guaranteed percent '
                yield str(environment.getattr(l_2_mc_tx_queue, 'bandwidth_guaranteed_percent'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_2_mc_tx_queue, 'shape'), 'rate')):
                pass
                yield '      shape rate '
                yield str(environment.getattr(environment.getattr(l_2_mc_tx_queue, 'shape'), 'rate'))
                yield '\n'
        l_2_mc_tx_queue = missing
        if t_3(environment.getattr(l_1_profile, 'priority_flow_control')):
            pass
            if t_3(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'enabled'), True):
                pass
                yield '   !\n   priority-flow-control on\n'
            elif t_3(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'enabled'), False):
                pass
                yield '   !\n   no priority-flow-control\n'
            for l_2_priority_block in t_2(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'priorities'), 'priority'):
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_2_priority_block, 'priority')):
                    pass
                    if t_3(environment.getattr(l_2_priority_block, 'no_drop'), True):
                        pass
                        yield '   priority-flow-control priority '
                        yield str(environment.getattr(l_2_priority_block, 'priority'))
                        yield ' no-drop\n'
                    elif t_3(environment.getattr(l_2_priority_block, 'no_drop'), False):
                        pass
                        yield '   priority-flow-control priority '
                        yield str(environment.getattr(l_2_priority_block, 'priority'))
                        yield ' drop\n'
            l_2_priority_block = missing
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'enabled'), True):
                pass
                yield '   priority-flow-control pause watchdog\n'
                if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'action')):
                    pass
                    yield '   priority-flow-control pause watchdog port action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'action'))
                    yield '\n'
                if t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'timer'), 'timeout')):
                    pass
                    l_1_pfc_command = 'priority-flow-control pause watchdog port timer'
                    _loop_vars['pfc_command'] = l_1_pfc_command
                    l_1_pfc_command = str_join(((undefined(name='pfc_command') if l_1_pfc_command is missing else l_1_pfc_command), ' timeout ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'timer'), 'timeout'), ))
                    _loop_vars['pfc_command'] = l_1_pfc_command
                    l_1_pfc_command = str_join(((undefined(name='pfc_command') if l_1_pfc_command is missing else l_1_pfc_command), ' polling-interval ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'timer'), 'polling_interval'), ))
                    _loop_vars['pfc_command'] = l_1_pfc_command
                    l_1_pfc_command = str_join(((undefined(name='pfc_command') if l_1_pfc_command is missing else l_1_pfc_command), ' recovery-time ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'timer'), 'recovery_time'), ))
                    _loop_vars['pfc_command'] = l_1_pfc_command
                    if t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'timer'), 'forced'), True):
                        pass
                        l_1_pfc_command = str_join(((undefined(name='pfc_command') if l_1_pfc_command is missing else l_1_pfc_command), ' forced', ))
                        _loop_vars['pfc_command'] = l_1_pfc_command
                yield '   '
                yield str((undefined(name='pfc_command') if l_1_pfc_command is missing else l_1_pfc_command))
                yield '\n'
    l_1_profile = l_1_pfc_command = missing

blocks = {}
debug_info = '7=30&9=35&10=37&11=39&14=45&17=47&18=50&20=52&21=55&23=57&24=60&26=62&27=65&29=67&30=70&32=74&33=77&35=81&37=85&38=87&39=89&40=93&43=96&44=99&46=101&47=104&48=106&49=109&51=111&52=114&55=117&56=119&59=122&63=125&64=128&65=130&66=133&67=135&68=138&72=141&74=144&75=147&77=149&78=151&79=153&80=155&81=157&82=159&83=161&86=164'