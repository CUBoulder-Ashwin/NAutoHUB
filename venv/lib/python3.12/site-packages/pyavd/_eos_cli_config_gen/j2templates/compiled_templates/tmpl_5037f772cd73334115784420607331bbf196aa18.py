from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/vrfs.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vrfs = resolve('vrfs')
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
    for l_1_vrf in t_1((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs), 'name'):
        _loop_vars = {}
        pass
        if (environment.getattr(l_1_vrf, 'name') != 'default'):
            pass
            yield '!\nvrf instance '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_vrf, 'description')):
                pass
                yield '   description '
                yield str(environment.getattr(l_1_vrf, 'description'))
                yield '\n'
    l_1_vrf = missing

blocks = {}
debug_info = '7=24&8=27&10=30&11=32&12=35'