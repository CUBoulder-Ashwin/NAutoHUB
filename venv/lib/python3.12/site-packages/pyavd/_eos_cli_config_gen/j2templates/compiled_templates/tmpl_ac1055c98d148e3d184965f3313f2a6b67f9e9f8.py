from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/maintenance-mode.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_bgp_groups = resolve('bgp_groups')
    l_0_interface_groups = resolve('interface_groups')
    l_0_maintenance = resolve('maintenance')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if ((t_1((undefined(name='bgp_groups') if l_0_bgp_groups is missing else l_0_bgp_groups)) or t_1((undefined(name='interface_groups') if l_0_interface_groups is missing else l_0_interface_groups))) or t_1((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance))):
        pass
        yield '\n## Maintenance Mode\n'
        template = environment.get_template('documentation/bgp-groups.j2', 'documentation/maintenance-mode.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/interface-groups.j2', 'documentation/maintenance-mode.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/maintenance.j2', 'documentation/maintenance-mode.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event

blocks = {}
debug_info = '7=20&13=23&15=26&17=29'