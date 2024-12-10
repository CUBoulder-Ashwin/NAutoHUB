from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_security = resolve('ip_security')
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
    if t_3((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security)):
        pass
        yield '\n## IP Security\n'
        if t_3(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'hardware_encryption_disabled'), True):
            pass
            yield '\n- Hardware encryption is disabled\n'
        if t_3(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'ike_policies')):
            pass
            yield '\n### IKE policies\n\n| Policy name | IKE lifetime | Encryption | DH group | Local ID | Integrity |\n| ----------- | ------------ | ---------- | -------- | -------- | --------- |\n'
            for l_1_ike_policy in t_2(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'ike_policies'), 'name'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_ike_policy, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ike_policy, 'ike_lifetime'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ike_policy, 'encryption'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ike_policy, 'dh_group'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ike_policy, 'local_id_fqdn'), environment.getattr(l_1_ike_policy, 'local_id'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ike_policy, 'integrity'), '-'))
                yield ' |\n'
            l_1_ike_policy = missing
        if t_3(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'sa_policies')):
            pass
            yield '\n### Security Association policies\n\n| Policy name | ESP Integrity | ESP Encryption | Lifetime | PFS DH Group |\n| ----------- | ------------- | -------------- | -------- | ------------ |\n'
            for l_1_sa_policy in t_2(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'sa_policies'), 'name'):
                l_1_lifetime = resolve('lifetime')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(environment.getattr(l_1_sa_policy, 'sa_lifetime'), 'value')):
                    pass
                    l_1_lifetime = str_join((environment.getattr(environment.getattr(l_1_sa_policy, 'sa_lifetime'), 'value'), ' ', t_1(environment.getattr(environment.getattr(l_1_sa_policy, 'sa_lifetime'), 'unit'), 'hours'), ))
                    _loop_vars['lifetime'] = l_1_lifetime
                yield '| '
                yield str(environment.getattr(l_1_sa_policy, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'integrity'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'encryption'), '-'))
                yield ' | '
                yield str(t_1((undefined(name='lifetime') if l_1_lifetime is missing else l_1_lifetime), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_sa_policy, 'pfs_dh_group'), '-'))
                yield ' |\n'
            l_1_sa_policy = l_1_lifetime = missing
        if t_3(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'profiles')):
            pass
            yield '\n### IPSec profiles\n\n| Profile name | IKE policy | SA policy | Connection | DPD Interval | DPD Time | DPD action | Mode | Flow Parallelization |\n| ------------ | ---------- | ----------| ---------- | ------------ | -------- | ---------- | ---- | -------------------- |\n'
            for l_1_profile in t_2(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'profiles'), 'name'):
                l_1_ike_policy = l_1_sa_policy = l_1_connection = l_1_dpd_interval = l_1_dpd_time = l_1_dpd_action = l_1_mode = l_1_flow_parallelization = missing
                _loop_vars = {}
                pass
                l_1_ike_policy = t_1(environment.getattr(l_1_profile, 'ike_policy'), '-')
                _loop_vars['ike_policy'] = l_1_ike_policy
                l_1_sa_policy = t_1(environment.getattr(l_1_profile, 'sa_policy'), '-')
                _loop_vars['sa_policy'] = l_1_sa_policy
                l_1_connection = t_1(environment.getattr(l_1_profile, 'connection'), '-')
                _loop_vars['connection'] = l_1_connection
                l_1_dpd_interval = t_1(environment.getattr(l_1_profile, 'dpd_interval'), '-')
                _loop_vars['dpd_interval'] = l_1_dpd_interval
                l_1_dpd_time = t_1(environment.getattr(l_1_profile, 'dpd_time'), '-')
                _loop_vars['dpd_time'] = l_1_dpd_time
                l_1_dpd_action = t_1(environment.getattr(l_1_profile, 'dpd_action'), '-')
                _loop_vars['dpd_action'] = l_1_dpd_action
                l_1_mode = t_1(environment.getattr(l_1_profile, 'mode'), '-')
                _loop_vars['mode'] = l_1_mode
                l_1_flow_parallelization = t_1(environment.getattr(l_1_profile, 'flow_parallelization_encapsulation_udp'), '-')
                _loop_vars['flow_parallelization'] = l_1_flow_parallelization
                yield '| '
                yield str(environment.getattr(l_1_profile, 'name'))
                yield ' | '
                yield str((undefined(name='ike_policy') if l_1_ike_policy is missing else l_1_ike_policy))
                yield ' | '
                yield str((undefined(name='sa_policy') if l_1_sa_policy is missing else l_1_sa_policy))
                yield ' | '
                yield str((undefined(name='connection') if l_1_connection is missing else l_1_connection))
                yield ' | '
                yield str((undefined(name='dpd_interval') if l_1_dpd_interval is missing else l_1_dpd_interval))
                yield ' | '
                yield str((undefined(name='dpd_time') if l_1_dpd_time is missing else l_1_dpd_time))
                yield ' | '
                yield str((undefined(name='dpd_action') if l_1_dpd_action is missing else l_1_dpd_action))
                yield ' | '
                yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                yield ' | '
                yield str((undefined(name='flow_parallelization') if l_1_flow_parallelization is missing else l_1_flow_parallelization))
                yield ' |\n'
            l_1_profile = l_1_ike_policy = l_1_sa_policy = l_1_connection = l_1_dpd_interval = l_1_dpd_time = l_1_dpd_action = l_1_mode = l_1_flow_parallelization = missing
        if t_3(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'key_controller')):
            pass
            yield '\n### Key controller\n\n| Profile name |\n| ------------ |\n| '
            yield str(t_1(environment.getattr(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'key_controller'), 'profile'), '-'))
            yield ' |\n'
        yield '\n### IP Security Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-security.j2', 'documentation/ip-security.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&10=33&14=36&20=39&21=43&24=56&30=59&31=63&32=65&34=68&37=79&43=82&44=86&45=88&46=90&47=92&48=94&49=96&50=98&51=100&52=103&55=122&61=125&67=128'