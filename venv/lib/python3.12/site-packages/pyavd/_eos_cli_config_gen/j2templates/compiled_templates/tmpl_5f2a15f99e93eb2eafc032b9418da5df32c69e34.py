from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/domain-list.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_domain_list = resolve('domain_list')
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
    if t_2((undefined(name='domain_list') if l_0_domain_list is missing else l_0_domain_list)):
        pass
        for l_1_domain in t_1((undefined(name='domain_list') if l_0_domain_list is missing else l_0_domain_list)):
            _loop_vars = {}
            pass
            yield 'ip domain-list '
            yield str(l_1_domain)
            yield '\n'
        l_1_domain = missing

blocks = {}
debug_info = '7=24&8=26&9=30'