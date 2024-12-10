from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_security = resolve('management_security')
    l_0_entropy_sources = resolve('entropy_sources')
    l_0_ssl_profiles_certs = resolve('ssl_profiles_certs')
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
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security)):
        pass
        yield '\n## Management Security\n\n### Management Security Summary\n\n| Settings | Value |\n| -------- | ----- |\n'
        if t_5(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_sources')):
            pass
            l_0_entropy_sources = []
            context.vars['entropy_sources'] = l_0_entropy_sources
            context.exported_vars.add('entropy_sources')
            for l_1_source in ['hardware', 'haveged', 'cpu_jitter', 'hardware_exclusive']:
                _loop_vars = {}
                pass
                if t_5(environment.getitem(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_sources'), l_1_source), True):
                    pass
                    context.call(environment.getattr((undefined(name='entropy_sources') if l_0_entropy_sources is missing else l_0_entropy_sources), 'append'), context.call(environment.getattr(l_1_source, 'replace'), '_', ' ', _loop_vars=_loop_vars), _loop_vars=_loop_vars)
            l_1_source = missing
            yield '| Entropy sources | '
            yield str(t_3(context.eval_ctx, (undefined(name='entropy_sources') if l_0_entropy_sources is missing else l_0_entropy_sources), ', '))
            yield ' |\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_key_common')):
            pass
            yield '| Common password encryption key | '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_key_common'))
            yield ' |\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_reversible')):
            pass
            yield '| Reversible password encryption | '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_reversible'))
            yield ' |\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'minimum_length')):
            pass
            yield '| Minimum password length | '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'minimum_length'))
            yield ' |\n'
        if t_5(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'ssl_profiles')):
            pass
            yield '\n### Management Security SSL Profiles\n\n| SSL Profile Name | TLS protocol accepted | Certificate filename | Key filename | Cipher List | CRLs |\n| ---------------- | --------------------- | -------------------- | ------------ | ----------- | ---- |\n'
            l_0_ssl_profiles_certs = []
            context.vars['ssl_profiles_certs'] = l_0_ssl_profiles_certs
            context.exported_vars.add('ssl_profiles_certs')
            for l_1_ssl_profile in t_2(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'ssl_profiles')):
                l_1_crls = l_1_tmp_cert = missing
                _loop_vars = {}
                pass
                l_1_crls = '-'
                _loop_vars['crls'] = l_1_crls
                if t_5(environment.getattr(l_1_ssl_profile, 'certificate_revocation_lists')):
                    pass
                    l_1_crls = t_3(context.eval_ctx, t_2(environment.getattr(l_1_ssl_profile, 'certificate_revocation_lists')), '<br>')
                    _loop_vars['crls'] = l_1_crls
                yield '| '
                yield str(t_1(environment.getattr(l_1_ssl_profile, 'name'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ssl_profile, 'tls_versions'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_ssl_profile, 'certificate'), 'file'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_ssl_profile, 'certificate'), 'key'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ssl_profile, 'cipher_list'), '-'))
                yield ' | '
                yield str((undefined(name='crls') if l_1_crls is missing else l_1_crls))
                yield ' |\n'
                l_1_tmp_cert = {}
                _loop_vars['tmp_cert'] = l_1_tmp_cert
                if t_5(environment.getattr(l_1_ssl_profile, 'trust_certificate')):
                    pass
                    l_1_tmp_cert = {'trust_certificate': environment.getattr(l_1_ssl_profile, 'trust_certificate')}
                    _loop_vars['tmp_cert'] = l_1_tmp_cert
                if t_5(environment.getattr(l_1_ssl_profile, 'chain_certificate')):
                    pass
                    context.call(environment.getattr((undefined(name='tmp_cert') if l_1_tmp_cert is missing else l_1_tmp_cert), 'update'), {'chain_certificate': environment.getattr(l_1_ssl_profile, 'chain_certificate')}, _loop_vars=_loop_vars)
                if (t_4((undefined(name='tmp_cert') if l_1_tmp_cert is missing else l_1_tmp_cert)) > 0):
                    pass
                    context.call(environment.getattr((undefined(name='tmp_cert') if l_1_tmp_cert is missing else l_1_tmp_cert), 'update'), {'name': environment.getattr(l_1_ssl_profile, 'name')}, _loop_vars=_loop_vars)
                    context.call(environment.getattr((undefined(name='ssl_profiles_certs') if l_0_ssl_profiles_certs is missing else l_0_ssl_profiles_certs), 'append'), (undefined(name='tmp_cert') if l_1_tmp_cert is missing else l_1_tmp_cert), _loop_vars=_loop_vars)
            l_1_ssl_profile = l_1_crls = l_1_tmp_cert = missing
            for l_1_ssl_profile in t_2((undefined(name='ssl_profiles_certs') if l_0_ssl_profiles_certs is missing else l_0_ssl_profiles_certs), 'name'):
                l_1_trust_certs = resolve('trust_certs')
                l_1_requirement = resolve('requirement')
                l_1_tmp_requirement = resolve('tmp_requirement')
                l_1_policy = resolve('policy')
                l_1_system = resolve('system')
                l_1_chain_certs = resolve('chain_certs')
                _loop_vars = {}
                pass
                yield '\n### SSL profile '
                yield str(environment.getattr(l_1_ssl_profile, 'name'))
                yield ' Certificates Summary\n'
                if t_5(environment.getattr(l_1_ssl_profile, 'trust_certificate')):
                    pass
                    yield '\n| Trust Certificates | Requirement | Policy | System |\n| ------------------ | ----------- | ------ | ------ |\n'
                    l_1_trust_certs = t_3(context.eval_ctx, t_1(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'certificates'), '-'), ', ')
                    _loop_vars['trust_certs'] = l_1_trust_certs
                    l_1_requirement = '-'
                    _loop_vars['requirement'] = l_1_requirement
                    if t_5(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement')):
                        pass
                        l_1_tmp_requirement = []
                        _loop_vars['tmp_requirement'] = l_1_tmp_requirement
                        if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement'), 'basic_constraint_ca'), True):
                            pass
                            context.call(environment.getattr((undefined(name='tmp_requirement') if l_1_tmp_requirement is missing else l_1_tmp_requirement), 'append'), 'Basic Constraint CA', _loop_vars=_loop_vars)
                        if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'requirement'), 'hostname_fqdn'), True):
                            pass
                            context.call(environment.getattr((undefined(name='tmp_requirement') if l_1_tmp_requirement is missing else l_1_tmp_requirement), 'append'), 'Hostname must be FQDN', _loop_vars=_loop_vars)
                        if (t_4((undefined(name='tmp_requirement') if l_1_tmp_requirement is missing else l_1_tmp_requirement)) > 0):
                            pass
                            l_1_requirement = t_3(context.eval_ctx, (undefined(name='tmp_requirement') if l_1_tmp_requirement is missing else l_1_tmp_requirement), ', ')
                            _loop_vars['requirement'] = l_1_requirement
                    l_1_policy = '-'
                    _loop_vars['policy'] = l_1_policy
                    if t_5(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'policy_expiry_date_ignore'), True):
                        pass
                        l_1_policy = 'Ignore Expiry Date'
                        _loop_vars['policy'] = l_1_policy
                    if t_5(environment.getattr(environment.getattr(l_1_ssl_profile, 'trust_certificate'), 'system'), True):
                        pass
                        l_1_system = 'Enabled'
                        _loop_vars['system'] = l_1_system
                    else:
                        pass
                        l_1_system = '-'
                        _loop_vars['system'] = l_1_system
                    yield '| '
                    yield str((undefined(name='trust_certs') if l_1_trust_certs is missing else l_1_trust_certs))
                    yield ' | '
                    yield str((undefined(name='requirement') if l_1_requirement is missing else l_1_requirement))
                    yield ' | '
                    yield str((undefined(name='policy') if l_1_policy is missing else l_1_policy))
                    yield ' | '
                    yield str((undefined(name='system') if l_1_system is missing else l_1_system))
                    yield ' |\n'
                if t_5(environment.getattr(l_1_ssl_profile, 'chain_certificate')):
                    pass
                    yield '\n| Chain Certificates | Requirement |\n| ------------------ | ----------- |\n'
                    l_1_chain_certs = t_3(context.eval_ctx, t_1(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'certificates'), '-'), ', ')
                    _loop_vars['chain_certs'] = l_1_chain_certs
                    l_1_requirement = '-'
                    _loop_vars['requirement'] = l_1_requirement
                    if t_5(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement')):
                        pass
                        l_1_tmp_requirement = []
                        _loop_vars['tmp_requirement'] = l_1_tmp_requirement
                        if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement'), 'basic_constraint_ca'), True):
                            pass
                            context.call(environment.getattr((undefined(name='tmp_requirement') if l_1_tmp_requirement is missing else l_1_tmp_requirement), 'append'), 'Basic Constraint CA', _loop_vars=_loop_vars)
                        if t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ssl_profile, 'chain_certificate'), 'requirement'), 'include_root_ca'), True):
                            pass
                            context.call(environment.getattr((undefined(name='tmp_requirement') if l_1_tmp_requirement is missing else l_1_tmp_requirement), 'append'), 'Root CA Included', _loop_vars=_loop_vars)
                        if (t_4((undefined(name='tmp_requirement') if l_1_tmp_requirement is missing else l_1_tmp_requirement)) > 0):
                            pass
                            l_1_requirement = t_3(context.eval_ctx, (undefined(name='tmp_requirement') if l_1_tmp_requirement is missing else l_1_tmp_requirement), ', ')
                            _loop_vars['requirement'] = l_1_requirement
                    yield '| '
                    yield str((undefined(name='chain_certs') if l_1_chain_certs is missing else l_1_chain_certs))
                    yield ' | '
                    yield str((undefined(name='requirement') if l_1_requirement is missing else l_1_requirement))
                    yield ' |\n'
            l_1_ssl_profile = l_1_trust_certs = l_1_requirement = l_1_tmp_requirement = l_1_policy = l_1_system = l_1_chain_certs = missing
        if t_5(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'policies')):
            pass
            yield '\n### Password Policies\n\n| Policy Name | Digits | Length | Lowercase letters | Special characters | Uppercase letters | Repetitive characters | Sequential characters |\n|-------------|--------|--------|-------------------|--------------------|-------------------|-----------------------|----------------------|\n'
            for l_1_policy in t_2(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'policies'), 'name'):
                l_1_min_digits = l_1_min_length = l_1_min_lower = l_1_min_special = l_1_min_upper = l_1_max_repetitive = l_1_max_sequential = missing
                _loop_vars = {}
                pass
                l_1_min_digits = (environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'digits') if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'digits')) else 'N/A')
                _loop_vars['min_digits'] = l_1_min_digits
                l_1_min_length = (environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'length') if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'length')) else 'N/A')
                _loop_vars['min_length'] = l_1_min_length
                l_1_min_lower = (environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'lower') if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'lower')) else 'N/A')
                _loop_vars['min_lower'] = l_1_min_lower
                l_1_min_special = (environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'special') if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'special')) else 'N/A')
                _loop_vars['min_special'] = l_1_min_special
                l_1_min_upper = (environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'upper') if t_5(environment.getattr(environment.getattr(l_1_policy, 'minimum'), 'upper')) else 'N/A')
                _loop_vars['min_upper'] = l_1_min_upper
                l_1_max_repetitive = (environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'repetitive') if t_5(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'repetitive')) else 'N/A')
                _loop_vars['max_repetitive'] = l_1_max_repetitive
                l_1_max_sequential = (environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'sequential') if t_5(environment.getattr(environment.getattr(l_1_policy, 'maximum'), 'sequential')) else 'N/A')
                _loop_vars['max_sequential'] = l_1_max_sequential
                yield '| '
                yield str(environment.getattr(l_1_policy, 'name'))
                yield ' | > '
                yield str((undefined(name='min_digits') if l_1_min_digits is missing else l_1_min_digits))
                yield ' | > '
                yield str((undefined(name='min_length') if l_1_min_length is missing else l_1_min_length))
                yield ' | > '
                yield str((undefined(name='min_lower') if l_1_min_lower is missing else l_1_min_lower))
                yield ' | > '
                yield str((undefined(name='min_special') if l_1_min_special is missing else l_1_min_special))
                yield ' | > '
                yield str((undefined(name='min_upper') if l_1_min_upper is missing else l_1_min_upper))
                yield ' | < '
                yield str((undefined(name='max_repetitive') if l_1_max_repetitive is missing else l_1_max_repetitive))
                yield ' | < '
                yield str((undefined(name='max_sequential') if l_1_max_sequential is missing else l_1_max_sequential))
                yield ' |\n'
            l_1_policy = l_1_min_digits = l_1_min_length = l_1_min_lower = l_1_min_special = l_1_min_upper = l_1_max_repetitive = l_1_max_sequential = missing
        if t_5(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'shared_secret_profiles')):
            pass
            yield '\n### Session Shared-secret Profiles\n'
            for l_1_profile in t_2(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'shared_secret_profiles'), 'profile'):
                _loop_vars = {}
                pass
                yield '\n#### '
                yield str(environment.getattr(l_1_profile, 'profile'))
                yield '\n\n| Secret Name | Receive Lifetime | Transmit Lifetime | Timezone |\n| ----------- | ---------------- | ----------------- | -------- |\n'
                for l_2_secret in t_2(environment.getattr(l_1_profile, 'secrets'), 'name'):
                    l_2_timezone = resolve('timezone')
                    l_2_receive_lifetime = resolve('receive_lifetime')
                    l_2_transmit_lifetime = resolve('transmit_lifetime')
                    _loop_vars = {}
                    pass
                    if (t_5(environment.getattr(l_2_secret, 'secret')) and ((t_5(environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'infinite'), True) or (environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'start_date_time') and t_5(environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'end_date_time')))) and (t_5(environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'infinite'), True) or (environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'start_date_time') and t_5(environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'end_date_time')))))):
                        pass
                        if t_5(environment.getattr(l_2_secret, 'local_time'), True):
                            pass
                            l_2_timezone = 'Local Time'
                            _loop_vars['timezone'] = l_2_timezone
                        else:
                            pass
                            l_2_timezone = 'UTC'
                            _loop_vars['timezone'] = l_2_timezone
                        if t_5(environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'infinite'), True):
                            pass
                            l_2_receive_lifetime = 'Infinite'
                            _loop_vars['receive_lifetime'] = l_2_receive_lifetime
                        else:
                            pass
                            l_2_receive_lifetime = str_join((environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'start_date_time'), ' - ', environment.getattr(environment.getattr(l_2_secret, 'receive_lifetime'), 'end_date_time'), ))
                            _loop_vars['receive_lifetime'] = l_2_receive_lifetime
                        if t_5(environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'infinite'), True):
                            pass
                            l_2_transmit_lifetime = 'Infinite'
                            _loop_vars['transmit_lifetime'] = l_2_transmit_lifetime
                        else:
                            pass
                            l_2_transmit_lifetime = str_join((environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'start_date_time'), ' - ', environment.getattr(environment.getattr(l_2_secret, 'transmit_lifetime'), 'end_date_time'), ))
                            _loop_vars['transmit_lifetime'] = l_2_transmit_lifetime
                        yield '| '
                        yield str(environment.getattr(l_2_secret, 'name'))
                        yield ' | '
                        yield str(t_1((undefined(name='receive_lifetime') if l_2_receive_lifetime is missing else l_2_receive_lifetime), '-'))
                        yield ' | '
                        yield str(t_1((undefined(name='transmit_lifetime') if l_2_transmit_lifetime is missing else l_2_transmit_lifetime), '-'))
                        yield ' | '
                        yield str((undefined(name='timezone') if l_2_timezone is missing else l_2_timezone))
                        yield ' |\n'
                l_2_secret = l_2_timezone = l_2_receive_lifetime = l_2_transmit_lifetime = missing
            l_1_profile = missing
        yield '\n### Management Security Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-security.j2', 'documentation/management-security.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'entropy_sources': l_0_entropy_sources, 'ssl_profiles_certs': l_0_ssl_profiles_certs})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=44&15=47&16=49&17=52&18=55&19=57&22=60&24=62&25=65&27=67&28=70&30=72&31=75&33=77&39=80&40=83&41=87&42=89&43=91&45=94&46=106&47=108&48=110&50=112&51=114&53=115&54=117&55=118&58=120&60=130&61=132&65=135&66=137&67=139&68=141&69=143&70=145&72=146&73=148&75=149&76=151&79=153&80=155&81=157&83=159&84=161&86=165&88=168&90=176&94=179&95=181&96=183&97=185&98=187&99=189&101=190&102=192&104=193&105=195&108=198&112=203&118=206&119=210&120=212&121=214&122=216&123=218&124=220&125=222&126=225&129=242&132=245&134=249&138=251&139=257&144=259&145=261&147=265&149=267&150=269&152=273&154=275&155=277&157=281&159=284&168=295'