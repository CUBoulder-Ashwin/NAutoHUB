from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/pim-sparse-mode.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_pim_sparse_mode = resolve('router_pim_sparse_mode')
    l_0_pim_interfaces = resolve('pim_interfaces')
    try:
        t_1 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_2((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode)) or (t_1((undefined(name='pim_interfaces') if l_0_pim_interfaces is missing else l_0_pim_interfaces)) > 0)):
        pass
        yield '\n### PIM Sparse Mode\n'
        template = environment.get_template('documentation/router-pim-sparse-mode.j2', 'documentation/pim-sparse-mode.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/pim-sparse-mode-interfaces.j2', 'documentation/pim-sparse-mode.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event

blocks = {}
debug_info = '7=25&11=28&13=31'