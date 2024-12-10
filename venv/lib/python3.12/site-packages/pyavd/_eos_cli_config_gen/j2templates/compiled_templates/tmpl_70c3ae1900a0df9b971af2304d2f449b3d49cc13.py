from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-accounts.j2'

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
        yield '\n### Management Accounts\n\n#### Password Policy\n\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='management_accounts') if l_0_management_accounts is missing else l_0_management_accounts), 'password'), 'policy')):
            pass
            yield 'The password policy set for management accounts is: '
            yield str(environment.getattr(environment.getattr((undefined(name='management_accounts') if l_0_management_accounts is missing else l_0_management_accounts), 'password'), 'policy'))
            yield '\n'
        else:
            pass
            yield 'No specific password policy is set for management accounts.\n'
        yield '\n#### Management Accounts Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-accounts.j2', 'documentation/management-accounts.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&13=21&14=24&22=30'