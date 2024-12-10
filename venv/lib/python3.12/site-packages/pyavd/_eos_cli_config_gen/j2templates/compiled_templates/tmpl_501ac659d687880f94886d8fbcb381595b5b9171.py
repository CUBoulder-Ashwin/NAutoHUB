from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/vrfs.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vrfs = resolve('vrfs')
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
        t_3 = environment.filters['rejectattr']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'rejectattr' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs)):
        pass
        yield '\n## VRF Instances\n\n### VRF Instances Summary\n\n| VRF Name | IP Routing |\n| -------- | ---------- |\n'
        for l_1_vrf in t_2(t_3(context, t_1((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs), []), 'name', 'arista.avd.defined', 'default'), 'name'):
            l_1_ip_routing = missing
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_vrf, 'ip_routing_ipv6_interfaces'), True):
                pass
                l_1_ip_routing = 'enabled (ipv6 interface)'
                _loop_vars['ip_routing'] = l_1_ip_routing
            elif t_4(environment.getattr(l_1_vrf, 'ip_routing'), True):
                pass
                l_1_ip_routing = 'enabled'
                _loop_vars['ip_routing'] = l_1_ip_routing
            else:
                pass
                l_1_ip_routing = 'disabled'
                _loop_vars['ip_routing'] = l_1_ip_routing
            yield '| '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield ' | '
            yield str((undefined(name='ip_routing') if l_1_ip_routing is missing else l_1_ip_routing))
            yield ' |\n'
        l_1_vrf = l_1_ip_routing = missing
        yield '\n### VRF Instances Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/vrfs.j2', 'documentation/vrfs.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&15=39&16=43&17=45&18=47&19=49&21=53&23=56&29=62'