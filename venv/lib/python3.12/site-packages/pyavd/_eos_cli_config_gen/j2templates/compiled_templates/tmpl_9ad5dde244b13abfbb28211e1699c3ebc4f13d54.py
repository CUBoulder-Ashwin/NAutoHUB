from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/qos-profiles.j2'

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
        t_3 = environment.filters['replace']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'replace' found.")
    try:
        t_4 = environment.filters['trim']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'trim' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='qos_profiles') if l_0_qos_profiles is missing else l_0_qos_profiles)):
        pass
        yield '\n### QOS Profiles\n\n#### QOS Profiles Summary\n'
        for l_1_profile in t_2((undefined(name='qos_profiles') if l_0_qos_profiles is missing else l_0_qos_profiles), 'name'):
            l_1_namespace = resolve('namespace')
            l_1_enabled = resolve('enabled')
            l_1_action = resolve('action')
            l_1_timeout = resolve('timeout')
            l_1_recovery = resolve('recovery')
            l_1_polling = resolve('polling')
            l_1_cos = l_1_dscp = l_1_trust = l_1_shape_rate = l_1_qos_sp = l_1_ns = missing
            _loop_vars = {}
            pass
            yield '\n##### QOS Profile: **'
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '**\n\n###### Settings\n\n| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |\n| ----------- | ------------ | ----- | ---------- | ------------------ |\n'
            l_1_cos = t_1(environment.getattr(l_1_profile, 'cos'), '-')
            _loop_vars['cos'] = l_1_cos
            l_1_dscp = t_1(environment.getattr(l_1_profile, 'dscp'), '-')
            _loop_vars['dscp'] = l_1_dscp
            l_1_trust = t_1(environment.getattr(l_1_profile, 'trust'), '-')
            _loop_vars['trust'] = l_1_trust
            l_1_shape_rate = t_1(environment.getattr(environment.getattr(l_1_profile, 'shape'), 'rate'), '-')
            _loop_vars['shape_rate'] = l_1_shape_rate
            l_1_qos_sp = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'service_policy'), 'type'), 'qos_input'), '-')
            _loop_vars['qos_sp'] = l_1_qos_sp
            yield '| '
            yield str((undefined(name='cos') if l_1_cos is missing else l_1_cos))
            yield ' | '
            yield str((undefined(name='dscp') if l_1_dscp is missing else l_1_dscp))
            yield ' | '
            yield str((undefined(name='trust') if l_1_trust is missing else l_1_trust))
            yield ' | '
            yield str((undefined(name='shape_rate') if l_1_shape_rate is missing else l_1_shape_rate))
            yield ' | '
            yield str((undefined(name='qos_sp') if l_1_qos_sp is missing else l_1_qos_sp))
            yield ' |\n'
            if ((t_5(environment.getattr(l_1_profile, 'tx_queues')) or t_5(environment.getattr(l_1_profile, 'uc_tx_queues'))) or t_5(environment.getattr(l_1_profile, 'mc_tx_queues'))):
                pass
                yield '\n###### TX Queues\n\n| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |\n| -------- | ---- | --------- | -------- | ---------- | ------- |\n'
                if t_5(environment.getattr(l_1_profile, 'tx_queues')):
                    pass
                    for l_2_tx_queue in t_2(environment.getattr(l_1_profile, 'tx_queues'), 'id'):
                        l_2_shape_rate = l_1_shape_rate
                        l_2_type = l_2_bw_percent = l_2_priority = l_2_comment = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'All'
                        _loop_vars['type'] = l_2_type
                        l_2_bw_percent = t_1(environment.getattr(l_2_tx_queue, 'bandwidth_percent'), environment.getattr(l_2_tx_queue, 'bandwidth_guaranteed_percent'), '-')
                        _loop_vars['bw_percent'] = l_2_bw_percent
                        l_2_priority = t_1(environment.getattr(l_2_tx_queue, 'priority'), '-')
                        _loop_vars['priority'] = l_2_priority
                        l_2_shape_rate = t_1(environment.getattr(environment.getattr(l_2_tx_queue, 'shape'), 'rate'), '-')
                        _loop_vars['shape_rate'] = l_2_shape_rate
                        l_2_comment = t_3(context.eval_ctx, t_4(t_1(environment.getattr(l_2_tx_queue, 'comment'), '-')), '\n', '<br>')
                        _loop_vars['comment'] = l_2_comment
                        yield '| '
                        yield str(environment.getattr(l_2_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | '
                        yield str((undefined(name='bw_percent') if l_2_bw_percent is missing else l_2_bw_percent))
                        yield ' | '
                        yield str((undefined(name='priority') if l_2_priority is missing else l_2_priority))
                        yield ' | '
                        yield str((undefined(name='shape_rate') if l_2_shape_rate is missing else l_2_shape_rate))
                        yield ' | '
                        yield str((undefined(name='comment') if l_2_comment is missing else l_2_comment))
                        yield ' |\n'
                    l_2_tx_queue = l_2_type = l_2_bw_percent = l_2_priority = l_2_shape_rate = l_2_comment = missing
                if t_5(environment.getattr(l_1_profile, 'uc_tx_queues')):
                    pass
                    for l_2_uc_tx_queue in t_2(environment.getattr(l_1_profile, 'uc_tx_queues'), 'id'):
                        l_2_shape_rate = l_1_shape_rate
                        l_2_type = l_2_bw_percent = l_2_priority = l_2_comment = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'Unicast'
                        _loop_vars['type'] = l_2_type
                        l_2_bw_percent = t_1(environment.getattr(l_2_uc_tx_queue, 'bandwidth_percent'), environment.getattr(l_2_uc_tx_queue, 'bandwidth_guaranteed_percent'), '-')
                        _loop_vars['bw_percent'] = l_2_bw_percent
                        l_2_priority = t_1(environment.getattr(l_2_uc_tx_queue, 'priority'), '-')
                        _loop_vars['priority'] = l_2_priority
                        l_2_shape_rate = t_1(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'shape'), 'rate'), '-')
                        _loop_vars['shape_rate'] = l_2_shape_rate
                        l_2_comment = t_3(context.eval_ctx, t_4(t_1(environment.getattr(l_2_uc_tx_queue, 'comment'), '-')), '\n', '<br>')
                        _loop_vars['comment'] = l_2_comment
                        yield '| '
                        yield str(environment.getattr(l_2_uc_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | '
                        yield str((undefined(name='bw_percent') if l_2_bw_percent is missing else l_2_bw_percent))
                        yield ' | '
                        yield str((undefined(name='priority') if l_2_priority is missing else l_2_priority))
                        yield ' | '
                        yield str((undefined(name='shape_rate') if l_2_shape_rate is missing else l_2_shape_rate))
                        yield ' | '
                        yield str((undefined(name='comment') if l_2_comment is missing else l_2_comment))
                        yield ' |\n'
                    l_2_uc_tx_queue = l_2_type = l_2_bw_percent = l_2_priority = l_2_shape_rate = l_2_comment = missing
                if t_5(environment.getattr(l_1_profile, 'mc_tx_queues')):
                    pass
                    for l_2_mc_tx_queue in t_2(environment.getattr(l_1_profile, 'mc_tx_queues'), 'id'):
                        l_2_shape_rate = l_1_shape_rate
                        l_2_type = l_2_bw_percent = l_2_priority = l_2_comment = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'Multicast'
                        _loop_vars['type'] = l_2_type
                        l_2_bw_percent = t_1(environment.getattr(l_2_mc_tx_queue, 'bandwidth_percent'), environment.getattr(l_2_mc_tx_queue, 'bandwidth_guaranteed_percent'), '-')
                        _loop_vars['bw_percent'] = l_2_bw_percent
                        l_2_priority = t_1(environment.getattr(l_2_mc_tx_queue, 'priority'), '-')
                        _loop_vars['priority'] = l_2_priority
                        l_2_shape_rate = t_1(environment.getattr(environment.getattr(l_2_mc_tx_queue, 'shape'), 'rate'), '-')
                        _loop_vars['shape_rate'] = l_2_shape_rate
                        l_2_comment = t_3(context.eval_ctx, t_4(t_1(environment.getattr(l_2_mc_tx_queue, 'comment'), '-')), '\n', '<br>')
                        _loop_vars['comment'] = l_2_comment
                        yield '| '
                        yield str(environment.getattr(l_2_mc_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | '
                        yield str((undefined(name='bw_percent') if l_2_bw_percent is missing else l_2_bw_percent))
                        yield ' | '
                        yield str((undefined(name='priority') if l_2_priority is missing else l_2_priority))
                        yield ' | '
                        yield str((undefined(name='shape_rate') if l_2_shape_rate is missing else l_2_shape_rate))
                        yield ' | '
                        yield str((undefined(name='comment') if l_2_comment is missing else l_2_comment))
                        yield ' |\n'
                    l_2_mc_tx_queue = l_2_type = l_2_bw_percent = l_2_priority = l_2_shape_rate = l_2_comment = missing
            l_1_ns = context.call((undefined(name='namespace') if l_1_namespace is missing else l_1_namespace), ecn_table=False, _loop_vars=_loop_vars)
            _loop_vars['ns'] = l_1_ns
            for l_2_tx_queue in t_1(environment.getattr(l_1_profile, 'tx_queues'), []):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'units')):
                    pass
                    if not isinstance(l_1_ns, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_ns['ecn_table'] = True
            l_2_tx_queue = missing
            for l_2_tx_queue in t_1(environment.getattr(l_1_profile, 'uc_tx_queues'), []):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'units')):
                    pass
                    if not isinstance(l_1_ns, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_ns['ecn_table'] = True
            l_2_tx_queue = missing
            if environment.getattr((undefined(name='ns') if l_1_ns is missing else l_1_ns), 'ecn_table'):
                pass
                yield '\n###### ECN Configuration\n\n| TX queue | Type | Min Threshold | Max Threshold | Max Mark Probability |\n| -------- | ---- | ------------- | ------------- | -------------------- |\n'
                if t_5(environment.getattr(l_1_profile, 'tx_queues')):
                    pass
                    for l_2_tx_queue in t_2(environment.getattr(l_1_profile, 'tx_queues'), 'id'):
                        l_2_type = l_2_min = l_2_max = l_2_prob = l_2_units = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'All'
                        _loop_vars['type'] = l_2_type
                        l_2_min = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'min'), '-')
                        _loop_vars['min'] = l_2_min
                        l_2_max = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'max'), '-')
                        _loop_vars['max'] = l_2_max
                        l_2_prob = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'max_probability'), '-')
                        _loop_vars['prob'] = l_2_prob
                        l_2_units = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'units'), '')
                        _loop_vars['units'] = l_2_units
                        yield '| '
                        yield str(environment.getattr(l_2_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | '
                        yield str((undefined(name='min') if l_2_min is missing else l_2_min))
                        yield ' '
                        yield str((undefined(name='units') if l_2_units is missing else l_2_units))
                        yield ' | '
                        yield str((undefined(name='max') if l_2_max is missing else l_2_max))
                        yield ' '
                        yield str((undefined(name='units') if l_2_units is missing else l_2_units))
                        yield ' | '
                        yield str((undefined(name='prob') if l_2_prob is missing else l_2_prob))
                        yield ' |\n'
                    l_2_tx_queue = l_2_type = l_2_min = l_2_max = l_2_prob = l_2_units = missing
                if t_5(environment.getattr(l_1_profile, 'uc_tx_queues')):
                    pass
                    for l_2_uc_tx_queue in t_2(environment.getattr(l_1_profile, 'uc_tx_queues'), 'id'):
                        l_2_type = l_2_min = l_2_max = l_2_prob = l_2_units = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'Unicast'
                        _loop_vars['type'] = l_2_type
                        l_2_min = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'min'), '-')
                        _loop_vars['min'] = l_2_min
                        l_2_max = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'max'), '-')
                        _loop_vars['max'] = l_2_max
                        l_2_prob = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'max_probability'), '-')
                        _loop_vars['prob'] = l_2_prob
                        l_2_units = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'ecn'), 'threshold'), 'units'), '')
                        _loop_vars['units'] = l_2_units
                        yield '| '
                        yield str(environment.getattr(l_2_uc_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | '
                        yield str((undefined(name='min') if l_2_min is missing else l_2_min))
                        yield ' '
                        yield str((undefined(name='units') if l_2_units is missing else l_2_units))
                        yield ' | '
                        yield str((undefined(name='max') if l_2_max is missing else l_2_max))
                        yield ' '
                        yield str((undefined(name='units') if l_2_units is missing else l_2_units))
                        yield ' | '
                        yield str((undefined(name='prob') if l_2_prob is missing else l_2_prob))
                        yield ' |\n'
                    l_2_uc_tx_queue = l_2_type = l_2_min = l_2_max = l_2_prob = l_2_units = missing
                if t_5(environment.getattr(l_1_profile, 'mc_tx_queues')):
                    pass
                    for l_2_mc_tx_queue in t_2(environment.getattr(l_1_profile, 'mc_tx_queues'), 'id'):
                        l_2_type = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'Multicast'
                        _loop_vars['type'] = l_2_type
                        yield '| '
                        yield str(environment.getattr(l_2_mc_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | - | - | - |\n'
                    l_2_mc_tx_queue = l_2_type = missing
            l_1_ns = context.call((undefined(name='namespace') if l_1_namespace is missing else l_1_namespace), wred_table=False, _loop_vars=_loop_vars)
            _loop_vars['ns'] = l_1_ns
            for l_2_tx_queue in t_1(environment.getattr(l_1_profile, 'tx_queues'), []):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'units')):
                    pass
                    if not isinstance(l_1_ns, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_ns['wred_table'] = True
            l_2_tx_queue = missing
            for l_2_tx_queue in t_1(environment.getattr(l_1_profile, 'uc_tx_queues'), []):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'units')):
                    pass
                    if not isinstance(l_1_ns, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_ns['wred_table'] = True
            l_2_tx_queue = missing
            if environment.getattr((undefined(name='ns') if l_1_ns is missing else l_1_ns), 'wred_table'):
                pass
                yield '\n###### WRED Configuration\n\n| TX queue | Type | Drop Precedence | Min Threshold | Max Threshold | Drop Probability | Weight |\n| -------- | ---- | --------------- | ------------- | ------------- | ---------------- | ------ |\n'
                if t_5(environment.getattr(l_1_profile, 'tx_queues')):
                    pass
                    for l_2_tx_queue in t_2(environment.getattr(l_1_profile, 'tx_queues'), 'id'):
                        l_2_type = l_2_precedence = l_2_min = l_2_max = l_2_prob = l_2_weight = l_2_units = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'All'
                        _loop_vars['type'] = l_2_type
                        l_2_precedence = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'drop_precedence'), '-')
                        _loop_vars['precedence'] = l_2_precedence
                        l_2_min = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'min'), '-')
                        _loop_vars['min'] = l_2_min
                        l_2_max = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'max'), '-')
                        _loop_vars['max'] = l_2_max
                        l_2_prob = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'drop_probability'), '-')
                        _loop_vars['prob'] = l_2_prob
                        l_2_weight = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'weight'), '-')
                        _loop_vars['weight'] = l_2_weight
                        l_2_units = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'units'), '')
                        _loop_vars['units'] = l_2_units
                        yield '| '
                        yield str(environment.getattr(l_2_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | '
                        yield str((undefined(name='precedence') if l_2_precedence is missing else l_2_precedence))
                        yield ' | '
                        yield str((undefined(name='min') if l_2_min is missing else l_2_min))
                        yield ' '
                        yield str((undefined(name='units') if l_2_units is missing else l_2_units))
                        yield ' | '
                        yield str((undefined(name='max') if l_2_max is missing else l_2_max))
                        yield ' '
                        yield str((undefined(name='units') if l_2_units is missing else l_2_units))
                        yield ' | '
                        yield str((undefined(name='prob') if l_2_prob is missing else l_2_prob))
                        yield ' | '
                        yield str((undefined(name='weight') if l_2_weight is missing else l_2_weight))
                        yield ' |\n'
                    l_2_tx_queue = l_2_type = l_2_precedence = l_2_min = l_2_max = l_2_prob = l_2_weight = l_2_units = missing
                if t_5(environment.getattr(l_1_profile, 'uc_tx_queues')):
                    pass
                    for l_2_uc_tx_queue in t_2(environment.getattr(l_1_profile, 'uc_tx_queues'), 'id'):
                        l_2_type = l_2_precedence = l_2_min = l_2_max = l_2_prob = l_2_weight = l_2_units = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'Unicast'
                        _loop_vars['type'] = l_2_type
                        l_2_precedence = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'drop_precedence'), '-')
                        _loop_vars['precedence'] = l_2_precedence
                        l_2_min = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'min'), '-')
                        _loop_vars['min'] = l_2_min
                        l_2_max = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'max'), '-')
                        _loop_vars['max'] = l_2_max
                        l_2_prob = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'drop_probability'), '-')
                        _loop_vars['prob'] = l_2_prob
                        l_2_weight = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'weight'), '-')
                        _loop_vars['weight'] = l_2_weight
                        l_2_units = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_2_uc_tx_queue, 'random_detect'), 'drop'), 'threshold'), 'units'), '')
                        _loop_vars['units'] = l_2_units
                        yield '| '
                        yield str(environment.getattr(l_2_uc_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | '
                        yield str((undefined(name='precedence') if l_2_precedence is missing else l_2_precedence))
                        yield ' |'
                        yield str((undefined(name='min') if l_2_min is missing else l_2_min))
                        yield ' '
                        yield str((undefined(name='units') if l_2_units is missing else l_2_units))
                        yield ' | '
                        yield str((undefined(name='max') if l_2_max is missing else l_2_max))
                        yield ' '
                        yield str((undefined(name='units') if l_2_units is missing else l_2_units))
                        yield ' | '
                        yield str((undefined(name='prob') if l_2_prob is missing else l_2_prob))
                        yield ' | '
                        yield str((undefined(name='weight') if l_2_weight is missing else l_2_weight))
                        yield ' |\n'
                    l_2_uc_tx_queue = l_2_type = l_2_precedence = l_2_min = l_2_max = l_2_prob = l_2_weight = l_2_units = missing
                if t_5(environment.getattr(l_1_profile, 'mc_tx_queues')):
                    pass
                    for l_2_mc_tx_queue in t_2(environment.getattr(l_1_profile, 'mc_tx_queues'), 'id'):
                        l_2_type = missing
                        _loop_vars = {}
                        pass
                        l_2_type = 'Multicast'
                        _loop_vars['type'] = l_2_type
                        yield '| '
                        yield str(environment.getattr(l_2_mc_tx_queue, 'id'))
                        yield ' | '
                        yield str((undefined(name='type') if l_2_type is missing else l_2_type))
                        yield ' | - | - | - | - | - |\n'
                    l_2_mc_tx_queue = l_2_type = missing
            if t_5(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'enabled'), True):
                pass
                yield '\n###### Priority Flow Control\n\nPriority Flow Control is **enabled**.\n\n| Priority | Action |\n| -------- | ------ |\n'
                for l_2_priority_block in t_2(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'priorities'), 'priority'):
                    l_2_action = l_1_action
                    _loop_vars = {}
                    pass
                    if t_5(environment.getattr(l_2_priority_block, 'priority')):
                        pass
                        if t_5(environment.getattr(l_2_priority_block, 'no_drop'), True):
                            pass
                            l_2_action = 'no-drop'
                            _loop_vars['action'] = l_2_action
                        else:
                            pass
                            l_2_action = 'drop'
                            _loop_vars['action'] = l_2_action
                        yield '| '
                        yield str(environment.getattr(l_2_priority_block, 'priority'))
                        yield ' | '
                        yield str((undefined(name='action') if l_2_action is missing else l_2_action))
                        yield ' |\n'
                l_2_priority_block = l_2_action = missing
                if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'enabled'), True):
                    pass
                    l_1_enabled = environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'enabled')
                    _loop_vars['enabled'] = l_1_enabled
                    l_1_action = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'action'), 'errdisable')
                    _loop_vars['action'] = l_1_action
                    l_1_timeout = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'timer'), 'timeout'), '-')
                    _loop_vars['timeout'] = l_1_timeout
                    l_1_recovery = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'timer'), 'recovery_time'), '-')
                    _loop_vars['recovery'] = l_1_recovery
                    l_1_polling = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'priority_flow_control'), 'watchdog'), 'timer'), 'polling_interval'), '-')
                    _loop_vars['polling'] = l_1_polling
                    yield '\n###### Priority Flow Control Watchdog Settings\n\n| Enabled | Action | Timeout | Recovery | Polling |\n| ------- | ------ | ------- | -------- | ------- |\n| '
                    yield str((undefined(name='enabled') if l_1_enabled is missing else l_1_enabled))
                    yield ' | '
                    yield str((undefined(name='action') if l_1_action is missing else l_1_action))
                    yield ' | '
                    yield str((undefined(name='timeout') if l_1_timeout is missing else l_1_timeout))
                    yield ' | '
                    yield str((undefined(name='recovery') if l_1_recovery is missing else l_1_recovery))
                    yield ' | '
                    yield str((undefined(name='polling') if l_1_polling is missing else l_1_polling))
                    yield ' |\n'
        l_1_profile = l_1_cos = l_1_dscp = l_1_trust = l_1_shape_rate = l_1_qos_sp = l_1_namespace = l_1_ns = l_1_enabled = l_1_action = l_1_timeout = l_1_recovery = l_1_polling = missing
        yield '\n#### QOS Profile Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/qos-profiles.j2', 'documentation/qos-profiles.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=42&12=45&14=56&20=58&21=60&22=62&23=64&24=66&25=69&26=79&34=82&35=84&36=89&37=91&40=93&41=95&42=97&43=100&46=113&47=115&48=120&49=122&52=124&53=126&54=128&55=131&58=144&59=146&60=151&61=153&64=155&65=157&66=159&67=162&71=175&72=177&73=180&74=182&77=186&78=189&79=191&82=195&88=198&89=200&90=204&91=206&92=208&93=210&94=212&95=215&98=230&99=232&100=236&101=238&102=240&103=242&104=244&105=247&108=262&109=264&110=268&111=271&115=276&116=278&117=281&118=283&121=287&122=290&123=292&126=296&132=299&133=301&134=305&135=307&136=309&137=311&138=313&139=315&140=317&141=320&144=339&145=341&146=345&147=347&148=349&149=351&150=353&151=355&152=357&153=360&156=379&157=381&158=385&159=388&163=393&171=396&172=400&173=402&174=404&176=408&178=411&181=416&182=418&183=420&184=422&185=424&186=426&192=429&200=441'