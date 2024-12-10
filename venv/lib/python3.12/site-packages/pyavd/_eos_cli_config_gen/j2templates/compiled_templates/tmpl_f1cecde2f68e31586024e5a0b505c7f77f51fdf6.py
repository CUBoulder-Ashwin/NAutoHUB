from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/policy-maps-copp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_policy_maps = resolve('policy_maps')
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
    if t_3(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'copp_system_policy')):
        pass
        yield '\n### Control-plane Policy Map\n\n#### Control-plane Policy Map Summary\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'copp_system_policy'), 'classes')):
            pass
            yield '\n##### copp-system-policy\n\n| Class | Shape | Bandwidth | Rate Unit |\n| ----- | ----- | --------- | --------- |\n'
            for l_1_class in t_2(environment.getattr(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'copp_system_policy'), 'classes'), 'name'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_class, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_class, 'shape'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_class, 'bandwidth'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_class, 'rate_unit'), '-'))
                yield ' |\n'
            l_1_class = missing
        yield '\n#### COPP Policy Maps Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/policy-maps-copp.j2', 'documentation/policy-maps-copp.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&18=36&19=40&26=50'