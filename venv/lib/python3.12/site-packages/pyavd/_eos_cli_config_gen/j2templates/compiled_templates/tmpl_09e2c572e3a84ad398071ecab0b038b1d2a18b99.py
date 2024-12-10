from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/local-users.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_local_users = resolve('local_users')
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
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='local_users') if l_0_local_users is missing else l_0_local_users)):
        pass
        yield '\n### Local Users\n\n#### Local Users Summary\n\n| User | Privilege | Role | Disabled | Shell |\n| ---- | --------- | ---- | -------- | ----- |\n'
        for l_1_local_user in t_2((undefined(name='local_users') if l_0_local_users is missing else l_0_local_users), 'name'):
            l_1_role = l_1_privilege = l_1_disabled = l_1_shell = missing
            _loop_vars = {}
            pass
            l_1_role = t_1(environment.getattr(l_1_local_user, 'role'), '-')
            _loop_vars['role'] = l_1_role
            l_1_privilege = t_1(environment.getattr(l_1_local_user, 'privilege'), '-')
            _loop_vars['privilege'] = l_1_privilege
            l_1_disabled = t_1(environment.getattr(l_1_local_user, 'disabled'), False)
            _loop_vars['disabled'] = l_1_disabled
            l_1_shell = t_1(environment.getattr(l_1_local_user, 'shell'), '-')
            _loop_vars['shell'] = l_1_shell
            yield '| '
            yield str(environment.getattr(l_1_local_user, 'name'))
            yield ' | '
            yield str((undefined(name='privilege') if l_1_privilege is missing else l_1_privilege))
            yield ' | '
            yield str((undefined(name='role') if l_1_role is missing else l_1_role))
            yield ' | '
            yield str((undefined(name='disabled') if l_1_disabled is missing else l_1_disabled))
            yield ' | '
            yield str((undefined(name='shell') if l_1_shell is missing else l_1_shell))
            yield ' |\n'
        l_1_local_user = l_1_role = l_1_privilege = l_1_disabled = l_1_shell = missing
        yield '\n#### Local Users Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/local-users.j2', 'documentation/local-users.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=37&17=39&18=41&19=43&20=46&26=58'