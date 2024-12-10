from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/daemon-terminattr.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_daemon_terminattr = resolve('daemon_terminattr')
    l_0_namespace = resolve('namespace')
    l_0_cvp_config = resolve('cvp_config')
    l_0_hide_passwords = resolve('hide_passwords')
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
    if t_5((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr)):
        pass
        l_0_cvp_config = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['cvp_config'] = l_0_cvp_config
        context.exported_vars.add('cvp_config')
        yield '!\ndaemon TerminAttr\n'
        if not isinstance(l_0_cvp_config, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_cvp_config['cli'] = 'exec /usr/bin/TerminAttr'
        for l_1_cluster in t_3(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'clusters'), 'name'):
            _loop_vars = {}
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.addr=', t_4(context.eval_ctx, environment.getattr(l_1_cluster, 'cvaddrs'), ','), ))
            if t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'method'), 'key'):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.auth=key,', t_2(t_1(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'key'), ''), (undefined(name='hide_passwords') if l_0_hide_passwords is missing else l_0_hide_passwords)), ))
            elif (t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'method'), 'token') and t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'token_file'))):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.auth=token,', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'token_file'), ))
            elif (t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'method'), 'token-secure') and t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'token_file'))):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.auth=token-secure,', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'token_file'), ))
            elif ((t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'method'), 'certs') and t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'cert_file'))) and t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'key_file'))):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.auth=certs,', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'cert_file'), ',', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'key_file'), ))
                if t_5(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'ca_file')):
                    pass
                    if not isinstance(l_0_cvp_config, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ',', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'ca_file'), ))
            if t_5(environment.getattr(l_1_cluster, 'cvvrf')):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.vrf=', environment.getattr(l_1_cluster, 'cvvrf'), ))
            if t_5(environment.getattr(l_1_cluster, 'cvsourceip')):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.sourceip=', environment.getattr(l_1_cluster, 'cvsourceip'), ))
            if t_5(environment.getattr(l_1_cluster, 'cvproxy')):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.proxy=', environment.getattr(l_1_cluster, 'cvproxy'), ))
            if t_5(environment.getattr(l_1_cluster, 'cvobscurekeyfile')):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.obscurekeyfile=', environment.getattr(l_1_cluster, 'cvobscurekeyfile'), ))
            if t_5(environment.getattr(l_1_cluster, 'cvsourceintf')):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvopt ', environment.getattr(l_1_cluster, 'name'), '.sourceintf=', environment.getattr(l_1_cluster, 'cvsourceintf'), ))
        l_1_cluster = missing
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvaddrs')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvaddr=', t_4(context.eval_ctx, environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvaddrs'), ','), ))
            if t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'method'), 'key'):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvauth=key,', t_2(t_1(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'key'), ''), (undefined(name='hide_passwords') if l_0_hide_passwords is missing else l_0_hide_passwords)), ))
            elif (t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'method'), 'token') and t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'token_file'))):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvauth=token,', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'token_file'), ))
            elif (t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'method'), 'token-secure') and t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'token_file'))):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvauth=token-secure,', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'token_file'), ))
            elif ((t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'method'), 'certs') and t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'cert_file'))) and t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'key_file'))):
                pass
                if not isinstance(l_0_cvp_config, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvauth=certs,', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'cert_file'), ',', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'key_file'), ))
                if t_5(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'ca_file')):
                    pass
                    if not isinstance(l_0_cvp_config, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ',', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'ca_file'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvvrf')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvvrf=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvvrf'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvsourceip')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvsourceip=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvsourceip'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvgnmi'), True):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvgnmi', ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvobscurekeyfile'), True):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvobscurekeyfile', ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'disable_aaa'), True):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -disableaaa', ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvproxy')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvproxy=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvproxy'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'grpcaddr')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -grpcaddr=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'grpcaddr'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'grpcreadonly'), True):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -grpcreadonly', ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'smashexcludes')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -smashexcludes=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'smashexcludes'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ingestexclude')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -ingestexclude=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ingestexclude'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'taillogs')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -taillogs=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'taillogs'), ))
        else:
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -taillogs', ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ecodhcpaddr')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -ecodhcpaddr=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ecodhcpaddr'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ipfix'), True):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -ipfix', ))
        elif t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ipfix'), False):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -ipfix=false', ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ipfixaddr')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -ipfixaddr=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ipfixaddr'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'sflow'), True):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -sflow', ))
        elif t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'sflow'), False):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -sflow=false', ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'sflowaddr')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -sflowaddr=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'sflowaddr'), ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvconfig'), True):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvconfig', ))
        if t_5(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvsourceintf')):
            pass
            if not isinstance(l_0_cvp_config, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_cvp_config['cli'] = str_join((environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'), ' -cvsourceintf=', environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvsourceintf'), ))
        yield '   '
        yield str(environment.getattr((undefined(name='cvp_config') if l_0_cvp_config is missing else l_0_cvp_config), 'cli'))
        yield '\n   no shutdown\n'

blocks = {}
debug_info = '7=45&8=47&11=51&12=54&13=57&14=60&15=62&16=65&17=67&18=70&19=72&20=75&21=77&22=80&23=82&26=85&27=87&29=90&30=92&32=95&33=97&35=100&36=102&38=105&39=107&42=111&43=113&44=116&45=118&46=121&47=123&48=126&49=128&50=131&51=133&52=136&53=138&57=141&58=143&60=146&61=148&63=151&64=153&66=156&67=158&69=161&70=163&72=166&73=168&75=171&76=173&78=176&79=178&81=181&82=183&84=186&85=188&87=191&88=193&90=198&92=201&93=203&95=206&96=208&97=211&98=213&100=216&101=218&103=221&104=223&105=226&106=228&108=231&109=233&111=236&112=238&114=241&115=243&117=247'