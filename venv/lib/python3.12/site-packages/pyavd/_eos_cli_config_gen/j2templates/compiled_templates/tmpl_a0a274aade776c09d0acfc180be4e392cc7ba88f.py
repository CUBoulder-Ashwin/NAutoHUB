from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/lacp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_lacp = resolve('lacp')
    l_0_row_range = resolve('row_range')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp)):
        pass
        yield '\n## LACP\n\n### LACP Summary\n\n| Port-id range | Rate-limit default | System-priority |\n| ------------- | ------------------ | --------------- |\n'
        if (t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'port_id'), 'range'), 'begin')) and t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'port_id'), 'range'), 'end'))):
            pass
            l_0_row_range = str_join((environment.getattr(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'port_id'), 'range'), 'begin'), ' - ', environment.getattr(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'port_id'), 'range'), 'end'), ))
            context.vars['row_range'] = l_0_row_range
            context.exported_vars.add('row_range')
        else:
            pass
            l_0_row_range = '-'
            context.vars['row_range'] = l_0_row_range
            context.exported_vars.add('row_range')
        yield '| '
        yield str((undefined(name='row_range') if l_0_row_range is missing else l_0_row_range))
        yield ' | '
        yield str(t_1(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'rate_limit'), 'default'), '-'))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'system_priority'), '-'))
        yield ' |\n\n### LACP Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/lacp.j2', 'documentation/lacp.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'row_range': l_0_row_range})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=25&15=28&16=30&18=35&20=39&25=45'