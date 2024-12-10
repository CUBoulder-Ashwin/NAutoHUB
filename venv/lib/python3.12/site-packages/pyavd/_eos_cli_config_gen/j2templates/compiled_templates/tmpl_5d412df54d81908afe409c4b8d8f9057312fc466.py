from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/system.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_system = resolve('system')
    l_0_cp_mss_cli = resolve('cp_mss_cli')
    l_0_with_vrf_non_default = resolve('with_vrf_non_default')
    l_0_without_vrf = resolve('without_vrf')
    l_0_with_vrf_default = resolve('with_vrf_default')
    l_0_sorted_ipv4_access_groups = resolve('sorted_ipv4_access_groups')
    l_0_sorted_ipv6_access_groups = resolve('sorted_ipv6_access_groups')
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
        t_3 = environment.filters['list']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'list' found.")
    try:
        t_4 = environment.filters['rejectattr']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'rejectattr' found.")
    try:
        t_5 = environment.filters['selectattr']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'selectattr' found.")
    try:
        t_6 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_6(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane')):
        pass
        yield '!\nsystem control-plane\n'
        if (t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv4')) or t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv6'))):
            pass
            l_0_cp_mss_cli = 'tcp mss ceiling'
            context.vars['cp_mss_cli'] = l_0_cp_mss_cli
            context.exported_vars.add('cp_mss_cli')
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv4')):
                pass
                l_0_cp_mss_cli = str_join(((undefined(name='cp_mss_cli') if l_0_cp_mss_cli is missing else l_0_cp_mss_cli), ' ipv4 ', environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv4'), ))
                context.vars['cp_mss_cli'] = l_0_cp_mss_cli
                context.exported_vars.add('cp_mss_cli')
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv6')):
                pass
                l_0_cp_mss_cli = str_join(((undefined(name='cp_mss_cli') if l_0_cp_mss_cli is missing else l_0_cp_mss_cli), ' ipv6 ', environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv6'), ))
                context.vars['cp_mss_cli'] = l_0_cp_mss_cli
                context.exported_vars.add('cp_mss_cli')
            yield '   '
            yield str((undefined(name='cp_mss_cli') if l_0_cp_mss_cli is missing else l_0_cp_mss_cli))
            yield '\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv4_access_group_ingress_default')):
            pass
            yield '   ip access-group ingress default '
            yield str(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv4_access_group_ingress_default'))
            yield '\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv4_access_groups')):
            pass
            l_0_with_vrf_non_default = t_2(t_2(t_4(context, t_5(context, environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv4_access_groups'), 'vrf', 'arista.avd.defined'), 'vrf', 'equalto', 'default')), 'vrf')
            context.vars['with_vrf_non_default'] = l_0_with_vrf_non_default
            context.exported_vars.add('with_vrf_non_default')
            l_0_without_vrf = t_2(t_4(context, environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv4_access_groups'), 'vrf', 'arista.avd.defined'))
            context.vars['without_vrf'] = l_0_without_vrf
            context.exported_vars.add('without_vrf')
            l_0_with_vrf_default = t_2(t_5(context, t_5(context, environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv4_access_groups'), 'vrf', 'arista.avd.defined'), 'vrf', 'equalto', 'default'))
            context.vars['with_vrf_default'] = l_0_with_vrf_default
            context.exported_vars.add('with_vrf_default')
            l_0_sorted_ipv4_access_groups = ((t_3(context.eval_ctx, (undefined(name='without_vrf') if l_0_without_vrf is missing else l_0_without_vrf)) + t_3(context.eval_ctx, (undefined(name='with_vrf_default') if l_0_with_vrf_default is missing else l_0_with_vrf_default))) + t_3(context.eval_ctx, (undefined(name='with_vrf_non_default') if l_0_with_vrf_non_default is missing else l_0_with_vrf_non_default)))
            context.vars['sorted_ipv4_access_groups'] = l_0_sorted_ipv4_access_groups
            context.exported_vars.add('sorted_ipv4_access_groups')
        for l_1_acl_set in t_1((undefined(name='sorted_ipv4_access_groups') if l_0_sorted_ipv4_access_groups is missing else l_0_sorted_ipv4_access_groups), []):
            l_1_cp_ipv4_access_grp = missing
            _loop_vars = {}
            pass
            l_1_cp_ipv4_access_grp = str_join(('ip access-group ', environment.getattr(l_1_acl_set, 'acl_name'), ))
            _loop_vars['cp_ipv4_access_grp'] = l_1_cp_ipv4_access_grp
            if t_6(environment.getattr(l_1_acl_set, 'vrf')):
                pass
                l_1_cp_ipv4_access_grp = str_join(((undefined(name='cp_ipv4_access_grp') if l_1_cp_ipv4_access_grp is missing else l_1_cp_ipv4_access_grp), ' vrf ', environment.getattr(l_1_acl_set, 'vrf'), ))
                _loop_vars['cp_ipv4_access_grp'] = l_1_cp_ipv4_access_grp
            l_1_cp_ipv4_access_grp = str_join(((undefined(name='cp_ipv4_access_grp') if l_1_cp_ipv4_access_grp is missing else l_1_cp_ipv4_access_grp), ' in', ))
            _loop_vars['cp_ipv4_access_grp'] = l_1_cp_ipv4_access_grp
            yield '   '
            yield str((undefined(name='cp_ipv4_access_grp') if l_1_cp_ipv4_access_grp is missing else l_1_cp_ipv4_access_grp))
            yield '\n'
        l_1_acl_set = l_1_cp_ipv4_access_grp = missing
        if t_6(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv6_access_group_ingress_default')):
            pass
            yield '   ipv6 access-group ingress default '
            yield str(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv6_access_group_ingress_default'))
            yield '\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv6_access_groups')):
            pass
            l_0_with_vrf_non_default = t_2(t_2(t_4(context, t_5(context, environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv6_access_groups'), 'vrf', 'arista.avd.defined'), 'vrf', 'equalto', 'default')), 'vrf')
            context.vars['with_vrf_non_default'] = l_0_with_vrf_non_default
            context.exported_vars.add('with_vrf_non_default')
            l_0_without_vrf = t_2(t_4(context, environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv6_access_groups'), 'vrf', 'arista.avd.defined'))
            context.vars['without_vrf'] = l_0_without_vrf
            context.exported_vars.add('without_vrf')
            l_0_with_vrf_default = t_2(t_5(context, t_5(context, environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv6_access_groups'), 'vrf', 'arista.avd.defined'), 'vrf', 'equalto', 'default'))
            context.vars['with_vrf_default'] = l_0_with_vrf_default
            context.exported_vars.add('with_vrf_default')
            l_0_sorted_ipv6_access_groups = ((t_3(context.eval_ctx, (undefined(name='without_vrf') if l_0_without_vrf is missing else l_0_without_vrf)) + t_3(context.eval_ctx, (undefined(name='with_vrf_default') if l_0_with_vrf_default is missing else l_0_with_vrf_default))) + t_3(context.eval_ctx, (undefined(name='with_vrf_non_default') if l_0_with_vrf_non_default is missing else l_0_with_vrf_non_default)))
            context.vars['sorted_ipv6_access_groups'] = l_0_sorted_ipv6_access_groups
            context.exported_vars.add('sorted_ipv6_access_groups')
        for l_1_acl_set in t_1((undefined(name='sorted_ipv6_access_groups') if l_0_sorted_ipv6_access_groups is missing else l_0_sorted_ipv6_access_groups), []):
            l_1_cp_ipv6_access_grp = missing
            _loop_vars = {}
            pass
            l_1_cp_ipv6_access_grp = str_join(('ipv6 access-group ', environment.getattr(l_1_acl_set, 'acl_name'), ))
            _loop_vars['cp_ipv6_access_grp'] = l_1_cp_ipv6_access_grp
            if t_6(environment.getattr(l_1_acl_set, 'vrf')):
                pass
                l_1_cp_ipv6_access_grp = str_join(((undefined(name='cp_ipv6_access_grp') if l_1_cp_ipv6_access_grp is missing else l_1_cp_ipv6_access_grp), ' vrf ', environment.getattr(l_1_acl_set, 'vrf'), ))
                _loop_vars['cp_ipv6_access_grp'] = l_1_cp_ipv6_access_grp
            l_1_cp_ipv6_access_grp = str_join(((undefined(name='cp_ipv6_access_grp') if l_1_cp_ipv6_access_grp is missing else l_1_cp_ipv6_access_grp), ' in', ))
            _loop_vars['cp_ipv6_access_grp'] = l_1_cp_ipv6_access_grp
            yield '   '
            yield str((undefined(name='cp_ipv6_access_grp') if l_1_cp_ipv6_access_grp is missing else l_1_cp_ipv6_access_grp))
            yield '\n'
        l_1_acl_set = l_1_cp_ipv6_access_grp = missing

blocks = {}
debug_info = '7=54&11=57&12=59&13=62&14=64&16=67&17=69&19=73&22=75&23=78&25=80&26=82&27=85&28=88&29=91&31=94&32=98&33=100&34=102&36=104&37=107&40=110&41=113&43=115&44=117&45=120&46=123&47=126&49=129&50=133&51=135&52=137&54=139&55=142'