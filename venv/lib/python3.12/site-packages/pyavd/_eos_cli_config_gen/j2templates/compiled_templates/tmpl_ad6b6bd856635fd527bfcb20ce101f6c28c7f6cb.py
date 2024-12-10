from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-igmp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_igmp = resolve('router_igmp')
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
    if t_2((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp)):
        pass
        yield '\n### Router IGMP\n\n#### Router IGMP Summary\n\n| VRF | SSM Aware | Host Proxy |\n| --- | --------- | ---------- |\n'
        if t_2(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'ssm_aware')):
            pass
            yield '| - | Enabled | - |\n'
        if t_2(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'host_proxy_match_mroute')):
            pass
            yield '| default | - | '
            yield str(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'host_proxy_match_mroute'))
            yield ' |\n'
        for l_1_vrf in t_1(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'vrfs'), 'name'):
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_vrf, 'host_proxy_match_mroute')):
                pass
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | - | '
                yield str(environment.getattr(l_1_vrf, 'host_proxy_match_mroute'))
                yield ' |\n'
        l_1_vrf = missing
        yield '\n#### Router IGMP Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-igmp.j2', 'documentation/router-igmp.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&15=27&18=30&19=33&21=35&22=38&23=41&30=47'