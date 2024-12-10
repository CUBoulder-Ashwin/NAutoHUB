from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-api-gnmi.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_api_gnmi = resolve('management_api_gnmi')
    l_0_first_line = resolve('first_line')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi)):
        pass
        l_0_first_line = True
        context.vars['first_line'] = l_0_first_line
        context.exported_vars.add('first_line')
        yield '!\nmanagement api gnmi\n'
        if t_3(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport')):
            pass
            if t_3(environment.getattr(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport'), 'grpc')):
                pass
                l_0_first_line = False
                context.vars['first_line'] = l_0_first_line
                context.exported_vars.add('first_line')
                l_1_loop = missing
                for l_1_transport, l_1_loop in LoopContext(t_1(environment.getattr(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport'), 'grpc'), 'name'), undefined):
                    _loop_vars = {}
                    pass
                    if (not environment.getattr(l_1_loop, 'first')):
                        pass
                        yield '   !\n'
                    if t_3(environment.getattr(l_1_transport, 'name')):
                        pass
                        yield '   transport grpc '
                        yield str(environment.getattr(l_1_transport, 'name'))
                        yield '\n'
                        if t_3(environment.getattr(l_1_transport, 'ssl_profile')):
                            pass
                            yield '      ssl profile '
                            yield str(environment.getattr(l_1_transport, 'ssl_profile'))
                            yield '\n'
                        if t_3(environment.getattr(l_1_transport, 'port')):
                            pass
                            yield '      port '
                            yield str(environment.getattr(l_1_transport, 'port'))
                            yield '\n'
                        if t_3(environment.getattr(l_1_transport, 'vrf')):
                            pass
                            yield '      vrf '
                            yield str(environment.getattr(l_1_transport, 'vrf'))
                            yield '\n'
                        if t_3(environment.getattr(l_1_transport, 'ip_access_group')):
                            pass
                            yield '      ip access-group '
                            yield str(environment.getattr(l_1_transport, 'ip_access_group'))
                            yield '\n'
                        if t_3(environment.getattr(l_1_transport, 'notification_timestamp')):
                            pass
                            yield '      notification timestamp '
                            yield str(environment.getattr(l_1_transport, 'notification_timestamp'))
                            yield '\n'
                l_1_loop = l_1_transport = missing
            if t_3(environment.getattr(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport'), 'grpc_tunnels')):
                pass
                if (not ((undefined(name='first_line') if l_0_first_line is missing else l_0_first_line) == True)):
                    pass
                    yield '   !\n'
                l_1_loop = missing
                for l_1_transport, l_1_loop in LoopContext(t_1(environment.getattr(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport'), 'grpc_tunnels'), 'name'), undefined):
                    _loop_vars = {}
                    pass
                    if (not environment.getattr(l_1_loop, 'first')):
                        pass
                        yield '   !\n'
                    yield '   transport grpc-tunnel '
                    yield str(environment.getattr(l_1_transport, 'name'))
                    yield '\n'
                    if t_3(environment.getattr(l_1_transport, 'shutdown'), True):
                        pass
                        yield '      shutdown\n'
                    elif t_3(environment.getattr(l_1_transport, 'shutdown'), False):
                        pass
                        yield '      no shutdown\n'
                    if t_3(environment.getattr(l_1_transport, 'vrf')):
                        pass
                        yield '      vrf '
                        yield str(environment.getattr(l_1_transport, 'vrf'))
                        yield '\n'
                    if t_3(environment.getattr(l_1_transport, 'tunnel_ssl_profile')):
                        pass
                        yield '      tunnel ssl profile '
                        yield str(environment.getattr(l_1_transport, 'tunnel_ssl_profile'))
                        yield '\n'
                    if t_3(environment.getattr(l_1_transport, 'gnmi_ssl_profile')):
                        pass
                        yield '      gnmi ssl profile '
                        yield str(environment.getattr(l_1_transport, 'gnmi_ssl_profile'))
                        yield '\n'
                    if t_3(environment.getattr(l_1_transport, 'destination')):
                        pass
                        yield '      destination '
                        yield str(environment.getattr(environment.getattr(l_1_transport, 'destination'), 'address'))
                        yield ' port '
                        yield str(environment.getattr(environment.getattr(l_1_transport, 'destination'), 'port'))
                        yield '\n'
                    if t_3(environment.getattr(l_1_transport, 'local_interface')):
                        pass
                        yield '      local interface '
                        yield str(environment.getattr(environment.getattr(l_1_transport, 'local_interface'), 'name'))
                        yield ' port '
                        yield str(environment.getattr(environment.getattr(l_1_transport, 'local_interface'), 'port'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_1_transport, 'target'), 'use_serial_number'), True):
                        pass
                        if t_3(environment.getattr(environment.getattr(l_1_transport, 'target'), 'target_ids')):
                            pass
                            yield '      target serial-number '
                            yield str(t_2(context.eval_ctx, environment.getattr(environment.getattr(l_1_transport, 'target'), 'target_ids'), ' '))
                            yield '\n'
                        else:
                            pass
                            yield '      target serial-number\n'
                    elif t_3(environment.getattr(environment.getattr(l_1_transport, 'target'), 'target_ids')):
                        pass
                        yield '      target '
                        yield str(t_2(context.eval_ctx, environment.getattr(environment.getattr(l_1_transport, 'target'), 'target_ids'), ' '))
                        yield '\n'
                l_1_loop = l_1_transport = missing
        if t_3(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'provider')):
            pass
            yield '   provider '
            yield str(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'provider'))
            yield '\n'

blocks = {}
debug_info = '7=31&8=33&11=37&12=39&13=41&14=45&15=48&18=51&19=54&20=56&21=59&23=61&24=64&26=66&27=69&29=71&30=74&32=76&33=79&38=82&39=84&42=88&43=91&46=95&47=97&49=100&52=103&53=106&55=108&56=111&58=113&59=116&61=118&62=121&64=125&65=128&67=132&68=134&69=137&73=142&74=145&79=148&80=151'