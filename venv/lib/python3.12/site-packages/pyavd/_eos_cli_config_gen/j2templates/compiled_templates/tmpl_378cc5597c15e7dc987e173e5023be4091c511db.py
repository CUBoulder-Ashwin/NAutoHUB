from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/stun.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_stun = resolve('stun')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='stun') if l_0_stun is missing else l_0_stun)):
        pass
        yield '!\nstun\n'
        if t_2(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client')):
            pass
            yield '   client\n'
            for l_1_profile in t_1(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client'), 'server_profiles'), 'name'):
                _loop_vars = {}
                pass
                yield '      server-profile '
                yield str(environment.getattr(l_1_profile, 'name'))
                yield '\n'
                if t_2(environment.getattr(l_1_profile, 'ip_address')):
                    pass
                    yield '         ip address '
                    yield str(environment.getattr(l_1_profile, 'ip_address'))
                    yield '\n'
                if t_2(environment.getattr(l_1_profile, 'port')):
                    pass
                    yield '         port '
                    yield str(environment.getattr(l_1_profile, 'port'))
                    yield '\n'
                if t_2(environment.getattr(l_1_profile, 'ssl_profile')):
                    pass
                    yield '         ssl profile '
                    yield str(environment.getattr(l_1_profile, 'ssl_profile'))
                    yield '\n'
            l_1_profile = missing
        if t_2(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server')):
            pass
            yield '   server\n'
            for l_1_local_interface in t_1(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'local_interfaces')):
                _loop_vars = {}
                pass
                yield '      local-interface '
                yield str(l_1_local_interface)
                yield '\n'
            l_1_local_interface = missing
            if t_2(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'port')):
                pass
                yield '      port '
                yield str(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'port'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_profile')):
                pass
                yield '      ssl profile '
                yield str(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_profile'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'bindings_timeout')):
                pass
                yield '      binding timeout '
                yield str(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'bindings_timeout'))
                yield ' seconds\n'
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_connection_lifetime'), 'minutes')):
                pass
                yield '      ssl connection lifetime '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_connection_lifetime'), 'minutes'))
                yield ' minutes\n'
            elif t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_connection_lifetime'), 'hours')):
                pass
                yield '      ssl connection lifetime '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'segitrver'), 'ssl_connection_lifetime'), 'hours'))
                yield ' hours\n'

blocks = {}
debug_info = '7=24&10=27&12=30&13=34&14=36&15=39&17=41&18=44&20=46&21=49&25=52&27=55&28=59&30=62&31=65&33=67&34=70&36=72&37=75&39=77&40=80&41=82&42=85'