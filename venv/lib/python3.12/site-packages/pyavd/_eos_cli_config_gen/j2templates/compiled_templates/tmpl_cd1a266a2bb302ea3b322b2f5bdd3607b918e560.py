from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/banners.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_banners = resolve('banners')
    l_0_login = resolve('login')
    l_0_motd = resolve('motd')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='banners') if l_0_banners is missing else l_0_banners), 'login')):
        pass
        yield '!\nbanner login\n'
        l_0_login = environment.getattr((undefined(name='banners') if l_0_banners is missing else l_0_banners), 'login')
        context.vars['login'] = l_0_login
        context.exported_vars.add('login')
        if (not context.call(environment.getattr(context.call(environment.getattr((undefined(name='login') if l_0_login is missing else l_0_login), 'rstrip')), 'endswith'), '\nEOF')):
            pass
            l_0_login = (context.call(environment.getattr((undefined(name='login') if l_0_login is missing else l_0_login), 'rstrip')) + '\nEOF\n')
            context.vars['login'] = l_0_login
            context.exported_vars.add('login')
        yield str((undefined(name='login') if l_0_login is missing else l_0_login))
        yield '\n'
    if t_1(environment.getattr((undefined(name='banners') if l_0_banners is missing else l_0_banners), 'motd')):
        pass
        yield '!\nbanner motd\n'
        l_0_motd = environment.getattr((undefined(name='banners') if l_0_banners is missing else l_0_banners), 'motd')
        context.vars['motd'] = l_0_motd
        context.exported_vars.add('motd')
        if (not context.call(environment.getattr(context.call(environment.getattr((undefined(name='motd') if l_0_motd is missing else l_0_motd), 'rstrip')), 'endswith'), '\nEOF')):
            pass
            l_0_motd = (context.call(environment.getattr((undefined(name='motd') if l_0_motd is missing else l_0_motd), 'rstrip')) + '\nEOF\n')
            context.vars['motd'] = l_0_motd
            context.exported_vars.add('motd')
        yield str((undefined(name='motd') if l_0_motd is missing else l_0_motd))
        yield '\n'

blocks = {}
debug_info = '7=20&10=23&11=26&12=28&14=31&16=33&19=36&20=39&21=41&23=44'