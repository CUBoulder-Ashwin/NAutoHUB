from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/local-users.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_local_users = resolve('local_users')
    try:
        t_1 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
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
        yield '!\n'
        for l_1_local_user in t_2((undefined(name='local_users') if l_0_local_users is missing else l_0_local_users), 'name'):
            l_1_hide_passwords = resolve('hide_passwords')
            l_1_local_ssh_key_cli = resolve('local_ssh_key_cli')
            l_1_local_secondary_ssh_key_cli = resolve('local_secondary_ssh_key_cli')
            l_1_local_user_cli = missing
            _loop_vars = {}
            pass
            l_1_local_user_cli = str_join(('username ', environment.getattr(l_1_local_user, 'name'), ))
            _loop_vars['local_user_cli'] = l_1_local_user_cli
            if t_3(environment.getattr(l_1_local_user, 'disabled'), True):
                pass
                yield 'no '
                yield str((undefined(name='local_user_cli') if l_1_local_user_cli is missing else l_1_local_user_cli))
                yield '\n'
                continue
            if t_3(environment.getattr(l_1_local_user, 'privilege')):
                pass
                l_1_local_user_cli = str_join(((undefined(name='local_user_cli') if l_1_local_user_cli is missing else l_1_local_user_cli), ' privilege ', environment.getattr(l_1_local_user, 'privilege'), ))
                _loop_vars['local_user_cli'] = l_1_local_user_cli
            if t_3(environment.getattr(l_1_local_user, 'role')):
                pass
                l_1_local_user_cli = str_join(((undefined(name='local_user_cli') if l_1_local_user_cli is missing else l_1_local_user_cli), ' role ', environment.getattr(l_1_local_user, 'role'), ))
                _loop_vars['local_user_cli'] = l_1_local_user_cli
            if t_3(environment.getattr(l_1_local_user, 'shell')):
                pass
                l_1_local_user_cli = str_join(((undefined(name='local_user_cli') if l_1_local_user_cli is missing else l_1_local_user_cli), ' shell ', environment.getattr(l_1_local_user, 'shell'), ))
                _loop_vars['local_user_cli'] = l_1_local_user_cli
            if t_3(environment.getattr(l_1_local_user, 'sha512_password')):
                pass
                l_1_local_user_cli = str_join(((undefined(name='local_user_cli') if l_1_local_user_cli is missing else l_1_local_user_cli), ' secret sha512 ', t_1(environment.getattr(l_1_local_user, 'sha512_password'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)), ))
                _loop_vars['local_user_cli'] = l_1_local_user_cli
            elif t_3(environment.getattr(l_1_local_user, 'no_password'), True):
                pass
                l_1_local_user_cli = str_join(((undefined(name='local_user_cli') if l_1_local_user_cli is missing else l_1_local_user_cli), ' nopassword', ))
                _loop_vars['local_user_cli'] = l_1_local_user_cli
            yield str((undefined(name='local_user_cli') if l_1_local_user_cli is missing else l_1_local_user_cli))
            yield '\n'
            if t_3(environment.getattr(l_1_local_user, 'ssh_key')):
                pass
                l_1_local_ssh_key_cli = str_join(('username ', environment.getattr(l_1_local_user, 'name'), ))
                _loop_vars['local_ssh_key_cli'] = l_1_local_ssh_key_cli
                l_1_local_ssh_key_cli = str_join(((undefined(name='local_ssh_key_cli') if l_1_local_ssh_key_cli is missing else l_1_local_ssh_key_cli), ' ssh-key ', environment.getattr(l_1_local_user, 'ssh_key'), ))
                _loop_vars['local_ssh_key_cli'] = l_1_local_ssh_key_cli
                yield str((undefined(name='local_ssh_key_cli') if l_1_local_ssh_key_cli is missing else l_1_local_ssh_key_cli))
                yield '\n'
                if t_3(environment.getattr(l_1_local_user, 'secondary_ssh_key')):
                    pass
                    l_1_local_secondary_ssh_key_cli = str_join(('username ', environment.getattr(l_1_local_user, 'name'), ))
                    _loop_vars['local_secondary_ssh_key_cli'] = l_1_local_secondary_ssh_key_cli
                    l_1_local_secondary_ssh_key_cli = str_join(((undefined(name='local_secondary_ssh_key_cli') if l_1_local_secondary_ssh_key_cli is missing else l_1_local_secondary_ssh_key_cli), ' ssh-key secondary ', environment.getattr(l_1_local_user, 'secondary_ssh_key'), ))
                    _loop_vars['local_secondary_ssh_key_cli'] = l_1_local_secondary_ssh_key_cli
                    yield str((undefined(name='local_secondary_ssh_key_cli') if l_1_local_secondary_ssh_key_cli is missing else l_1_local_secondary_ssh_key_cli))
                    yield '\n'
        l_1_local_user = l_1_local_user_cli = l_1_hide_passwords = l_1_local_ssh_key_cli = l_1_local_secondary_ssh_key_cli = missing

blocks = {}
debug_info = '7=30&9=33&10=40&11=42&12=45&13=47&15=48&16=50&18=52&19=54&21=56&22=58&24=60&25=62&26=64&27=66&29=68&30=70&31=72&32=74&33=76&34=78&35=80&36=82&37=84'