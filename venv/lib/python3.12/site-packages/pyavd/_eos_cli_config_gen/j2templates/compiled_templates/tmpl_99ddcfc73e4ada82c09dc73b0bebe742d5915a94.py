from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/roles.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_roles = resolve('roles')
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
    for l_1_role in t_1((undefined(name='roles') if l_0_roles is missing else l_0_roles), 'name'):
        _loop_vars = {}
        pass
        yield '!\nrole '
        yield str(environment.getattr(l_1_role, 'name'))
        yield '\n'
        if t_2(environment.getattr(l_1_role, 'sequence_numbers')):
            pass
            for l_2_sequence in environment.getattr(l_1_role, 'sequence_numbers'):
                l_2_sequence_cli = resolve('sequence_cli')
                _loop_vars = {}
                pass
                if (t_2(environment.getattr(l_2_sequence, 'action')) and t_2(environment.getattr(l_2_sequence, 'command'))):
                    pass
                    l_2_sequence_cli = ''
                    _loop_vars['sequence_cli'] = l_2_sequence_cli
                    if t_2(environment.getattr(l_2_sequence, 'sequence')):
                        pass
                        l_2_sequence_cli = str_join((environment.getattr(l_2_sequence, 'sequence'), ' ', ))
                        _loop_vars['sequence_cli'] = l_2_sequence_cli
                    l_2_sequence_cli = str_join(((undefined(name='sequence_cli') if l_2_sequence_cli is missing else l_2_sequence_cli), environment.getattr(l_2_sequence, 'action'), ))
                    _loop_vars['sequence_cli'] = l_2_sequence_cli
                    if t_2(environment.getattr(l_2_sequence, 'mode')):
                        pass
                        l_2_sequence_cli = str_join(((undefined(name='sequence_cli') if l_2_sequence_cli is missing else l_2_sequence_cli), ' mode ', environment.getattr(l_2_sequence, 'mode'), ))
                        _loop_vars['sequence_cli'] = l_2_sequence_cli
                    l_2_sequence_cli = str_join(((undefined(name='sequence_cli') if l_2_sequence_cli is missing else l_2_sequence_cli), ' command ', environment.getattr(l_2_sequence, 'command'), ))
                    _loop_vars['sequence_cli'] = l_2_sequence_cli
                    yield '   '
                    yield str((undefined(name='sequence_cli') if l_2_sequence_cli is missing else l_2_sequence_cli))
                    yield '\n'
            l_2_sequence = l_2_sequence_cli = missing
    l_1_role = missing

blocks = {}
debug_info = '7=24&9=28&10=30&11=32&12=36&13=38&14=40&15=42&17=44&18=46&19=48&21=50&22=53'