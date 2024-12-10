from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_security = resolve('management_security')
    l_0_entropy_sources = resolve('entropy_sources')
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
        t_4 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security)):
        pass
        yield '!\nmanagement security\n'
        if t_5(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_sources')):
            pass
            l_0_entropy_sources = []
            context.vars['entropy_sources'] = l_0_entropy_sources
            context.exported_vars.add('entropy_sources')
            for l_1_source in ['hardware', 'haveged', 'cpu_jitter']:
                _loop_vars = {}
                pass
                if t_5(environment.getitem(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_sources'), l_1_source), True):
                    pass
                    context.call(environment.getattr((undefined(name='entropy_sources') if l_0_entropy_sources is missing else l_0_entropy_sources), 'append'), context.call(environment.getattr(l_1_source, 'replace'), '_', ' ', _loop_vars=_loop_vars), _loop_vars=_loop_vars)
            l_1_source = missing
            if (undefined(name='entropy_sources') if l_0_entropy_sources is missing else l_0_entropy_sources):
                pass
                yield '   entropy source '
                yield str(t_4(context.eval_ctx, (undefined(name='entropy_sources') if l_0_entropy_sources is missing else l_0_entropy_sources), ' '))
                yield '\n'
            if t_5(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_sources'), 'hardware_exclusive'), True):
                pass
                yield '   entropy source hardware exclusive\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'minimum_length')):
            pass
            yield '   password minimum length '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'minimum_length'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_key_common'), True):
            pass
            yield '   password encryption-key common\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_reversible')):
            pass
            yield '   password encryption reversible '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_reversible'))
            yield '\n'
        for l_1_policy in t_3(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'policies'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   password policy '
            yield str(environment.getattr(l_1_policy, 'name'))
            yield '\n'
            if t_5(environment.getattr(l_1_policy, 'minimum')):
                pass
                if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'digits')):
                    pass
                    yield '      minimum digits '
                    yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'digits'))
                    yield '\n'
                if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'length')):
                    pass
                    yield '      minimum length '
                    yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'length'))
                    yield '\n'
                if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'lower')):
                    pass
                    yield '      minimum lower '
                    yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'lower'))
                    yield '\n'
                if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'special')):
                    pass
                    yield '      minimum special '
                    yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'special'))
                    yield '\n'
                if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'upper')):
                    pass
                    yield '      minimum upper '
                    yield str(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'upper'))
                    yield '\n'
            if t_5(environment.getattr(l_1_policy, 'maximum')):
                pass
                if t_5(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'repetitive')):
                    pass
                    yield '      maximum repetitive '
                    yield str(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'repetitive'))
                    yield '\n'
                if t_5(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'sequential')):
                    pass
                    yield '      maximum sequential '
                    yield str(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'sequential'))
                    yield '\n'
        l_1_policy = missing
        for l_1_profile in t_3(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'shared_secret_profiles'), 'profile'):
            _loop_vars = {}
            pass
            yield '   !\n   session shared-secret profile '
            yield str(environment.getattr(l_1_profile, 'profile'))
            yield '\n'
            for l_2_secret in t_3(environment.getattr(l_1_profile, 'secrets'), 'name'):
                l_2_hide_passwords = resolve('hide_passwords')
                l_2_secret_cli = resolve('secret_cli')
                _loop_vars = {}
                pass
                if (t_5(environment.getattr(l_2_secret, 'secret')) and ((t_5(environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'infinite'), True) or (environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'start_date_time') and t_5(environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'end_date_time')))) and (t_5(environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'infinite'), True) or (environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'start_date_time') and t_5(environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'end_date_time')))))):
                    pass
                    l_2_secret_cli = str_join(('secret ', environment.getattr(l_2_secret, 'name'), ' ', t_1(environment.getattr(l_2_secret, 'secret_type'), '7'), ' ', t_2(environment.getattr(l_2_secret, 'secret'), (undefined(name='hide_passwords') if l_2_hide_passwords is missing else l_2_hide_passwords)), ))
                    _loop_vars['secret_cli'] = l_2_secret_cli
                    if t_5(environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'infinite'), True):
                        pass
                        l_2_secret_cli = str_join(((undefined(name='secret_cli') if l_2_secret_cli is missing else l_2_secret_cli), ' receive-lifetime infinite', ))
                        _loop_vars['secret_cli'] = l_2_secret_cli
                    else:
                        pass
                        l_2_secret_cli = str_join(((undefined(name='secret_cli') if l_2_secret_cli is missing else l_2_secret_cli), ' receive-lifetime ', environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'start_date_time'), ' ', environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'end_date_time'), ))
                        _loop_vars['secret_cli'] = l_2_secret_cli
                    if t_5(environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'infinite'), True):
                        pass
                        l_2_secret_cli = str_join(((undefined(name='secret_cli') if l_2_secret_cli is missing else l_2_secret_cli), ' transmit-lifetime infinite', ))
                        _loop_vars['secret_cli'] = l_2_secret_cli
                    else:
                        pass
                        l_2_secret_cli = str_join(((undefined(name='secret_cli') if l_2_secret_cli is missing else l_2_secret_cli), ' transmit-lifetime ', environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'start_date_time'), ' ', environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'end_date_time'), ))
                        _loop_vars['secret_cli'] = l_2_secret_cli
                    if t_5(environment.getattr(l_2_secret, 'local_time'), True):
                        pass
                        l_2_secret_cli = str_join(((undefined(name='secret_cli') if l_2_secret_cli is missing else l_2_secret_cli), ' local-time', ))
                        _loop_vars['secret_cli'] = l_2_secret_cli
                    yield '      '
                    yield str((undefined(name='secret_cli') if l_2_secret_cli is missing else l_2_secret_cli))
                    yield '\n'
            l_2_secret = l_2_hide_passwords = l_2_secret_cli = missing
        l_1_profile = missing
        for l_1_ssl_profile in t_3(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'ssl_profiles')):
            _loop_vars = {}
            pass
            yield '   !\n   ssl profile '
            yield str(environment.getattr(l_1_ssl_profile, 'name'))
            yield '\n'
            if t_5(environment.getattr(l_1_ssl_profile, 'tls_versions')):
                pass
                yield '      tls versions '
                yield str(environment.getattr(l_1_ssl_profile, 'tls_versions'))
                yield '\n'
            if t_5(environment.getattr(l_1_ssl_profile, 'cipher_list')):
                pass
                yield '      cipher-list '
                yield str(environment.getattr(l_1_ssl_profile, 'cipher_list'))
                yield '\n'
            if t_5(environment.getattr(l_1_ssl_profile, 'trust_certificate')):
                pass
                for l_2_trust_cert in t_3(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'certificates')):
                    _loop_vars = {}
                    pass
                    yield '      trust certificate '
                    yield str(l_2_trust_cert)
                    yield '\n'
                l_2_trust_cert = missing
                if t_5(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'system'), True):
                    pass
                    yield '      trust certificate system\n'
                if t_5(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement')):
                    pass
                    if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement'), 'basic_constraint_ca'), True):
                        pass
                        yield '      trust certificate requirement basic-constraint ca true\n'
                    if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement'), 'hostname_fqdn'), True):
                        pass
                        yield '      trust certificate requirement hostname fqdn\n'
                if t_5(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'policy_expiry_date_ignore'), True):
                    pass
                    yield '      trust certificate policy expiry-date ignore\n'
            if t_5(environment.getattr(l_1_ssl_profile, 'chain_certificate')):
                pass
                for l_2_chain_cert in t_3(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'certificates')):
                    _loop_vars = {}
                    pass
                    yield '      chain certificate '
                    yield str(l_2_chain_cert)
                    yield '\n'
                l_2_chain_cert = missing
                if t_5(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement')):
                    pass
                    if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement'), 'basic_constraint_ca'), True):
                        pass
                        yield '      chain certificate requirement basic-constraint ca true\n'
                    if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement'), 'include_root_ca'), True):
                        pass
                        yield '      chain certificate requirement include root-ca\n'
            if t_5(environment.getattr(l_1_ssl_profile, 'certificate')):
                pass
                yield '      certificate '
                yield str(environment.getattr(environment.getattr(l_1_ssl_profile, 'certificate'), 'file'))
                yield ' key '
                yield str(environment.getattr(environment.getattr(l_1_ssl_profile, 'certificate'), 'key'))
                yield '\n'
            for l_2_crl in t_3(environment.getattr(l_1_ssl_profile, 'certificate_revocation_lists')):
                _loop_vars = {}
                pass
                yield '      crl '
                yield str(l_2_crl)
                yield '\n'
            l_2_crl = missing
        l_1_ssl_profile = missing

blocks = {}
debug_info = '7=43&10=46&11=48&12=51&13=54&14=56&17=58&18=61&20=63&24=66&25=69&27=71&30=74&31=77&33=79&35=83&36=85&37=87&38=90&40=92&41=95&43=97&44=100&46=102&47=105&49=107&50=110&53=112&54=114&55=117&57=119&58=122&62=125&64=129&65=131&66=136&69=138&70=140&71=142&73=146&75=148&76=150&78=154&80=156&81=158&83=161&87=165&89=169&90=171&91=174&93=176&94=179&96=181&97=183&98=187&100=190&103=193&104=195&107=198&111=201&115=204&116=206&117=210&119=213&120=215&123=218&128=221&129=224&131=228&132=232'