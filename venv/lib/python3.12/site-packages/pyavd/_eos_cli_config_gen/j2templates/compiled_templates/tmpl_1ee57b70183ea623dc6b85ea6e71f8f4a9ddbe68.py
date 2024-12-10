from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/virtual-source-nat-vrfs.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_virtual_source_nat_vrfs = resolve('virtual_source_nat_vrfs')
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
    if t_3((undefined(name='virtual_source_nat_vrfs') if l_0_virtual_source_nat_vrfs is missing else l_0_virtual_source_nat_vrfs)):
        pass
        yield '\n## Virtual Source NAT\n\n### Virtual Source NAT Summary\n\n| Source NAT VRF | Source NAT IPv4 Address | Source NAT IPv6 Address |\n| -------------- | ----------------------- | ----------------------- |\n'
        for l_1_vrf in t_2((undefined(name='virtual_source_nat_vrfs') if l_0_virtual_source_nat_vrfs is missing else l_0_virtual_source_nat_vrfs), 'name'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield ' | '
            yield str(t_1(environment.getattr(l_1_vrf, 'ip_address'), '-'))
            yield ' | '
            yield str(t_1(environment.getattr(l_1_vrf, 'ipv6_address'), '-'))
            yield ' |\n'
        l_1_vrf = missing
        yield '\n### Virtual Source NAT Configuration\n\n```eos\n'
        template = environment.get_template('eos/virtual-source-nat-vrfs.j2', 'documentation/virtual-source-nat-vrfs.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=37&22=45'