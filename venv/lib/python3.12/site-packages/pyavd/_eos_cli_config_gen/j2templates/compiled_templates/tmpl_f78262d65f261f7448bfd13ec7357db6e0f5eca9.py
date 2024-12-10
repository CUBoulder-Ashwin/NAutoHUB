from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/radius-server.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_radius_server = resolve('radius_server')
    l_0_attribute_32_include_in_access_cli = resolve('attribute_32_include_in_access_cli')
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
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server)):
        pass
        yield '!\n'
        if t_3(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'deadtime')):
            pass
            yield 'radius-server deadtime '
            yield str(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'deadtime'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'attribute_32_include_in_access_req')):
            pass
            l_0_attribute_32_include_in_access_cli = 'radius-server attribute 32 include-in-access-req'
            context.vars['attribute_32_include_in_access_cli'] = l_0_attribute_32_include_in_access_cli
            context.exported_vars.add('attribute_32_include_in_access_cli')
            if t_3(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'attribute_32_include_in_access_req'), 'hostname'), True):
                pass
                l_0_attribute_32_include_in_access_cli = str_join(((undefined(name='attribute_32_include_in_access_cli') if l_0_attribute_32_include_in_access_cli is missing else l_0_attribute_32_include_in_access_cli), ' hostname', ))
                context.vars['attribute_32_include_in_access_cli'] = l_0_attribute_32_include_in_access_cli
                context.exported_vars.add('attribute_32_include_in_access_cli')
            elif t_3(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'attribute_32_include_in_access_req'), 'format')):
                pass
                l_0_attribute_32_include_in_access_cli = str_join(((undefined(name='attribute_32_include_in_access_cli') if l_0_attribute_32_include_in_access_cli is missing else l_0_attribute_32_include_in_access_cli), ' format ', environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'attribute_32_include_in_access_req'), 'format'), ))
                context.vars['attribute_32_include_in_access_cli'] = l_0_attribute_32_include_in_access_cli
                context.exported_vars.add('attribute_32_include_in_access_cli')
            yield str((undefined(name='attribute_32_include_in_access_cli') if l_0_attribute_32_include_in_access_cli is missing else l_0_attribute_32_include_in_access_cli))
            yield '\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization'), 'port')):
            pass
            yield 'radius-server dynamic-authorization port '
            yield str(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization'), 'port'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'tls_ssl_profile')):
            pass
            yield 'radius-server tls ssl-profile '
            yield str(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'tls_ssl_profile'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization'), 'tls_ssl_profile')):
            pass
            yield 'radius-server dynamic-authorization tls ssl-profile '
            yield str(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization'), 'tls_ssl_profile'))
            yield '\n'
        for l_1_radius_host in t_1(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'hosts'), []):
            l_1_hide_passwords = resolve('hide_passwords')
            l_1_radius_cli = missing
            _loop_vars = {}
            pass
            l_1_radius_cli = str_join(('radius-server host ', environment.getattr(l_1_radius_host, 'host'), ))
            _loop_vars['radius_cli'] = l_1_radius_cli
            if (t_3(environment.getattr(l_1_radius_host, 'vrf')) and (environment.getattr(l_1_radius_host, 'vrf') != 'default')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' vrf ', environment.getattr(l_1_radius_host, 'vrf'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if t_3(environment.getattr(environment.getattr(l_1_radius_host, 'tls'), 'enabled'), True):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' tls', ))
                _loop_vars['radius_cli'] = l_1_radius_cli
                if t_3(environment.getattr(environment.getattr(l_1_radius_host, 'tls'), 'ssl_profile')):
                    pass
                    l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' ssl-profile ', environment.getattr(environment.getattr(l_1_radius_host, 'tls'), 'ssl_profile'), ))
                    _loop_vars['radius_cli'] = l_1_radius_cli
                if t_3(environment.getattr(environment.getattr(l_1_radius_host, 'tls'), 'port')):
                    pass
                    l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' port ', environment.getattr(environment.getattr(l_1_radius_host, 'tls'), 'port'), ))
                    _loop_vars['radius_cli'] = l_1_radius_cli
            if t_3(environment.getattr(l_1_radius_host, 'timeout')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' timeout ', environment.getattr(l_1_radius_host, 'timeout'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if t_3(environment.getattr(l_1_radius_host, 'retransmit')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' retransmit ', environment.getattr(l_1_radius_host, 'retransmit'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if (t_3(environment.getattr(l_1_radius_host, 'key')) and (not t_3(environment.getattr(environment.getattr(l_1_radius_host, 'tls'), 'enabled'), True))):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' key 7 ', t_2(environment.getattr(l_1_radius_host, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            yield str((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli))
            yield '\n'
        l_1_radius_host = l_1_radius_cli = l_1_hide_passwords = missing

blocks = {}
debug_info = '7=31&9=34&10=37&12=39&13=41&14=44&15=46&16=49&17=51&19=54&21=56&22=59&24=61&25=64&27=66&28=69&30=71&31=76&32=78&33=80&35=82&36=84&37=86&38=88&40=90&41=92&44=94&45=96&47=98&48=100&50=102&51=104&53=106'