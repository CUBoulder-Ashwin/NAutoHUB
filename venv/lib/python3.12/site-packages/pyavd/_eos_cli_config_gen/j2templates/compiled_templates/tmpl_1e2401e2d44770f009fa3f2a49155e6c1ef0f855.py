from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-accounts.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_accounts = resolve('management_accounts')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='management_accounts') if l_0_management_accounts is missing else l_0_management_accounts)):
        pass
        yield '!\nmanagement accounts\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='management_accounts') if l_0_management_accounts is missing else l_0_management_accounts), 'password'), 'policy')):
            pass
            yield '   password policy '
            yield str(environment.getattr(environment.getattr((undefined(name='management_accounts') if l_0_management_accounts is missing else l_0_management_accounts), 'password'), 'policy'))
            yield '\n'

blocks = {}
debug_info = '7=18&10=21&11=24'