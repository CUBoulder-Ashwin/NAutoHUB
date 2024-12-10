from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/domain-list.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_domain_list = resolve('domain_list')
    try:
        t_1 = environment.filters['sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='domain_list') if l_0_domain_list is missing else l_0_domain_list)):
        pass
        yield '\n### IP Domain-list\n\n#### Domains List\n\n'
        for l_1_domain in t_1(environment, (undefined(name='domain_list') if l_0_domain_list is missing else l_0_domain_list)):
            _loop_vars = {}
            pass
            yield '- '
            yield str(l_1_domain)
            yield '\n'
        l_1_domain = missing
        yield '\n#### IP Domain-list Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/domain-list.j2', 'documentation/domain-list.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '!\n```\n'

blocks = {}
debug_info = '7=24&13=27&14=31&20=35'