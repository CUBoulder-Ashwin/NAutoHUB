from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/aaa-authentication.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_authentication = resolve('aaa_authentication')
    l_0_lockout_cli = resolve('lockout_cli')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication)):
        pass
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'login'), 'default')):
            pass
            yield 'aaa authentication login default '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'login'), 'default'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'login'), 'console')):
            pass
            yield 'aaa authentication login console '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'login'), 'console'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'enable'), 'default')):
            pass
            yield 'aaa authentication enable default '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'enable'), 'default'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'dot1x'), 'default')):
            pass
            yield 'aaa authentication dot1x default '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'dot1x'), 'default'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'on_failure_log'), True):
            pass
            yield 'aaa authentication policy on-failure log\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'on_success_log'), True):
            pass
            yield 'aaa authentication policy on-success log\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'local'), 'allow_nopassword'), True):
            pass
            yield 'aaa authentication policy local allow-nopassword-remote-login\n'
        if (t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'failure')) and t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'duration'))):
            pass
            l_0_lockout_cli = str_join(('aaa authentication policy lockout failure ', environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'failure'), ))
            context.vars['lockout_cli'] = l_0_lockout_cli
            context.exported_vars.add('lockout_cli')
            if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'window')):
                pass
                l_0_lockout_cli = str_join(((undefined(name='lockout_cli') if l_0_lockout_cli is missing else l_0_lockout_cli), ' window ', environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'window'), ))
                context.vars['lockout_cli'] = l_0_lockout_cli
                context.exported_vars.add('lockout_cli')
            l_0_lockout_cli = str_join(((undefined(name='lockout_cli') if l_0_lockout_cli is missing else l_0_lockout_cli), ' duration ', environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'duration'), ))
            context.vars['lockout_cli'] = l_0_lockout_cli
            context.exported_vars.add('lockout_cli')
            yield str((undefined(name='lockout_cli') if l_0_lockout_cli is missing else l_0_lockout_cli))
            yield '\n'

blocks = {}
debug_info = '7=19&8=21&9=24&11=26&12=29&14=31&15=34&17=36&18=39&20=41&23=44&26=47&29=50&30=52&31=55&32=57&34=60&35=63'