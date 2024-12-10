from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-igmp-snooping.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_igmp_snooping = resolve('ip_igmp_snooping')
    l_0_enabled = resolve('enabled')
    l_0_fast_leave = resolve('fast_leave')
    l_0_intf_res_qry = resolve('intf_res_qry')
    l_0_proxy = resolve('proxy')
    l_0_res_qry_int = resolve('res_qry_int')
    l_0_rv = resolve('rv')
    l_0_querier = resolve('querier')
    l_0_addr = resolve('addr')
    l_0_qry_int = resolve('qry_int')
    l_0_mx_resp_time = resolve('mx_resp_time')
    l_0_last_mem_qry_int = resolve('last_mem_qry_int')
    l_0_last_mem_qry_cnt = resolve('last_mem_qry_cnt')
    l_0_stu_qry_int = resolve('stu_qry_int')
    l_0_stu_qry_cnt = resolve('stu_qry_cnt')
    l_0_version = resolve('version')
    l_0_qr_settings_vlans = resolve('qr_settings_vlans')
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
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping)):
        pass
        yield '\n### IP IGMP Snooping\n\n#### IP IGMP Snooping Summary\n\n| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |\n| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |\n'
        if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'globally_enabled'), False):
            pass
            l_0_enabled = 'Disabled'
            context.vars['enabled'] = l_0_enabled
            context.exported_vars.add('enabled')
        else:
            pass
            l_0_enabled = 'Enabled'
            context.vars['enabled'] = l_0_enabled
            context.exported_vars.add('enabled')
        l_0_fast_leave = t_1(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'fast_leave'), '-')
        context.vars['fast_leave'] = l_0_fast_leave
        context.exported_vars.add('fast_leave')
        l_0_intf_res_qry = t_1(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'interface_restart_query'), '-')
        context.vars['intf_res_qry'] = l_0_intf_res_qry
        context.exported_vars.add('intf_res_qry')
        l_0_proxy = t_1(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'proxy'), '-')
        context.vars['proxy'] = l_0_proxy
        context.exported_vars.add('proxy')
        l_0_res_qry_int = t_1(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'restart_query_interval'), '-')
        context.vars['res_qry_int'] = l_0_res_qry_int
        context.exported_vars.add('res_qry_int')
        l_0_rv = t_1(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'robustness_variable'), '-')
        context.vars['rv'] = l_0_rv
        context.exported_vars.add('rv')
        yield '| '
        yield str((undefined(name='enabled') if l_0_enabled is missing else l_0_enabled))
        yield ' | '
        yield str((undefined(name='fast_leave') if l_0_fast_leave is missing else l_0_fast_leave))
        yield ' | '
        yield str((undefined(name='intf_res_qry') if l_0_intf_res_qry is missing else l_0_intf_res_qry))
        yield ' | '
        yield str((undefined(name='proxy') if l_0_proxy is missing else l_0_proxy))
        yield ' | '
        yield str((undefined(name='res_qry_int') if l_0_res_qry_int is missing else l_0_res_qry_int))
        yield ' | '
        yield str((undefined(name='rv') if l_0_rv is missing else l_0_rv))
        yield ' |\n'
        if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier')):
            pass
            yield '\n| Querier Enabled | IP Address | Query Interval | Max Response Time | Last Member Query Interval | Last Member Query Count | Startup Query Interval | Startup Query Count | Version |\n| --------------- | ---------- | -------------- | ----------------- | -------------------------- | ----------------------- | ---------------------- | ------------------- | ------- |\n'
            l_0_querier = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'enabled'), '-')
            context.vars['querier'] = l_0_querier
            context.exported_vars.add('querier')
            l_0_addr = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'address'), '-')
            context.vars['addr'] = l_0_addr
            context.exported_vars.add('addr')
            l_0_qry_int = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'query_interval'), '-')
            context.vars['qry_int'] = l_0_qry_int
            context.exported_vars.add('qry_int')
            l_0_mx_resp_time = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'max_response_time'), '-')
            context.vars['mx_resp_time'] = l_0_mx_resp_time
            context.exported_vars.add('mx_resp_time')
            l_0_last_mem_qry_int = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_interval'), '-')
            context.vars['last_mem_qry_int'] = l_0_last_mem_qry_int
            context.exported_vars.add('last_mem_qry_int')
            l_0_last_mem_qry_cnt = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_count'), '-')
            context.vars['last_mem_qry_cnt'] = l_0_last_mem_qry_cnt
            context.exported_vars.add('last_mem_qry_cnt')
            l_0_stu_qry_int = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_interval'), '-')
            context.vars['stu_qry_int'] = l_0_stu_qry_int
            context.exported_vars.add('stu_qry_int')
            l_0_stu_qry_cnt = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_count'), '-')
            context.vars['stu_qry_cnt'] = l_0_stu_qry_cnt
            context.exported_vars.add('stu_qry_cnt')
            l_0_version = t_1(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'version'), '-')
            context.vars['version'] = l_0_version
            context.exported_vars.add('version')
            yield '| '
            yield str((undefined(name='querier') if l_0_querier is missing else l_0_querier))
            yield ' | '
            yield str((undefined(name='addr') if l_0_addr is missing else l_0_addr))
            yield ' | '
            yield str((undefined(name='qry_int') if l_0_qry_int is missing else l_0_qry_int))
            yield ' | '
            yield str((undefined(name='mx_resp_time') if l_0_mx_resp_time is missing else l_0_mx_resp_time))
            yield ' | '
            yield str((undefined(name='last_mem_qry_int') if l_0_last_mem_qry_int is missing else l_0_last_mem_qry_int))
            yield ' | '
            yield str((undefined(name='last_mem_qry_cnt') if l_0_last_mem_qry_cnt is missing else l_0_last_mem_qry_cnt))
            yield ' | '
            yield str((undefined(name='stu_qry_int') if l_0_stu_qry_int is missing else l_0_stu_qry_int))
            yield ' | '
            yield str((undefined(name='stu_qry_cnt') if l_0_stu_qry_cnt is missing else l_0_stu_qry_cnt))
            yield ' | '
            yield str((undefined(name='version') if l_0_version is missing else l_0_version))
            yield ' |\n'
        if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'vlans')):
            pass
            l_0_qr_settings_vlans = []
            context.vars['qr_settings_vlans'] = l_0_qr_settings_vlans
            context.exported_vars.add('qr_settings_vlans')
            yield '\n##### IP IGMP Snooping Vlan Summary\n\n| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |\n| ---- | ------------- | ---------- | ---------- | ----- |\n'
            for l_1_vlan in t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'vlans'), 'id'):
                l_1_fast_leave = l_0_fast_leave
                l_1_proxy = l_0_proxy
                l_1_vlan_snooping = l_1_max_groups = missing
                _loop_vars = {}
                pass
                l_1_vlan_snooping = t_1(environment.getattr(l_1_vlan, 'enabled'), '-')
                _loop_vars['vlan_snooping'] = l_1_vlan_snooping
                l_1_fast_leave = t_1(environment.getattr(l_1_vlan, 'fast_leave'), '-')
                _loop_vars['fast_leave'] = l_1_fast_leave
                l_1_max_groups = t_1(environment.getattr(l_1_vlan, 'max_groups'), '-')
                _loop_vars['max_groups'] = l_1_max_groups
                l_1_proxy = t_1(environment.getattr(l_1_vlan, 'proxy'), '-')
                _loop_vars['proxy'] = l_1_proxy
                yield '| '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' | '
                yield str((undefined(name='vlan_snooping') if l_1_vlan_snooping is missing else l_1_vlan_snooping))
                yield ' | '
                yield str((undefined(name='fast_leave') if l_1_fast_leave is missing else l_1_fast_leave))
                yield ' | '
                yield str((undefined(name='max_groups') if l_1_max_groups is missing else l_1_max_groups))
                yield ' | '
                yield str((undefined(name='proxy') if l_1_proxy is missing else l_1_proxy))
                yield ' |\n'
                if t_4(environment.getattr(l_1_vlan, 'querier')):
                    pass
                    context.call(environment.getattr((undefined(name='qr_settings_vlans') if l_0_qr_settings_vlans is missing else l_0_qr_settings_vlans), 'append'), l_1_vlan, _loop_vars=_loop_vars)
            l_1_vlan = l_1_vlan_snooping = l_1_fast_leave = l_1_max_groups = l_1_proxy = missing
            if (t_3((undefined(name='qr_settings_vlans') if l_0_qr_settings_vlans is missing else l_0_qr_settings_vlans)) > 0):
                pass
                yield '\n| Vlan | Querier Enabled | IP Address | Query Interval | Max Response Time | Last Member Query Interval | Last Member Query Count | Startup Query Interval | Startup Query Count | Version |\n| ---- | --------------- | ---------- | -------------- | ----------------- | -------------------------- | ----------------------- | ---------------------- | ------------------- | ------- |\n'
                for l_1_vlan in (undefined(name='qr_settings_vlans') if l_0_qr_settings_vlans is missing else l_0_qr_settings_vlans):
                    l_1_querier = l_0_querier
                    l_1_addr = l_0_addr
                    l_1_qry_int = l_0_qry_int
                    l_1_mx_resp_time = l_0_mx_resp_time
                    l_1_last_mem_qry_int = l_0_last_mem_qry_int
                    l_1_last_mem_qry_cnt = l_0_last_mem_qry_cnt
                    l_1_stu_qry_int = l_0_stu_qry_int
                    l_1_stu_qry_cnt = l_0_stu_qry_cnt
                    l_1_version = l_0_version
                    _loop_vars = {}
                    pass
                    l_1_querier = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'enabled'), '-')
                    _loop_vars['querier'] = l_1_querier
                    l_1_addr = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'address'), '-')
                    _loop_vars['addr'] = l_1_addr
                    l_1_qry_int = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'query_interval'), '-')
                    _loop_vars['qry_int'] = l_1_qry_int
                    l_1_mx_resp_time = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'max_response_time'), '-')
                    _loop_vars['mx_resp_time'] = l_1_mx_resp_time
                    l_1_last_mem_qry_int = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_interval'), '-')
                    _loop_vars['last_mem_qry_int'] = l_1_last_mem_qry_int
                    l_1_last_mem_qry_cnt = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_count'), '-')
                    _loop_vars['last_mem_qry_cnt'] = l_1_last_mem_qry_cnt
                    l_1_stu_qry_int = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_interval'), '-')
                    _loop_vars['stu_qry_int'] = l_1_stu_qry_int
                    l_1_stu_qry_cnt = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_count'), '-')
                    _loop_vars['stu_qry_cnt'] = l_1_stu_qry_cnt
                    l_1_version = t_1(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'version'), '-')
                    _loop_vars['version'] = l_1_version
                    yield '| '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' | '
                    yield str((undefined(name='querier') if l_1_querier is missing else l_1_querier))
                    yield ' | '
                    yield str((undefined(name='addr') if l_1_addr is missing else l_1_addr))
                    yield ' | '
                    yield str((undefined(name='qry_int') if l_1_qry_int is missing else l_1_qry_int))
                    yield ' | '
                    yield str((undefined(name='mx_resp_time') if l_1_mx_resp_time is missing else l_1_mx_resp_time))
                    yield ' | '
                    yield str((undefined(name='last_mem_qry_int') if l_1_last_mem_qry_int is missing else l_1_last_mem_qry_int))
                    yield ' | '
                    yield str((undefined(name='last_mem_qry_cnt') if l_1_last_mem_qry_cnt is missing else l_1_last_mem_qry_cnt))
                    yield ' | '
                    yield str((undefined(name='stu_qry_int') if l_1_stu_qry_int is missing else l_1_stu_qry_int))
                    yield ' | '
                    yield str((undefined(name='stu_qry_cnt') if l_1_stu_qry_cnt is missing else l_1_stu_qry_cnt))
                    yield ' | '
                    yield str((undefined(name='version') if l_1_version is missing else l_1_version))
                    yield ' |\n'
                l_1_vlan = l_1_querier = l_1_addr = l_1_qry_int = l_1_mx_resp_time = l_1_last_mem_qry_int = l_1_last_mem_qry_cnt = l_1_stu_qry_int = l_1_stu_qry_cnt = l_1_version = missing
        yield '\n#### IP IGMP Snooping Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-igmp-snooping.j2', 'documentation/ip-igmp-snooping.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'addr': l_0_addr, 'enabled': l_0_enabled, 'fast_leave': l_0_fast_leave, 'intf_res_qry': l_0_intf_res_qry, 'last_mem_qry_cnt': l_0_last_mem_qry_cnt, 'last_mem_qry_int': l_0_last_mem_qry_int, 'mx_resp_time': l_0_mx_resp_time, 'proxy': l_0_proxy, 'qr_settings_vlans': l_0_qr_settings_vlans, 'qry_int': l_0_qry_int, 'querier': l_0_querier, 'res_qry_int': l_0_res_qry_int, 'rv': l_0_rv, 'stu_qry_cnt': l_0_stu_qry_cnt, 'stu_qry_int': l_0_stu_qry_int, 'version': l_0_version})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=52&15=55&16=57&18=62&20=65&21=68&22=71&23=74&24=77&25=81&26=93&30=96&31=99&32=102&33=105&34=108&35=111&36=114&37=117&38=120&39=124&41=142&42=144&48=148&49=154&50=156&51=158&52=160&53=163&54=173&55=175&58=177&62=180&63=192&64=194&65=196&66=198&67=200&68=202&69=204&70=206&71=208&72=211&80=233'