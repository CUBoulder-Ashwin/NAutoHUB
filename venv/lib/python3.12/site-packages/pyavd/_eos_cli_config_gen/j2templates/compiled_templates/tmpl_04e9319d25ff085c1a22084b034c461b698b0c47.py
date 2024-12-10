from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/interface-profiles.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_interface_profiles = resolve('interface_profiles')
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
    if t_2((undefined(name='interface_profiles') if l_0_interface_profiles is missing else l_0_interface_profiles)):
        pass
        for l_1_interface_profile in t_1((undefined(name='interface_profiles') if l_0_interface_profiles is missing else l_0_interface_profiles), 'name'):
            _loop_vars = {}
            pass
            yield '!\ninterface profile '
            yield str(environment.getattr(l_1_interface_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_interface_profile, 'commands')):
                pass
                for l_2_command in environment.getattr(l_1_interface_profile, 'commands'):
                    _loop_vars = {}
                    pass
                    yield '   command '
                    yield str(l_2_command)
                    yield '\n'
                l_2_command = missing
        l_1_interface_profile = missing

blocks = {}
debug_info = '7=24&8=26&10=30&11=32&12=34&13=38'