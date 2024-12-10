from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/class-maps.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_class_maps = resolve('class_maps')
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
    if t_2(environment.getattr((undefined(name='class_maps') if l_0_class_maps is missing else l_0_class_maps), 'qos')):
        pass
        yield '\n### QOS Class Maps\n\n#### QOS Class Maps Summary\n\n| Name | Field | Value |\n| ---- | ----- | ----- |\n'
        for l_1_class_map in t_1(environment.getattr((undefined(name='class_maps') if l_0_class_maps is missing else l_0_class_maps), 'qos'), 'name'):
            l_1_namespace = resolve('namespace')
            l_1_row = missing
            _loop_vars = {}
            pass
            l_1_row = context.call((undefined(name='namespace') if l_1_namespace is missing else l_1_namespace), _loop_vars=_loop_vars)
            _loop_vars['row'] = l_1_row
            if t_2(environment.getattr(l_1_class_map, 'cos')):
                pass
                if not isinstance(l_1_row, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_row['type'] = 'cos'
                if not isinstance(l_1_row, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_row['value'] = environment.getattr(l_1_class_map, 'cos')
            elif t_2(environment.getattr(l_1_class_map, 'vlan')):
                pass
                if not isinstance(l_1_row, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_row['type'] = 'vlan'
                if not isinstance(l_1_row, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_row['value'] = environment.getattr(l_1_class_map, 'vlan')
            elif t_2(environment.getattr(environment.getattr(l_1_class_map, 'ip'), 'access_group')):
                pass
                if not isinstance(l_1_row, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_row['type'] = 'acl'
                if not isinstance(l_1_row, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_row['value'] = environment.getattr(environment.getattr(l_1_class_map, 'ip'), 'access_group')
            else:
                pass
                if not isinstance(l_1_row, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_row['type'] = '-'
                if not isinstance(l_1_row, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_row['value'] = '-'
            yield '| '
            yield str(environment.getattr(l_1_class_map, 'name'))
            yield ' | '
            yield str(environment.getattr((undefined(name='row') if l_1_row is missing else l_1_row), 'type'))
            yield ' | '
            yield str(environment.getattr((undefined(name='row') if l_1_row is missing else l_1_row), 'value'))
            yield ' |\n'
        l_1_class_map = l_1_namespace = l_1_row = missing
        yield '\n#### Class-maps Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/class-maps.j2', 'documentation/class-maps.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('eos/class-maps-pbr.j2', 'documentation/class-maps.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&15=27&16=32&17=34&18=36&19=39&20=42&21=44&22=47&23=50&24=52&25=55&27=60&28=63&30=67&36=75&37=78'