from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-security.j2'

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
        t_2 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
    try:
        t_3 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security)):
        pass
        yield '!\nip security\n'
        l_1_loop = missing
        for l_1_ike_policy, l_1_loop in LoopContext(t_3(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'ike_policies'), 'name'), undefined):
            _loop_vars = {}
            pass
            if (not environment.getattr(l_1_loop, 'first')):
                pass
                yield '   !\n'
            yield '   ike policy '
            yield str(environment.getattr(l_1_ike_policy, 'name'))
            yield '\n'
            if t_4(environment.getattr(l_1_ike_policy, 'integrity')):
                pass
                yield '      integrity '
                yield str(environment.getattr(l_1_ike_policy, 'integrity'))
                yield '\n'
            if t_4(environment.getattr(l_1_ike_policy, 'ike_lifetime')):
                pass
                yield '      ike-lifetime '
                yield str(environment.getattr(l_1_ike_policy, 'ike_lifetime'))
                yield '\n'
            if t_4(environment.getattr(l_1_ike_policy, 'encryption')):
                pass
                yield '      encryption '
                yield str(environment.getattr(l_1_ike_policy, 'encryption'))
                yield '\n'
            if t_4(environment.getattr(l_1_ike_policy, 'dh_group')):
                pass
                yield '      dh-group '
                yield str(environment.getattr(l_1_ike_policy, 'dh_group'))
                yield '\n'
            if t_4(environment.getattr(l_1_ike_policy, 'local_id_fqdn')):
                pass
                yield '      local-id fqdn '
                yield str(environment.getattr(l_1_ike_policy, 'local_id_fqdn'))
                yield '\n'
            elif t_4(environment.getattr(l_1_ike_policy, 'local_id')):
                pass
                yield '      local-id '
                yield str(environment.getattr(l_1_ike_policy, 'local_id'))
                yield '\n'
        l_1_loop = l_1_ike_policy = missing
        for l_1_sa_policy in t_3(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'sa_policies'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   sa policy '
            yield str(environment.getattr(l_1_sa_policy, 'name'))
            yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'encryption')):
                pass
                if (environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'encryption') == 'disabled'):
                    pass
                    yield '      esp encryption null\n'
                else:
                    pass
                    yield '      esp encryption '
                    yield str(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'encryption'))
                    yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'integrity')):
                pass
                if (environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'integrity') == 'disabled'):
                    pass
                    yield '      esp integrity null\n'
                else:
                    pass
                    yield '      esp integrity '
                    yield str(environment.getattr(environment.getattr(l_1_sa_policy, 'esp'), 'integrity'))
                    yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_sa_policy, 'sa_lifetime'), 'value')):
                pass
                yield '      sa lifetime '
                yield str(environment.getattr(environment.getattr(l_1_sa_policy, 'sa_lifetime'), 'value'))
                yield ' '
                yield str(t_1(environment.getattr(environment.getattr(l_1_sa_policy, 'sa_lifetime'), 'unit'), 'hours'))
                yield '\n'
            if t_4(environment.getattr(l_1_sa_policy, 'pfs_dh_group')):
                pass
                yield '      pfs dh-group '
                yield str(environment.getattr(l_1_sa_policy, 'pfs_dh_group'))
                yield '\n'
        l_1_sa_policy = missing
        for l_1_profile in t_3(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'profiles'), 'name'):
            l_1_hide_passwords = resolve('hide_passwords')
            _loop_vars = {}
            pass
            yield '   !\n   profile '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n'
            if t_4(environment.getattr(l_1_profile, 'ike_policy')):
                pass
                yield '      ike-policy '
                yield str(environment.getattr(l_1_profile, 'ike_policy'))
                yield '\n'
            if t_4(environment.getattr(l_1_profile, 'sa_policy')):
                pass
                yield '      sa-policy '
                yield str(environment.getattr(l_1_profile, 'sa_policy'))
                yield '\n'
            if t_4(environment.getattr(l_1_profile, 'connection')):
                pass
                yield '      connection '
                yield str(environment.getattr(l_1_profile, 'connection'))
                yield '\n'
            if t_4(environment.getattr(l_1_profile, 'shared_key')):
                pass
                yield '      shared-key 7 '
                yield str(t_2(environment.getattr(l_1_profile, 'shared_key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                yield '\n'
            if ((t_4(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'interval')) and t_4(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'time'))) and t_4(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'action'))):
                pass
                yield '      dpd '
                yield str(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'interval'))
                yield ' '
                yield str(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'time'))
                yield ' '
                yield str(environment.getattr(environment.getattr(l_1_profile, 'dpd'), 'action'))
                yield '\n'
            if t_4(environment.getattr(l_1_profile, 'flow_parallelization_encapsulation_udp'), True):
                pass
                yield '      flow parallelization encapsulation udp\n'
            if t_4(environment.getattr(l_1_profile, 'mode')):
                pass
                yield '      mode '
                yield str(environment.getattr(l_1_profile, 'mode'))
                yield '\n'
        l_1_profile = l_1_hide_passwords = missing
        if t_4(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'key_controller')):
            pass
            yield '   !\n   key controller\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'key_controller'), 'profile')):
                pass
                yield '      profile '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'key_controller'), 'profile'))
                yield '\n'
        if t_4(environment.getattr((undefined(name='ip_security') if l_0_ip_security is missing else l_0_ip_security), 'hardware_encryption_disabled'), True):
            pass
            yield '   hardware encryption disabled\n'

blocks = {}
debug_info = '7=36&10=40&11=43&14=47&15=49&16=52&18=54&19=57&21=59&22=62&24=64&25=67&27=69&28=72&29=74&30=77&33=80&35=84&36=86&37=88&40=94&43=96&44=98&47=104&50=106&51=109&53=113&54=116&57=119&59=124&60=126&61=129&63=131&64=134&66=136&67=139&69=141&70=144&72=146&73=149&75=155&78=158&79=161&82=164&85=167&86=170&89=172'